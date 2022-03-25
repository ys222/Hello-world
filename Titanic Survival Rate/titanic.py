# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:32:25 2018

@author: risha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#data = pd.read_excel('Downloads/Mesothelioma%20data%20set.xlsx')

PATH = 'F:/Kaggle projects/Titanic'

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
gender_submission = pd.read_csv('gender_submission.csv')

column_names = train_data.columns
for column in column_names:
    print(column + ' - ' + str(train_data[column].isnull().sum()))
#The columns 'Age' and 'Cabin' contains more null values.    

train_data.Survived.value_counts()    

plt = train_data.Survived.value_counts().plot('bar')
plt.set_xlabel('Survived or not')
plt.set_ylabel('Passenger Count')

plt = train_data.Pclass.value_counts().sort_index().plot('bar', title='Kuch Bhi')
plt.set_xlabel('Pclass')
plt.set_ylabel('Survival Probability')

train_data[['Pclass', 'Survived']].groupby('Pclass').count()

train_data[['Pclass', 'Survived']].groupby('Pclass').sum()

train_data[['Pclass', 'Survived']].groupby('Pclass').mean()

plt = train_data[['Pclass', 'Survived']].groupby('Pclass').mean().Survived.plot('bar')
plt.set_xlabel('Pclass')
plt.set_ylabel('Survival Probability')
#From the above results, we can say that, 1st class has high chance of surviving than the other two classes.


#Majority of them are Male.
plt = train_data.Sex.value_counts().sort_index().plot('bar')
plt.set_xlabel('Sex')
plt.set_ylabel('Passenger count')


#As we see, the survival probaility for Female is more. They might have given more priority to female than male.
plt = train_data[['Sex', 'Survived']].groupby('Sex').mean().Survived.plot('bar')
plt.set_xlabel('Sex')
plt.set_ylabel('Survival Probability')


#Most of them are from Southampton(S).
plt = train_data.Embarked.value_counts().sort_index().plot('bar')
plt.set_xlabel('Embarked')
plt.set_ylabel('Passenger count')


#Survival probability: C > Q > S
plt = train_data[['Embarked', 'Survived']].groupby('Embarked').mean().Survived.plot('bar')
plt.set_xlabel('Embarked')
plt.set_ylabel('Survival Probability')


#SibSp - Siblings/Spouse
plt = train_data.SibSp.value_counts().sort_index().plot('bar')
plt.set_xlabel('SibSp')
plt.set_ylabel('Passenger count')


#As we can see, majority of them have no Siblings/Spouse.
plt = train_data[['SibSp', 'Survived']].groupby('SibSp').mean().Survived.plot('bar')
plt.set_xlabel('SibSp')
plt.set_ylabel('Survival Probability')


#The passengers having one sibling/spouse has more survival probability.
#'1' > '2' > '0' > '3' > '4'
plt = train_data.Parch.value_counts().sort_index().plot('bar')
plt.set_xlabel('Parch')
plt.set_ylabel('Passenger count')


#As we can see, majority of them have no Children/Parents.
plt = train_data[['Parch', 'Survived']].groupby('Parch').mean().Survived.plot('bar')
plt.set_xlabel('Parch')
plt.set_ylabel('Survival Probability')


#The passengers having three children/parents has more survival probability.
#'3' > '1' > '2' > '0' > '5'


#Embarked vs Pclass
sns.factorplot('Pclass', col = 'Embarked', data = train_data, kind = 'count', size = 3)

#Majority of the passengers are Male in every class. But, the survival probability for female is high.
#Pclass vs Sex
sns.factorplot('Sex', col = 'Pclass', data = train_data, kind = 'count', size = 3)


#Embarked vs Sex
sns.factorplot('Sex', col = 'Embarked', data = train_data, kind = 'count')

#Create a new feature 'Family size' from the features 'SibSp' and 'Parch'
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1

#Remove unnecessary columns
#We can remove 'Ticket' and 'PassengerId', as they don't contribute to target class.
#Remove 'Cabin' as it has a lot of missing values in both train and test data
train_data = train_data.drop(columns=['Ticket', 'PassengerId', 'Cabin'])

#Map 'Sex' and 'Embarked' to numerical values.
train_data['Sex'] = train_data['Sex'].map({'male':0, 'female':1})
train_data['Embarked'] = train_data['Embarked'].map({'C':0, 'Q':1, 'S':2})

#Preprocess 'Name'
#Extarct title from name of the passenger and categorize them.
#Drop the column 'Name'
train_data['Title'] = train_data.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
train_data = train_data.drop(columns='Name')

train_data.Title.value_counts().plot('bar')


#Combine some of the classes and group all the rare classes into 'Others'.
train_data['Title'] = train_data['Title'].replace(['Dr', 'Rev', 'Col', 'Major', 'Countess', 'Sir', 'Jonkheer', 'Lady', 'Capt', 'Don'], 'Others')
train_data['Title'] = train_data['Title'].replace('Ms', 'Miss')
train_data['Title'] = train_data['Title'].replace('Mme', 'Mrs')
train_data['Title'] = train_data['Title'].replace('Mlle', 'Miss')

