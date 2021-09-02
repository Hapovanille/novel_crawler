import requests
from bs4 import BeautifulSoup
import time

from chapter_crawler import fetch_and_save_by_path
from common import *

total_chapter_counter = 0

for i in range(1, toc_page_number):
    print(bcolors.HEADER + "PAGE " + str(i) + bcolors.ENDC)
    url = toc_url + str(i)
    response = requests.get(url, headers=headers_mobile)

    soup = BeautifulSoup(response.content, "lxml")
    title_list = soup.find(id="alllist").find_all('li')

    for a in title_list:
        title = a.text
        path = a.find('a', href=True)['href']
        if len(path) >= 15:
            total_chapter_counter += 1
            chapter_filename = chapter_dir + "/" + \
                str(total_chapter_counter).zfill(3) + " " + title + ".txt"

            status = fetch_and_save_by_path(
                chapter_filename, total_chapter_counter, path)
            if status == 0:
                time.sleep(sleep_time)
