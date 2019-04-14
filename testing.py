import science_olympiads as so
import pandas as pd

df = so.get_dataframe("informatics", "2018")

males = df[df.sex == "male"].count()
females = df[df.sex == "female"].count()

print(males, "males to", females, "females")
print(females/(males + females))
print(males/females)