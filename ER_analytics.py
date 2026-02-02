import os
import mysql.connector  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error, accuracy_score, auc, classification_report, confusion_matrix, roc_curve, RocCurveDisplay


df=pd.read_csv('ER_Dataset.csv')

'''print(df.head())
print(df.tail())'''

'''print(df.info())
print(df.shape)'''

#print(df.isnull().sum())
# Start the sequence from 5001 for the rows where IDs are missing
# Assuming your DataFrame index aligns with the row count
df.loc[5000:, 'Visit_ID'] = range(5001, 8001)

df.to_csv('updated_ER_Dataset.csv', index=False)


#print(df.isnull().sum())
#print(df.nunique())
print(df.columns.to_list())

#EDA Analysis
#Univariate Analysis

# Distribution of Patient Waiting Time
'''sns.histplot(df['Waiting_Time_Min'], bins=30, kde=True)
plt.title("Distribution of Patient Waiting Time")
plt.xlabel("Waiting Time (Minutes)")
plt.ylabel("Frequency")
plt.show()'''


#Overcrowding Frequency
'''sns.countplot(x='Overcrowded', data=df)
plt.title("ER Overcrowding Frequency")
plt.show()
'''

#Doctor Availability
'''sns.boxplot(y=df['Doctor_Available'])
plt.title("Doctor Availability Distribution")
plt.show()
'''

#Bivariate Analysis
#Waiting Time vs Overcrowding
'''sns.boxplot(x='Overcrowded', y='Waiting_Time_Min', data=df)
plt.title("Waiting Time vs ER Overcrowding")
plt.show()
'''

#Patients in ER vs Doctor Availability
'''sns.scatterplot(x='Patients_In_ER', y='Doctor_Available', data=df)
plt.title("Patients vs Doctor Availability")
plt.show()
'''

#Season vs Overcrowding
'''sns.countplot(x='Season', hue='Overcrowded', data=df)
plt.title("Seasonal Impact on ER Overcrowding")
plt.show()
'''

#Multivariate Analysis
#Correlation Heatmap
'''plt.figure(figsize=(10,6))
sns.heatmap(df[['Waiting_Time_Min','Patients_In_ER',
                'Doctor_Available','Equipment_Usage_%',
                'Overcrowded']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Analysis of ER Variables")
plt.show()
'''


#Hour vs Day vs Patient Load (Heatmap)
'''pivot = df.pivot_table(values='Patients_In_ER',
                       index='Day',
                       columns='Hour',
                       aggfunc='mean')

sns.heatmap(pivot, cmap='YlOrRd')
plt.title("Average ER Patient Load by Day and Hour")
plt.show()
'''

#Equipment Usage, Doctors & Overcrowding
'''sns.scatterplot(x='Equipment_Usage_%',
                y='Patients_In_ER',
                hue='Overcrowded',
                data=df)
plt.title("Equipment Usage vs Patients with Overcrowding")
plt.show()
'''


#Linear Regression: 

'''X = df[['Patients_In_ER', 'Doctor_Available', 'Equipment_Usage_%']]
y = df['Waiting_Time_Min']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2_score=r2_score(y_test,y_pred)

print('Mean Squared Error:',mse)
print('R2 Score:',r2_score)'''


#Logistic Regression:

X = df[['Patients_In_ER', 'Doctor_Available', 'Equipment_Usage_%', 'Waiting_Time_Min']]
y = df['Overcrowded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

print(df['Overcrowded'].value_counts())






df.rename(columns={'Equipment_Usage_%': 'Equipment_usage_percent'}, inplace=True)


'''db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anjali@sql'
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS er_healthcare") 
db.close()
'''





# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="er_healthcare"
)

if db.is_connected():
    print("✅ Connected to MySQL successfully")

db.close()






import csv
import mysql.connector

def to_bool(value):
    return 1 if str(value).strip().lower() in ('1', 'true', 'yes') else 0

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="er_healthcare"
)

cursor = db.cursor()

sql = '''
INSERT INTO er_analytics
(Visit_Id, Hospital_Name, Arrival_Time,
 Day, Hour, Season, Waiting_Time_Min,
 Doctor_Available, Patients_In_ER, Equipment_usage_percent,
 Overcrowded, Disposition)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

with open("updated_ER_Dataset.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        row[7] = to_bool(row[7])    # Doctor_Available
        row[10] = to_bool(row[10])  # Overcrowded

        cursor.execute(sql, row)

db.commit()
cursor.close()
db.close()

print("CSV data inserted into MySQL successfully!")
     


