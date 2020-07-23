#!/usr/bin/env python3

import os
import sys


def identify_path():
    path = input("Enter pathname: ")

    if os.path.exists(path):
        for each in os.listdir(path):
            f_d_p = os.path.join(path, each)
            if os.path.isfile(each):
                print(f"{f_d_p} is a file.")
            else:
                print(f"{f_d_p} is a directory.")
    else:
        print(f"{path} does not exists. Please enter valid path.")
        sys.exit()

