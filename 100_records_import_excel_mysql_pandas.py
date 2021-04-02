#!/usr/bin/env python
# coding: utf-8

# In[84]:


from sqlalchemy import create_engine

import pymysql

import pandas as pd


# In[5]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ruth"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE A_100recordsDB")


# In[104]:


from sqlalchemy import create_engine

import pymysql

import pandas as pd
# Credentials to database connection
hostname="localhost"
dbname="a_100recordsdb"
uname="root"
pwd="ruth"

# create dataframe from excel file
df= pd.read_excel("C:\\Users\\user\\Desktop\\python-files\\100 Records2.xlsx")

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
        .format(host=hostname, db=dbname, user=uname, pw=pwd))


# Convert dataframe to sql table                                   
df.to_sql('the_100_records_tbl2', engine, index=False)

df = pd.read_sql_query("SELECT * FROM the_100_records_tbl2", engine)
df.head()


# In[105]:


from sqlalchemy import create_engine

import pymysql

import pandas as pd
# Credentials to database connection
hostname="localhost"
dbname="a_100recordsdb"
uname="root"
pwd="ruth"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

#engine = create_engine("mysql+pymysql://user:ruth@localhost/a_100recordsdb")

df2 = pd.read_sql_query("SELECT EmpID, NamePrefix, FirstName, MiddleInitial, LastName,Gender, EMail, Fathers_Name, Mothers_Name,Mothers_Maiden_Name, Date_of_Birth, Time_of_Birth,Age_in_Yrs,Weight_in_Kgs,Date_of_Joining,Quarter_of_Joining,Half_of_Joining,Year_of_Joining, Month_of_Joining,Month_Name_of_Joining,Short_Month,Day_of_Joining,DOW_of_Joining,Short_DOW,Age_in_Company_Years,Salary,SSN,Phone_No, Place_Name,County,City,State,Zip,Region FROM the_100_records_tbl2", engine)
df2.head()


# In[106]:


df2.columns


# In[107]:


from sqlalchemy import create_engine

import pymysql

import pandas as pd
# Credentials to database connection
hostname="localhost"
dbname="a_100recordsdb"
uname="root"
pwd="ruth"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

#engine = create_engine("mysql+pymysql://user:ruth@localhost/a_100recordsdb")

df1 = pd.read_sql_query("SELECT Password,User_Name FROM the_100_records_tbl2", engine)
df1.head()


# In[108]:


df1


# In[92]:


df.iloc[0:3,34:35]


# In[95]:


## create a dictionary containing each dataframe
df1[['Password', 'User_Name']]
df2
dfs={'Authentication':df1,'Employee Records':df2}


# In[110]:


with pd.ExcelWriter('100_records_new.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Authentication')
    df2.to_excel(writer, sheet_name='Employee Records')


# In[76]:


import os
os.getcwd()


# In[78]:


df1


# In[ ]:




