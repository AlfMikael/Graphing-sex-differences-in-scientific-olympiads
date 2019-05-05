#!/usr/bin/env python
__author__ = "Alf Mikael Constantinou"
__license__ = "GPL3"
__email__ = "amikaelc@protonmail.com"

"""This script creates images that show the proportion of participants that are girls,
depending on how many participants you include. The trend so far has been that the more participants,
the higher the proportion of girls.

Change the function "create_images" to produce the images you want."""

import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def mean_proportion(contest, year_list):
    my_df = pd.DataFrame()

    for year in year_list:
        df1 = data.get_dataframe(contest, year)[["points", "sex"]]
        df1 = df1[(df1.sex == "male") | (df1.sex == "female")]

        df1["year"] = year
        df1.insert(2, "male_cum", np.nan)
        df1.insert(3, "female_cum", np.nan)
        df1.insert(4, "fraction", np.nan)
        df1.index = pd.RangeIndex(len(df1.index))
        male_cum, female_cum = (0,0)
        for index, row in df1.iterrows():
            if row[1] == "female": female_cum += 1
            if row[1] == "male": male_cum += 1
            df1.iloc[index, 2] = male_cum
            df1.iloc[index, 3] = female_cum

            # Cutoff at 10 to avoid erratic graph
            if male_cum + female_cum >= 10:
                df1.iloc[index, 4] = female_cum / (male_cum + female_cum)
        my_df[year] = df1.fraction
    my_df['mean'] = my_df.mean(axis=1)
    return my_df


def graph(ax, competitions, length=0):
    colors = {"physics": "blue", "chemistry": "purple", "informatics": "black", "mathematics": "red"}

    for competition in competitions:
        df = mean_proportion(competition, data.get_years(competition))
        ax.plot(df.index, df['mean'], color=colors.get(competition), label=competition)

        #Setting labels to display percentage
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

        #Length will be max length, unless otherwise specified
        if length != 0:
            ax.set_xlim(0,length)
        ax.set_ylabel("% girls")
        ax.set_xlabel("participants")
        ax.legend()


def create_images():
    y_max = 0.3

    # Short graph with everything
    competitions = ["informatics", "physics", "mathematics", "chemistry"]
    length = 60
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylim(0,y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/short_all.png")
    plt.close(fig)

    # Medium length graph with everything
    competitions = ["informatics", "physics", "mathematics", "chemistry"]
    fig = plt.figure()
    length = 150
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/medium_all.png")
    plt.close(fig)

    # Long graph with everything
    competitions = ["informatics", "physics", "mathematics", "chemistry"]
    fig = plt.figure()
    length = 0
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/long_all.png")
    plt.close(fig)

    # Long graph with physics only
    competitions = ["physics"]
    fig = plt.figure()
    length = 0
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/physics.png")
    plt.close(fig)

    # Long graph with chemistry only
    competitions = ["chemistry"]
    fig = plt.figure()
    length = 0
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/chemistry.png")
    plt.close(fig)

    # Long graph with informatics only
    competitions = ["informatics"]
    fig = plt.figure()
    length = 0
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/informatics.png")
    plt.close(fig)

    # Long graph with mathematics only
    competitions = ["mathematics"]
    fig = plt.figure()
    length = 0
    ax = fig.add_subplot(111)
    ax.set_ylim(0, y_max)
    graph(ax, competitions, length)
    fig.savefig("graphics/cumulative/mathematics.png")
    plt.close(fig)

