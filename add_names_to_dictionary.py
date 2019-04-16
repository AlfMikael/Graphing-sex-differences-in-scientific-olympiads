#!/usr/bin/env python
__author__ = "Alf Mikael Constantinou"
__license__ = "GPL3"
__email__ = "amikaelc@protonmail.com"

""" This script pieces together a file of names for the gender_guesser, based on the original
dictionary provided by the author, along with additional name-gender pairs as needed.
"""


def add_names(print_output=False):

    # Loading the source-files and retrieving the data
    header_file = open("gender_guesser/data/header.txt", "r", encoding="utf-8")
    header_string = header_file.read()

    base_file = open("gender_guesser/data/base.txt", "r", encoding="utf-8")
    base_list = base_file.readlines()

    new_lines_file = open("new_names.txt", "r", encoding="utf-8")

    new_dict_file = open("gender_guesser/data/nam_dict.txt", "w+", encoding="utf-8")

    # New lines are the whole lines that are to be places into the dictionary, while
    # new_names are just the names.
    new_lines = []
    new_names = []
    for line in new_lines_file.readlines():
        line = line.strip()
        bit1 = " " * (46 - len(line)) + "1"
        bit2 = " " * 38 + "$\n"
        new_lines.append(line + bit1 + bit2)
        new_names.append(line.split()[1])

    # The new names will displace the old ones by the same name.
    for name in new_names:
        name = name + " "
        # Without the " " at the end it will overmatch.
        for line in base_list:
            if name in line:
                base_list.remove(line)
                if print_output==True:
                    print(f"Added and or changed {name}")

    # First placing all original lines into the dictionary.
    dict = {}
    for el in base_list:
        dict[el[3:]] = el[:3]

    # Then putting in the new lines, supplanting the old ones if necessary.
    for el in new_lines:
        dict[el[2:]] = el[:2] + " "

    # Sorting the keys and generating a list of strings which will be the lines in the file of names.
    keys = sorted(dict.keys())
    sorted_list = []
    for key in keys:
        sorted_list.append(dict[key] + key)

    # Writing into file
    new_dict_file.write(header_string)
    for line in sorted_list:
        new_dict_file.write(line)
