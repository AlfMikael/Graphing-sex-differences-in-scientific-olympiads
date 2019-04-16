#!/usr/bin/env python
__author__ = "Alf Mikael Constantinou"
__license__ = "GPL3"
__email__ = "amikaelc@protonmail.com"

""" This file converts raw data in in form [point],[first_name] and uses the first name
to estimate the individual's sex. This is added to a new column and then exported using
the generate_csv function.

The dictionary "METADATA" contains which competitions there are files available for, along
with which years are available. Change this to suit your own data set, along with the
country.

"""

import pandas as pd
import os
import gender_guesser.detector as gg

METADATA = {"chemistry": [2012, 2013, 2015, 2017, 2018, 2019],
            "mathematics": [2017, 2018, 2019],
            "physics": [2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
            "informatics": [2013, 2014, 2015, 2016, 2017, 2018, 2019]

            # Add additional competitions here
            }
COUNTRY = "norway"



def get_dataframe(competition, year):
    return pd.read_csv(os.path.join(os.path.dirname(__file__), f"csv/{competition}_{year}.csv"))


def get_years(competition):
    return METADATA.get(competition)


def get_data_dict():
    return METADATA


def generate_csv(print_unknown_names=True):
    detector = gg.Detector()
    unknown_names = []
    for competition in METADATA.keys():
        for year in METADATA.get(competition):
            df = pd.read_csv(f"raw_data/{competition}_{year}.csv")
            df.columns = ["points", "first_name"]
            df.insert(1, "sex", "")
            for index, row in df.iterrows():
                first_name = df.loc[index, "first_name"]
                sex = detector.get_gender(first_name, country=COUNTRY)
                df.loc[index, "sex"] = sex

            if print_unknown_names == True:
                df_unknown = df[(df.sex != "male") & (df.sex != "female")]
                unknown_names.extend(list(df_unknown.first_name))
            del df["first_name"]
            df.to_csv(f"csv/{competition}_{year}.csv")

    if print_unknown_names==True:
        print("Unknown names:")
        for name in sorted(set(unknown_names)):
            print(name)