plt = train_data.Title.value_counts().sort_index().plot('bar')
plt.set_xlabel('Title')
plt.set_ylabel('Passenger count')


plt = train_data[['Title', 'Survived']].groupby('Title').mean().Survived.plot('bar')
plt.set_xlabel('Title')
plt.set_ylabel('Survival Probability')


#The survival probability for 'Mrs' and 'Miss' is high comapred to other classes.
#Map 'Title' to numerical values
train_data['Title'] = train_data['Title'].map({'Master':0, 'Miss':1, 'Mr':2, 'Mrs':3, 'Others':4})

plt = train_data[['Title', 'Survived']].groupby('Title').mean().Survived.plot('bar')
plt.set_xlabel('Title')
plt.set_ylabel('Survival Probability')



#Correlation between columns
corr_matrix = train_data.corr()

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 8))
sns.heatmap(data = corr_matrix,cmap='BrBG', annot=True, linewidths=0.2)

#There are no very highly correlated columns.
train_data.isnull().sum()
train_data['Embarked'].isnull().sum()


#There are two null values in the column 'Embarked'. Let's impute them using majority class.
#The majority class is 'S'. Impute the unkonown values (NaN) using 'S'
train_data['Embarked'] = train_data['Embarked'].fillna(2)
train_data.head()


#Let's find the columns that are useful to predict the value of Age.
corr_matrix = train_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].corr()
plt.figure(figsize=(7, 6))
sns.heatmap(data = corr_matrix,cmap='BrBG', annot=True, linewidths=0.2)

#Age is not correlated with 'Sex' and 'Fare'. So, we don't consider these two columns while imputing 'Sex'.
#'Pclass', 'SibSp' and 'Parch' are negatively correlated with 'Sex'.
#Let's fill Age with the median age of similar rows from 'Pclass', 'SibSp' and 'Parch'. If there are no similar rows, fill the age with the median age of total dataset.

NaN_indexes = train_data['Age'][train_data['Age'].isnull()].index

for i in NaN_indexes:
    pred_age = train_data['Age'][((train_data.SibSp == train_data.iloc[i]["SibSp"]) & 
                         (train_data.Parch == train_data.iloc[i]["Parch"]) & 
                         (train_data.Pclass == train_data.iloc[i]["Pclass"]))].median()
    if not np.isnan(pred_age):
        train_data['Age'].iloc[i] = pred_age
    else:
        train_data['Age'].iloc[i] = train_data['Age'].median()
        
train_data.isnull().sum()



######Read test data#########
test_data = pd.read_csv('test.csv')
test_data.isnull().sum()

test_data = test_data.drop(columns=['Ticket', 'PassengerId', 'Cabin'])

test_data['Sex'] = test_data['Sex'].map({'male':0, 'female':1})
test_data['Embarked'] = test_data['Embarked'].map({'C':0, 'Q':1, 'S':2})

test_data['Title'] = test_data.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
test_data = test_data.drop(columns='Name')

test_data['Title'] = test_data['Title'].replace(['Dr', 'Rev', 'Col', 'Major', 'Countess', 'Sir', 'Jonkheer', 'Lady', 'Capt', 'Don'], 'Others')
test_data['Title'] = test_data['Title'].replace('Ms', 'Miss')
test_data['Title'] = test_data['Title'].replace('Mme', 'Mrs')
test_data['Title'] = test_data['Title'].replace('Mlle', 'Miss')

test_data['Title'] = test_data['Title'].map({'Master':0, 'Miss':1, 'Mr':2, 'Mrs':3, 'Others':4})

test_data.isnull().sum()

NaN_indexes = test_data['Age'][test_data['Age'].isnull()].index

for i in NaN_indexes:
    pred_age = train_data['Age'][((train_data.SibSp == test_data.iloc[i]["SibSp"]) & (train_data.Parch == test_data.iloc[i]["Parch"]) & (test_data.Pclass == train_data.iloc[i]["Pclass"]))].median()
    if not np.isnan(pred_age):
        test_data['Age'].iloc[i] = pred_age
    else:
        test_data['Age'].iloc[i] = train_data['Age'].median()

title_mode = train_data.Title.mode()[0]
test_data.Title = test_data.Title.fillna(title_mode)

fare_mean = train_data.Fare.mean()
test_data.Fare = test_data.Fare.fillna(fare_mean)

test_data['FamilySize'] = test_data['SibSp'] + test_data['Parch'] + 1




from sklearn.utils import shuffle
train_data = shuffle(train_data)

X_train = train_data.drop(columns='Survived')
y_train = train_data.Survived
y_train = pd.DataFrame({'Survived':y_train.values})
X_test = test_data

X_train.to_csv('X_train.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)























