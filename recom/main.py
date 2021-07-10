import pandas as pd
import numpy as np

features = ["Comedy","Drama","Action","Romance","Adventure","Thriller","Crime","Fantasy","Children","Animation","Sci-Fi","Horror","Mystery","IMAX","Musical","Documentary","War","Western","(no genres listed)",
            "Adam Sandler","Will Ferrell"]  # top 2 watched movie's actor

data = pd.read_csv("formatted_data/data_train_111.csv")
datatest = pd.read_csv("formatted_data/data_test_111.csv")
data["userRating"] = pd.to_numeric(data["userRating"])

# formatting data to have one hot encoding features
def reformat(data, features):
    for i,f in enumerate(features):
        data[f] = 0.0
        for index, row in data.iterrows():
            if i < 19:
                if f in row["genres"]:
                    data.loc[index, f] = 1.0
            else:
                if f in row["actors"]:
                    data.loc[index, f] = 1.0 # change this value to create weighted features
    data = data.drop(["title","userId","imdbRating","genres","directors","actors"],axis=1)
    return data

# 1. Format the Data
data = reformat(data, features)
datatest = reformat(datatest, features)

# see the result
data.to_csv("train_matrix.csv", sep=',',encoding='utf-8', index=False)

# 2. Get User Profile
# Multiply features weight by User Rating
for f in features:
    data[f] *= data["userRating"]

sum_score = data.loc[:,"Comedy":].sum(axis=0)
sum_ones = data.loc[:,"Comedy":].astype(bool).sum(axis=0) # total non zero value
user_profile = sum_score / sum_ones # averaging
print(user_profile)

# 3. Scoring the Datatest
datatest["value"] = 0.0
for i in range(len(datatest)):
    datatest.loc[i,"Comedy":]*=user_profile
    
for index, row in datatest.iterrows():
    test_sum_score = datatest.loc[index,"Comedy":].sum()
    test_sum_ones = datatest.loc[index,"Comedy":].astype(bool).sum() # total non zero value
    datatest.loc[index, "value"] = test_sum_score / test_sum_ones # averaging

# Save the result
datatest.loc[:,["imdbId", "userRating","value"]].to_csv("result.csv", sep=',',encoding='utf-8', index=False)