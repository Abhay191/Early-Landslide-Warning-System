# Name - Abhay Gupta
# Registration number - B20075
# Mobile - 9511334630


import pandas as pd
import matplotlib.pyplot as plt
import math

# Question 1
# import file
print("Question 1")
dmiss = pd.read_csv('landslide_data3_miss.csv',sep = ',')
x = []
y = []
for i in dmiss.columns:
    x.append(i)
    y.append(dmiss[i].isnull().sum())

# plotting the bar graph
plt.figure()
plt.bar(x,y)
plt.xlabel('Attribute names')
plt.ylabel('Number of missing values')
plt.xticks(rotation=60) 


# Question 2
print("Question 2")
# (a) part
print("Total number of tuples in starting: ",dmiss.shape[0])
print("Total number of tuples deleted in question 2(a) = ",dmiss['stationid'].isnull().sum())

# droping the NaN values
dmiss = dmiss.dropna(axis = 0,subset = ['stationid'])

# (b) part
n1 = dmiss.shape[0]
dmiss = dmiss.dropna(thresh=6)
n2 = dmiss.shape[0]
print("Total number of tuples deleted in question 2(b) = ", n1-n2)


# Question 3
print("Question 3")
b = []
# making an array containing the number of missing values of each attribute
for i in dmiss.columns:
    b.append(dmiss[i].isnull().sum())
print("Total number of tuples left: ",dmiss.shape[0])
print(dmiss.isnull().sum())
print("Percentage of missing values for each attribute:")
print((dmiss.isnull().sum())*100/896)
print("Total nuber of missing values in the file:",sum(b))


# Question 4
print("Question 4")
# (a) part
# (i) part

# importing the original file
d_orig = pd.read_csv('landslide_data3_original.csv',sep = ',')

# printing the properties of  original dataframe
print("Properties of orginal data: ")
print("Mean: ")
print(d_orig.mean())
print()
print("Median: ")
print(d_orig.median())
print()
print("Mode: ")
print(d_orig.mode().iloc[0])
print()
print("Standard deviation: ")
print(d_orig.std())
print()


# filling the missing values by mean
means = dmiss.mean()
d_miss1 = dmiss.fillna(value = means)

# printing the properties of  processed dataframe
print('Properties of data after processing:')
print("Mean: ")
print(d_miss1.mean())
print()
print("Median: ")
print(d_miss1.median())
print()
print("Mode: ")
print(d_miss1.mode().iloc[0])
print()
print("Standard deviation: ")
print(d_miss1.std())
print()



# (ii) part
# making an RMSE function
def rmse(a,b):
    new_dic={}   
    for columns in a.columns:
        if columns!='dates' and columns!='stationid':
            N=b.isnull().sum()[columns]
            mean_square=(((a[columns]-d_orig.loc[a.index,columns])**2).sum())/N    
            root_mean_square=math.sqrt(mean_square)
            new_dic[columns]=root_mean_square
    print(pd.Series(new_dic)) 
    plt.figure()
    plt.bar(new_dic.keys(),new_dic.values())
    plt.yscale("log")
    plt.xlabel('Attribute name')
    plt.ylabel('RMSE')
    plt.xticks(rotation=60) 
    plt.show()

print("RMSE:")
rmse(d_miss1,dmiss)


# (b) part
# (i) part

# filling the missing values by interpolation
d_miss2=dmiss.interpolate()

# printing the properties of processed dataframe
print("Mean: ")
print(d_miss2.mean())
print()
print("Median: ")
print(d_miss2.median())
print()
print("Mode: ")
print(d_miss2.mode().iloc[0])
print()
print("Standard deviation: ")
print(d_miss2.std())
print()


# (ii) part
print("RMSE:")
rmse(d_miss2,dmiss)


# Question 5
print("Question 5")
# (a) part

# making an function for calculating outlier
def outlier(df,a,c):       
    b=[]
    IQR=(df[a].quantile(0.75)-df[a].quantile(0.25))
    for i in df[a]:              
        if (i>df[a].quantile(0.75)+1.5*IQR or i<df[a].quantile(0.25)-1.5*IQR):
            b.append(i)
    print("IQR: ",IQR)
    print("Variance: ",df[a].var())
    print(len(b))
    print(b)  
    
    plt.figure()
    plt.boxplot(df[a])
    plt.title(c)
    plt.show()
    
# calculating outliers of the data 
outlier(d_miss2,'temperature','Boxplot of temperature')         
outlier(d_miss2,'rain','Boxplot of rain')


list=['temperature','rain']
for i in list:
    Q1=d_miss2[i].quantile(0.25)      
    Q3=d_miss2[i].quantile(0.75)
    IQR=Q3-Q1
    d_miss2.loc[(d_miss2[i]>Q3+1.5*IQR) | (d_miss2[i]<Q1-1.5*IQR),i]=d_miss2[i].median()    


outlier(d_miss2,'temperature','Boxplot of attribute temperature after replacing outliers with median')         
outlier(d_miss2,'rain','Boxplot of attribute rain after replacing outliers with median')












