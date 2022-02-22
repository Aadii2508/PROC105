import csv 
import math

file=open("data.csv")
data=csv.reader(file)
file_data=list(data)

dataList=[] 
for i in range(len(file_data)): 
    marks=file_data[i]
    dataList.append(marks)

print(dataList) 
n=len(dataList) 
total=0 

for j in dataList: 
    total=total+ j
    
mean=total/n 

print("Mean is : "+str(mean)) 

squreList= []
for p in dataList:
    number = mean- p
    square = number**2
    squreList.append(square)

sumsq = 0

for q in squreList:
    sumsq = sumsq+ q

resultsq = sumsq/n
standarddev = math.sqrt(resultsq)

print(standarddev)

