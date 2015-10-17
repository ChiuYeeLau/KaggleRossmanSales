
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

print 'Read Data!'
Train = pd.read_csv('train.csv')
Test = pd.read_csv('test.csv')
Store = pd.read_csv('store.csv')

print len(Train)
print len(Test)


# In[3]:

Train = pd.merge(Train, Store)
Test = pd.merge(Test, Store)
print len(Train)

Train = Train[Train.Sales != 0]
print len(Train)


# In[4]:

from datetime import datetime

def Parse_Time (x):
    DD = datetime.strptime(x, "%Y-%m-%d")
    Day = DD.day
    Month = DD.month
    Year = DD.year
    return Year, Month, Day


# In[5]:

Train["Year"], Train["Month"], Train["Day"] = zip(*Train["Date"].apply(Parse_Time))


# In[6]:

Test["Year"], Test["Month"], Test["Day"] = zip(*Test["Date"].apply(Parse_Time))


# In[7]:

Train_Target = Train.Sales
# print Train


# In[8]:

Test_ID = Test.Id
Train = Train.drop(['Date', 'Sales', 'Customers', 'PromoInterval'], axis = 1)
Test = Test.drop(['Date', 'Id', 'PromoInterval'], axis = 1)

# print Train.head()
# print Test.head()
# print len(Train)


# In[9]:

Store_Type_List = ['a', 'b', 'c', 'd']
Assortment_List = ['a', 'b', 'c']
Holiday_List = [0L, '0', 'a', 'b', 'c']

def Store_Type(x):
    return Store_Type_List.index(x)

def Assortment(x):
    return Assortment_List.index(x)

def Holiday(x):
    return Holiday_List.index(x)

Train.StoreType = Train.StoreType.apply(Store_Type)
Train.Assortment = Train.Assortment.apply(Assortment)

Test.StoreType = Test.StoreType.apply(Store_Type)
Test.Assortment = Test.Assortment.apply(Assortment)

Train.StateHoliday = Train.StateHoliday.apply(Holiday)
Test.StateHoliday = Test.StateHoliday.apply(Holiday)


# In[10]:

Train = Train.fillna(0)
Test = Test.fillna(0)

# print Train.head()
# print Test.head()


# In[11]:

print 'Train Random Forests!'

from sklearn.ensemble.forest import RandomForestRegressor
RF = RandomForestRegressor(n_estimators = 500, random_state = 0)


# In[12]:

Rows = np.random.choice(Train.index.values, 400000)
Sampled_Train = Train.ix[Rows]
Sample_Train_Target = Train_Target.ix[Rows]

# RF.fit(Sampled_Train, Sample_Train_Target)
RF.fit(Train, Train_Target)


# In[ ]:

print 'Predict!'

Test_Predict = RF.predict(Test.as_matrix())


# In[ ]:

print Test_Predict.shape


# In[ ]:

from collections import OrderedDict

Submission = pd.DataFrame(data = OrderedDict([('Id', Test_ID), ('Sales', Test_Predict)]))
Submission.to_csv('Submission_RF.csv', index = False)


# In[ ]:

Test_Predict.shape


# In[ ]:



