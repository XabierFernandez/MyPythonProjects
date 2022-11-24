import pandas as pd

titanic = pd.read_csv('titanic.csv')
ages = titanic["Age"]
age_sex = titanic[["Age", "Sex"]]
above_35 = titanic[titanic["Age"] > 35]
below_35 = titanic[titanic["Age"] < 35]
below_15 = titanic[titanic["Age"] < 15]
age_no_na = titanic[titanic["Age"].notna()]
young_names = titanic.loc[titanic["Age"] < 25, "Name"]

print(ages)
print(age_no_na)
print(ages.head())
print(type(titanic["Age"]))
print(titanic["Age"].shape)

print(age_sex)

print(above_35)
print(below_35)
print(below_15)
print(young_names)

print(above_35.shape)
print(below_35.shape)
print(below_15.shape)