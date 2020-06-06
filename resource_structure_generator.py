
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:11:21 2020

@author: Adam
"""

import os, functools, json

path = os.getcwd()

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


data = get_directory_structure(path + "\\Resources")

for i in data['Resources']:
    for o in data['Resources'][i]:
        data['Resources'][i][o] = o
        
with open('generated_resource_structure.json', 'w') as outfile:
    json.dump(data, outfile, indent=4,)