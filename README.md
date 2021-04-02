# import_excel_mysql_pandas
## The project imports an Excel file into MySQL using Python Pandas. It then Separates the Spreadsheet programmatically into 2 separate worksheets into Sheet1]: Identified as Authentication and the Sheet2]: Employee Records.
# Quickstart
* You have to be familiar with Python pandas and writing SQL queries to execute the project.
## Import libraries/create engne
* from sqlalchemy import create_engine
* import pymysql
* import pandas as pd

# Import import mysql.connector and create a database
* mycursor = mydb.cursor()
* mycursor.execute("CREATE DATABASE A_100recordsDB")
# create dataframe from excel file
* df= pd.read_excel("C:\\Users\\user\\Desktop\\python-files\\100 Records2.xlsx")

# Create SQLAlchemy engine to connect to MySQL Database
* engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
        * .format(host=hostname, db=dbname, user=uname, pw=pwd))


# Convert dataframe to sql table                                   
* df.to_sql('the_100_records_tbl2', engine, index=False)

* df = pd.read_sql_query("SELECT * FROM the_100_records_tbl2", engine)

# Check the presence of your database and table in MySQL Workbench
![image](https://user-images.githubusercontent.com/17750481/113440674-899d7380-93f5-11eb-9104-21bfa29fef7d.png)
# Use sql queries to extract data from your MySQL DB and place in two different data frames and place in 2 separate dataframes
# Use the function below to transfer data from pandas to 2 separate excel sheet
![image](https://user-images.githubusercontent.com/17750481/113441003-252ee400-93f6-11eb-98b4-80f1e83c78f8.png)

## Output
![image](https://user-images.githubusercontent.com/17750481/113439772-ded88580-93f3-11eb-99db-5e7b45471b1c.png)

![image](https://user-images.githubusercontent.com/17750481/113439821-ef88fb80-93f3-11eb-9c17-781e44f81add.png)

