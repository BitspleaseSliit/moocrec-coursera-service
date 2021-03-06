import json
import logging
import os
import re
import time
import shutil

from distutils.version import LooseVersion as V

import bs4
import six
import requests

from .cookies import (
    AuthenticationFailed, ClassNotFound,
    get_cookies_for_class, make_cookie_values, TLSAdapter, login)
from .define import (CLASS_URL, ABOUT_URL, PATH_CACHE)
from .downloaders import get_downloader
from .workflow import CourseraDownloader
from .parallel import ConsecutiveDownloader, ParallelDownloader
from .utils import (clean_filename, get_anchor_format, mkdir_p, fix_url,
                    print_ssl_error_message,
                    decode_input, BeautifulSoup, is_debug_run,
                    spit_json, slurp_json)

# from api import expand_specializations
from .network import get_page, get_page_and_url
from .commandline import parse_args
from .extractors import CourseraExtractor

from scrapper import __version__

# Login Details
USERNAME = "bitpleasesliit@gmail.com"
PASSWORD = "sliit_bitplease"

def get_session():

    # Create a session with TLS v1.2 certificate.
    session = requests.Session()
    session.mount('https://', TLSAdapter())

    return session


def list_courses(args):

    # List enrolled courses.

    session = get_session()
    login(session, USERNAME, PASSWORD)
    extractor = CourseraExtractor(session)
    courses = extractor.list_courses()
    logging.info('Found %d courses', len(courses))
    for course in courses:
        logging.info(course)


def download_on_demand_class(session, args, class_name):

    error_occurred = False
    extractor = CourseraExtractor(session)

    cached_syllabus_filename = '%s-syllabus-parsed.json' % class_name
    if args.cache_syllabus and os.path.isfile(cached_syllabus_filename):
        modules = slurp_json(cached_syllabus_filename)
    else:
        error_occurred, modules = extractor.get_modules(
            class_name,
            args.reverse,
            args.unrestricted_filenames,
            args.subtitle_language,
            args.video_resolution,
            args.download_quizzes,
            args.mathjax_cdn_url,
            args.download_notebooks
        )

    if is_debug_run or args.cache_syllabus():
        spit_json(modules, cached_syllabus_filename)

    if args.only_syllabus:
        return error_occurred, False

    downloader = get_downloader(session, class_name, args)
    downloader_wrapper = ParallelDownloader(downloader, args.jobs) \
        if args.jobs > 1 else ConsecutiveDownloader(downloader)

    # obtain the resources

    ignored_formats = []
    if args.ignore_formats:
        ignored_formats = args.ignore_formats.split(",")

    course_downloader = CourseraDownloader(
        downloader_wrapper,
        commandline_args=args,
        class_name=class_name,
        path=args.path,
        ignored_formats=ignored_formats,
        disable_url_skipping=args.disable_url_skipping
    )

    completed = course_downloader.download_modules(modules)

    # Print skipped URLs if any
    if course_downloader.skipped_urls:
        print_skipped_urls(course_downloader.skipped_urls)

    if course_downloader.failed_urls:
        print_failed_urls(course_downloader.failed_urls)

    return error_occurred, completed


def print_skipped_urls(skipped_urls):
    logging.info('The following URLs (%d) have been skipped and not '
                 'downloaded:', len(skipped_urls))

    logging.info('-' * 80)
    for url in skipped_urls:
        logging.info(url)
    logging.info('-' * 80)


def print_failed_urls(failed_urls):
    logging.info('The following URLs (%d) could not be downloaded:',
                 len(failed_urls))
    logging.info('-' * 80)
    for url in failed_urls:
        logging.info(url)
    logging.info('-' * 80)


def download_class(session, args, class_name):

    logging.debug('Downloading new style (on demand) class %s', class_name)
    return download_on_demand_class(session, args, class_name)

# 01
def scrapper(course_path):

    # Main entry point for execution as a program

    args = parse_args()

    args.class_names = [course_path] # class Name should 

    logging.info('MOCCRec args %s', args) # XXXX
    logging.info('MOCCRec version %s', __version__) # XXXX
    completed_classes = []
    classes_with_errors = []

    mkdir_p(PATH_CACHE, 0o700)
    if args.clear_cache:
        shutil.rmtree(PATH_CACHE)
    if args.list_courses:
        logging.info('Listing enrolled courses')
        list_courses(args)
        return

    session = get_session()
    login(session, USERNAME, PASSWORD)

    for class_index, class_name in enumerate(args.class_names):
        try:
            logging.info('Downloading class: %s (%d / %d)', class_name, class_index + 1, len(args.class_names))
            error_occurred, completed = download_class(session, args, class_name)
            if completed:
                completed_classes.append(class_name)
            if error_occurred:
                classes_with_errors.append(class_name)
        except requests.exceptions.HTTPError as e:
            logging.error('HTTPError %s', e)
            if is_debug_run():
                logging.exception('HTTPError %s', e)
        except requests.exceptions.SSLError as e:
            logging.error('SSLError %s', e)
            print_ssl_error_message(e)
            if is_debug_run():
                raise
        except ClassNotFound as e:
            logging.error('Could not find class: %s', e)
        except AuthenticationFailed as e:
            logging.error('Could not authenticate: %s', e)

        if class_index + 1 != len(args.class_names):
            logging.info('Sleeping for %d seconds before downloading next course. ',
                         args.download_delay)
            time.sleep(args.download_delay)

    if completed_classes:
        logging.info('-' * 80)
        logging.info(
            "Classes which appear completed: " + " ".join(completed_classes))

    if classes_with_errors:
        logging.info('-' * 80)
        logging.info('The following classes had errors during the syllabus'
                     ' parsing stage.')
        for class_name in classes_with_errors:
            logging.info('%s (https://www.coursera.org/learn/%s)',
                         class_name, class_name)

    if completed_classes.count > 0:
        return True
    else:
        return False


# if __name__ == '__main__':
#     main()
