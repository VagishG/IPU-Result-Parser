# import csv
import numpy as np
import re
import glob, os
import pandas as pd
os.chdir("./")
for file in glob.glob("*.csv"):
    d=[]

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # # Print the DataFrame in a nice tabular format
    # # print(df)
    # print(df.index.tolist())
    # print(df['2'])


    array_2d = df.values.tolist()

    num_rows = len(array_2d)
    num_cols = len(array_2d[0]) if array_2d else 0
    rolln=0
    cs=0
    # print(array_2d)
    for a in range(0,num_cols):
        if array_2d[0][a] == "CS/Remarks":
            cs=a
        elif array_2d[0][a]=="Roll no./Name":
            rolln=a
    # d["Institute"]=array_2d[0][rolln+1]
    rowno=-10
    arr=[]
    for a in range(0,num_rows):
        temp={}
        if array_2d[a][0]=="S.No.":
            continue
        if pd.isna(array_2d[a][0]) != True:
            rowno=a
            if pd.isna(array_2d[a][2])==True or     array_2d[a][0]=='0':
                continue
            # temp["Name"]=array_2d[a][2]
            temp["Name"]=array_2d[a][2].split("SID:")[0] if "SID:" in array_2d[a][2] else array_2d[a][2]
            for i in range(3,num_cols-1):
                if pd.isna(array_2d[a][i])!=True :
                    arr.append(array_2d[a][i])
            temp["Subjects"]=arr 
            temp["Credits"]=array_2d[a][num_cols-1] 
            d.append(temp)
            # print(array_2d[a])
            # print()
        if rowno+2 == a:
            # print(array_2d[a])
            marks=[]
            for i in range(0,num_cols):
                if pd.isna(array_2d[a][i]) != True:
                    marks.append(re.sub(r'\D', '', array_2d[a][i]) if any(char.isdigit() for char in array_2d[a][i]) else "absent")
            
            for i in range(0,len(marks)):
                d[-1][arr[i]]=marks[i]
            arr=[]
            # print(array_2d[a])
        # print(array_2d[a])
        # print()
    # # print(d)
    def calculate_cgpa(data):
        total_subject=len(data["Subjects"])
        total_credits = 0
        for a in data["Subjects"]:
            total_credits+=int(a[a.find("(")+1])
        total_grade_points=0
        for a in data["Subjects"]:
            grade_points=0
            marks=data[a]
            if marks=="absent":
                continue
            marks=int(marks)
            if marks >= 90:
                grade_points = 10
            elif marks >= 75:
                grade_points = 9
            elif marks >= 65:
                grade_points = 8
            elif marks >= 55:
                grade_points = 7
            elif marks >= 50:
                grade_points = 6
            elif marks >= 45:
                grade_points = 5
            elif marks >= 40:
                grade_points = 4
            else:
                grade_points = 0
            total_grade_points +=int(a[a.find("(")+1])*grade_points
        return (total_grade_points/total_credits)
        
            
    for a in d:
        a["CGPA"]=calculate_cgpa(a)
    def sort_by_cgpa(data):
        sorted_data = sorted(data, key=lambda x: x['CGPA'], reverse=True)
        return sorted_data

    sorted_data = sort_by_cgpa(d)
    for a in sorted_data:
        print(a)