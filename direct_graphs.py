#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script creates images that displays the scores of the best girls and the best
boys next to each other."""

import pandas as pd
import matplotlib.pyplot as plt
import math
import data

def define_axis(ax, competition, year, draw_median_line=False):
    """ This function retrieves the data and draws in on the given axis. It uses
    the median of all participants as the reference-point to compare scores. Each
    participant's score is displayed as a multiple of the median.
    :param ax: axes
    :param competition: String
    :param year: number
    :param draw_median_line: boolean
    :return: axes
    """
    df = data.get_dataframe(competition, year)
    df = df[(df.sex == "male") | (df.sex == "female")][["points", "sex"]]
    df_boys = df[df.sex == "male"]
    df_girls = df[df.sex == "female"]
    df_boys.index = pd.RangeIndex(len(df_boys.index))
    df_girls.index = pd.RangeIndex(len(df_girls.index))
    df.index = pd.RangeIndex(len(df.index))
    median_nr = len(df.index)/2

    if median_nr % 1 == 0:
        median = df.iloc[int(median_nr), 0]
    else:
        ceil = math.ceil(median_nr)
        floor = math.floor(median_nr)
        median = (df.iloc[ceil, 0] + df.iloc[floor, 0])/2

    ax.plot(df_boys.index, df_boys.points/median, color="blue", label="Boys")
    ax.plot(df_girls.index, df_girls.points/median, color="red", label="Girls")
    if draw_median_line==True:
        ax.plot(df_boys.index, [1]*len(df_boys.index), color="black")
    return ax

def create_individual_images():
    """ Creates an image for each competition and for each year. This will
    create a lot of images.
    """
    for competition in ["physics", "chemistry", "informatics", "mathematics"]:
        for year in data.get_years(competition):
            fig = new_fig()
            ax = fig.add_subplot(111)
            define_axis(ax, competition, year, draw_median_line=False)
            ax.set_title(f"{competition} {year}")
            ax.set_ylabel("of median")
            ax.set_xlabel("participants")
            ax.legend()
            fig.savefig(f"graphics/direct/{competition}_{year}.png")
            fig.clf()
            print(f"Generated {competition} images ")

def new_fig():
    return plt.figure(figsize=(8, 6), dpi=160)
    return plt.figure(figsize=(8, 6), dpi=160)

def create_4_images():
    """ This function creates a 2x2 grid that displays the competitions next to each other.
    """
    # common_years could be found programmatically.
    common_years = [2017, 2018]
    for year in common_years:
        fig = new_fig()
        fig.subplots_adjust(hspace=0.6, wspace=0.4)
        ax_inf = fig.add_subplot(221)
        ax_chem = fig.add_subplot(222)
        ax_phys = fig.add_subplot(223)
        ax_math = fig.add_subplot(224)
        axes = [ax_phys, ax_chem, ax_inf, ax_math]
        competitions = ["informatics",  "chemistry", "physics", "mathematics"]
        for competition, ax in zip(competitions, axes):
            define_axis(ax, competition, year, draw_median_line=False)
            ax.set_title(f"{competition} {year}")
            ax.set_ylabel("of median")
            ax.set_xlabel("participants")
            ax.legend()
            fig.savefig(f"graphics/direct/all_in_1_{year}.png")

        plt.clf()


#def create_custom_image():
    # year =
    # competition =
    # year =
    # fig = new_fig()
    # ax = fig.add_subplot(111)
    #define_axis(ax, competition, year, draw_median_line=False)


