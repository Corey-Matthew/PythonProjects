#!/usr/bin/env python3

import os
import string
import platform


def search_file():
    if platform.system() == 'Windows':
        req_file = input("Enter your file name to search: ")
        possible_drives = string.ascii_uppercase
        win_drives = []
        for each_drive in possible_drives:
            if os.path.exists(each_drive + ":\\"):
                win_drives.append(each_drive + ":\\")
        for each_drive in win_drives:
            for r, d, f in os.walk(each_drive):
                for each_file in f:
                    if each_file == req_file:
                        print(os.path.join(r, each_file))

    else:
        path = "/home"
        req_file = input("Enter your file name to search: ")

        for r, d, f in os.walk(path):
            for each_file in f:
                if each_file == req_file:
                    print(os.path.join(r, each_file))


def search_extension():
    req_path = input("Enter your directory path: ")
    req_ext = input("Enter the required extension .py/.sh/.log/.txt/.json: ")
    if os.path.isfile(req_path):
        print(f"The given path {req_path} is a file. Please pass only directory path.")
    else:
        all_f_ds = os.listdir(req_path)
        if all_f_ds == 0:
            print(f"The given path {req_path} is an empty path.")
        else:
            for each_file in all_f_ds:
                if each_file.endswith(req_ext):
                    print(each_file)

search_extension()