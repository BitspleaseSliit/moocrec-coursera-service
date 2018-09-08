
import json
import logging

import requests


def get_reply(session, url, post=False, data=None, headers=None, quiet=False):


    request_headers = {} if headers is None else headers

    request = requests.Request('POST' if post else 'GET',
                               url,
                               data=data,
                               headers=request_headers)
    prepared_request = session.prepare_request(request)

    reply = session.send(prepared_request)

    try:
        reply.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if not quiet:
            logging.error("Error %s getting page %s", e, url)
            logging.error("The server replied: %s", reply.text)
        raise

    return reply


def get_page(session,
             url,
             json=False,
             post=False,
             data=None,
             headers=None,
             quiet=False,
             **kwargs):

    url = url.format(**kwargs)
    reply = get_reply(session, url, post=post, data=data, headers=headers,
                      quiet=quiet)
    return reply.json() if json else reply.text


def get_page_and_url(session, url):

    reply = get_reply(session, url)
    return reply.text, reply.url


def post_page_and_reply(session, url, data=None, headers=None, **kwargs):
    url = url.format(**kwargs)
    reply = get_reply(session, url, post=True, data=data, headers=headers)
    return reply.text, reply
