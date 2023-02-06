#!/usr/bin/python3
"""
This program take the file add_item.json, and add the
parameters to the list inside this file.
- If the file doesn't exist create it.
- If no exist parameters do nothing or create the list if the file is empty.
"""

from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

namefile = "add_item.json"
argc = len(argv)

file_list = []

if exists(namefile):
    file_list = load_from_json_file(namefile)

if (argc == 1):
    save_to_json_file(file_list, namefile)
else:
    for index in range(1, argc):
        file_list.append(argv[index])
    save_to_json_file(file_list, namefile)
