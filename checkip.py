"""
Created on Fri Sep 22 09:50:20 2017

@author: hien
"""
import re

def find_word(filename, word):
    fo = open(filename, 'r')
    res = re.findall(word, fo.read())
    fo.close()
    return res

def print_res(result):
    for item in result:
        print(item)
    print('\n\n****Found {} entries'.format(len(result)))
    
found = find_word('mbox-short.txt', r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
for x in found: 
    print(x)

    