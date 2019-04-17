#!/usr/bin/env python
__author__ = "Alf Mikael Constantinou"
__license__ = "GPL3"
__email__ = "amikaelc@protonmail.com"

""" This script pieces together a file of names for the gender_guesser, based on the original
dictionary provided by the author, along with additional name-gender pairs as needed.
"""

COUNTRIES = {"great britain": 1, "ireland": 2, "u.s.a.": 3, "italy": 4, "malta": 5, "portugal": 6,
             "spain": 7, "france": 8, "belgium": 9, "luxembourg": 10, "the netherlands": 100, "east frisia": 12, "germany": 13, "austria": 14,
            "switzerland": 15, "iceland": 16, "denmark": 17, "norway": 18, "sweden": 19, "finland": 20, "estonia": 21, "latvia": 22,
            "lithuania": 23, "poland": 24,"czech republic": 25,"slovakia": 26,"hungary": 27,"romania": 28,"bulgaria": 29,
            "bosnia and gerzegovina": 30,"croatia": 31, "kosovo": 32,"macedonia": 33,"montenegro": 34,"serbia": 35,
            "slovenia": 36,"albania": 37,"greece": 38,"russia": 39,"belarus": 40, "moldova": 41,"ukraine": 42, "armenia": 43,
            "azerbaijan": 44, "georgia": 45,"kazakhstan": 46,"turkey": 47,"arabia": 48,"israel": 49,"china": 50,"india": 51,"japan": 52,
            "korea": 53,"vietnam": 54,"other": 55
            }


def add_names(print_output=False):

    # Loading the source-files and retrieving the data
    header_file = open("gender_guesser/data/header.txt", "r", encoding="utf-8")
    header_string = header_file.read()

    base_file = open("gender_guesser/data/base.txt", "r", encoding="utf-8")
    base_list = base_file.readlines()

    new_names_file = open("new_names.txt", "r", encoding="utf-8")

    new_dict_file = open("gender_guesser/data/nam_dict.txt", "w+", encoding="utf-8")

    # New lines are the whole lines that are to be places into the dictionary, while
    # new_names are just the names.
    new_lines = []
    new_names = []
    for line in new_names_file.readlines():
        words = line.split()
        if len(words) != 3: raise ValueError(f'Wrong number of words on line: {line}')

        sex = words[0] #'M' or 'F'
        if (sex != "M") & (sex != "F"): raise ValueError(f'Wrong sex on line: {line}')

        country = words[2]
        if country not in COUNTRIES.keys(): raise ValueError(f'Country not in lise in line: {line}')

        sex_and_name = words[0] + " " + words[1]
        spaces_before_1 = 64 - COUNTRIES.get(country) - len(sex_and_name)
        bit1 = " " * spaces_before_1 + "1"
        bit2 = " " * (56 - COUNTRIES.get(country)) + "$\n"
        new_lines.append(sex_and_name + bit1 + bit2)
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
