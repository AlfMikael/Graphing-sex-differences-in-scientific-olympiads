Scientific Olympiad Grapher

The purpose of this code is to visualize sex differences within scientific olympiads, but could conceivably do so
for any test that provides a first name and a point-score. Data from the Norwegian Olympids are provided. Delete that
data and replace it with your own to graph another country.

How to use:
First, put your data in the following form, in a csv-file:

points,first_name

value1,name1

value2,name2

value3,name3

etc.

Then name your files in the following way: [competition]_[year].csv. Then put all data files into the raw_data folder.
Then, in the data.py change the METADATA dict so that it corresponds to the files your have put there. Then change
the country to the correct one. Then open the run.py and comment out everything except the "data.generate_csv" line. This will
provide a list of names for which the gender could not be identified. Copy-paste these names to the bottom of "new_names.txt".
Then and place an "M" or "F" in front of them (for male and female). Go back to run.py and run "add.add_names." At this point
you can uncomment every line and run the entire run.py script. This will have generated the finished csv files in /csv/ and the
images in /graphics/.
