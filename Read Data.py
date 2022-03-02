# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

import requests
from os import makedirs
from os.path import isdir
import sys

def fetchDataForDay(i):
    cookie = eval(open('Secret/adventCookie.txt', 'r').read())
    url = 'https://adventofcode.com/2021/day/' + str(i) + '/input'
    response = requests.get(url, cookies=cookie)
    response.raise_for_status() # ensure we notice bad responses
    num = "%02d" % (i,)
    if not isdir(num):
        makedirs(num)
    file = open(num + '/Problem ' +  num + ' Data.txt', 'w')
    file.write(response.text)
    file.close()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Error: Please provide the day for which you would like to get data!')
        sys.exit(0)
    i = int(sys.argv[1])
    fetchDataForDay(i)
    