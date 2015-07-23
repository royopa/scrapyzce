# -*- coding: utf-8 -*-
import requests


def get_urls():
    with open('urls_to_check.txt') as f:
        return f.read().splitlines()


def check_url(url):
    connect_timeout = 2.0
    read_timeout = 2.0
    # Get the page
    try:
        response = requests.get(url, timeout=(connect_timeout, read_timeout))

    except requests.exceptions.ConnectionError as e:
        print("Too slow! ", url, e)
        return False

    except requests.exceptions.ConnectTimeout as e:
        print("Too slow! ", url, e)
        return False

    except requests.exceptions.ReadTimeout as e:
        print("Too slow! ", url, e)
        return False

    if response.status_code == 404:
        print('Not found ', url)
        return False

    if response.status_code == 200:
        print('Found ', url)
        return True


def save_url_in_file(list):
    with open('urls_to_check.txt', 'w') as file:
        for url in list:
            file.write("{}\n".format(url))

url_base = 'http://www.zend.com/en/yellow-pages/ZEND'
i = int(input('Enter initial id: '))

while i < 999999:
    zce_id = str(i).zfill(6)
    url_to_check = url_base+zce_id
    list = get_urls()

    if check_url(url_to_check):
        if url_to_check not in list:
            list.append(url_to_check)
            save_url_in_file(list)
    i = i + 1
