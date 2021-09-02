import requests
import io
import os
import errno

from bs4 import BeautifulSoup
from common import *

if not os.path.exists(chapter_dir):
    try:
        os.makedirs(chapter_dir)
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise


def fetch_and_save_by_path(chapter_filename, counter, path):
    if os.path.isfile(chapter_filename):
        print(bcolors.WARNING + "existed:\t" + chapter_filename + bcolors.ENDC)
        return 1

    url = base_url + path

    response = requests.get(url, headers=headers_mobile)
    soup = BeautifulSoup(response.content, "lxml")
    title = soup.find(id="nr_title")
    title = str(title.string.extract()).strip()
    content = soup.find(id="nr1").find_all('p')

    if len(content) is 0:
        print(bcolors.FAIL + "failed:\t" + path + "\t" +
              title + "\t" + str(counter).zfill(3) + bcolors.ENDC)
        return 2

    body = '\n'.join([p.text for p in content])

    double_check_chapter_filename = chapter_dir + "/" + \
        str(counter).zfill(3) + " " + title + ".txt"
    if double_check_chapter_filename != chapter_filename:
        print(bcolors.WARNING + "conflicted:\t expect:" + chapter_filename +
              ", actual:" + double_check_chapter_filename + bcolors.ENDC)
        return 3

    chapter = title + '\n' + body

    chapter_output = io.open(chapter_filename, "w", encoding="utf-8")
    chapter_output.write(chapter)
    chapter_output.close()
    print(bcolors.OKGREEN + "saved:\t" +
          path + "\t" + title + "\t" + str(counter).zfill(3) + bcolors.ENDC)
    return 0
