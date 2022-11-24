import pandas as pd

tips = pd.read_csv('tips.csv')
print(tips)
print(tips.head(8))
print(tips.tail(8))
print(tips.info())