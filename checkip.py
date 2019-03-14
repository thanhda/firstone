"""
Created on Fri Sep 22 09:50:20 2017

@author: hien
"""
import re

#find the matching words inside the input file
def find_word(filename, word):
    with open(filename, 'r') as fo:
        res = re.findall(word, fo.read())
        fo.close()
        return res

def print_res(result):
    for item in result:
        print(item)
    print(f'\n\n****Found {len(result)} entries****')
    
found = find_word('mbox-short.txt', r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
print_res(found)


    