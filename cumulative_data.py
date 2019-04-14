import science_olympiads as so
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def mean_fractions(contest, year_list):
    my_df = pd.DataFrame()
    for year in year_list:
        df1 = so.get_dataframe(contest, year)[["points", "sex"]]
        df1 = df1[(df1.sex == "male") | (df1.sex == "female")]
        df1["year"] = year
        df1.insert(2, "male_cum", np.nan)
        df1.insert(3, "female_cum", np.nan)
        df1.insert(4, "fraction", np.nan)
        df1.index = pd.RangeIndex(len(df1.index))
        male_cum, female_cum = (0,0)
        for index, row in df1.iterrows():
            if row[1] == "female":
                female_cum += 1
            if row[1] == "male":
                male_cum += 1
            df1.iloc[index, 2] = male_cum
            df1.iloc[index, 3] = female_cum
            if (male_cum + female_cum >= 10):
                df1.iloc[index, 4] = female_cum / (male_cum + female_cum)
        my_df[year] = df1.fraction
    my_df['mean'] = my_df.mean(axis=1)
    return my_df



fig = plt.figure()

ax = fig.add_subplot(111)

df1 = mean_fractions("physics", so.PHYSICS_YEARS)
print(df1['mean'].rolling(5).sum())

ax.plot(df1.index, df1['mean'], color="blue", label="Physics")

df1 = mean_fractions("mathematics", so.MATH_YEARS)
ax.plot(df1.index, df1['mean'], color="red", label="Mathematics")

df1 = mean_fractions("chemistry", so.CHEMISTRY_YEARS)
ax.plot(df1.index, df1['mean'], color="purple", label="Chemistry")

df1 = mean_fractions("informatics", so.INFORMATICS_YEARS)
ax.plot(df1.index, df1['mean'], color="black", label="Informatics")

ax.axis([10,400, 0, 0.5])

#Setting labels to a percentage
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

ax.legend()
ax.plot()
plt.show()
