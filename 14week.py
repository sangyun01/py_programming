# 15장 판다스

import pandas as pd

titanic = pd.read_csv("C://Users//User//Desktop//중앙대//2학년//2학기//객지프//과제//titanic.csv")

# print(max(titanic.Age))
# print(titanic.Age.max())
# print(titanic["Age"].max())

titanic.to_excel("C://Users//User//Desktop//중앙대//2학년//2학기//객지프//과제//titanic.xlsx", sheet_name='passengers',index=False)

# print(titanic[titanic.Age < 20].head())
# print(titanic[titanic.Pclass.isin([1,3])])
print(titanic.loc[titanic.Age < 20, "Name"])
print(titanic.sort_values(by=["Pclass", "Age"], ascending=False).head())