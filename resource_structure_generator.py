# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:11:21 2020

@author: Adam
"""

import os, functools

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


colors = get_directory_structure(path + "\\Resources")['Resources']['colors']
fonts = get_directory_structure(path + "\\Resources")['Resources']['fonts']
images = get_directory_structure(path + "\\Resources")['Resources']['images']
music = get_directory_structure(path + "\\Resources")['Resources']['music']
musichd = get_directory_structure(path + "\\Resources")['Resources']['music-hd']
particles = get_directory_structure(path + "\\Resources")['Resources']['particles']
sounds = get_directory_structure(path + "\\Resources")['Resources']['sounds']
soundshd = get_directory_structure(path + "\\Resources")['Resources']['sounds-hd']
spines = get_directory_structure(path + "\\Resources")['Resources']['spines']
strings = get_directory_structure(path + "\\Resources")['Resources']['strings']

print(images)