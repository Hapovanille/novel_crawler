from chapter_crawler import fetch_and_save_by_path

path = '/book_72861/398120.html'
chapter_filename = './chapters/000 第122章 伏尔加河畔的秘密基地.txt'
counter = 0

fetch_and_save_by_path(chapter_filename, counter, path)
