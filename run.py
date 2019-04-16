#!/usr/bin/env python
__author__ = "Alf Mikael Constantinou"
__license__ = "GPL3"
__email__ = "amikaelc@protonmail.com"


import add_names_to_dictionary as add
import cumulative_graphs as cg
import data
import direct_graphs as dg





# Add new names to dictionary
add.add_names(print_output=False)

# Generate csv - files
data.generate_csv(print_unknown_names=True)

# Make cumulative graphs
cg.create_images()

# Make direct graphs
dg.create_individual_images()
dg.create_4_images()

