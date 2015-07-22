# -*- coding: utf-8 -*-
import requests


def get_urls():
    with open('urls_to_check.txt') as f:
        return f.read().splitlines()


def check_url(url):
    # Get the page
    r = requests.get(url)

    if r.status_code == 404:
        print('Not found ', url)
        return False

    if r.status_code == 200:
        print('Found ', url)
        return True


def save_url_in_file(list):
    with open('urls_to_check.txt', 'w') as file:
        for url in list:
            file.write("{}\n".format(url))

url_base = 'http://www.zend.com/en/yellow-pages/ZEND'
i = 176

while i < 999999:
    zce_id = str(i).zfill(6)
    url_to_check = url_base+zce_id
    list = get_urls()

    if check_url(url_to_check):
        if url_to_check not in list:
            list.append(url_to_check)
            save_url_in_file(list)
    i = i + 1
