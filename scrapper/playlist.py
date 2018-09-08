import os
import glob


def create_m3u_playlist(section_dir):

    path_to_return = os.getcwd()

    for (_path, subdirs, files) in os.walk(section_dir):
        os.chdir(_path)
        globbed_videos = sorted(glob.glob("*.mp4"))
        m3u_name = os.path.split(_path)[1] + ".m3u"

        if len(globbed_videos):
            with open(m3u_name, "w") as m3u:
                for video in globbed_videos:
                    m3u.write(video + "\n")
            os.chdir(path_to_return)
    os.chdir(path_to_return)

