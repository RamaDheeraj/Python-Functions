import pandas as pd
import numpy as np
import matplotlib
import collections 
matplotlib.style.use('ggplot')



a=5
if a<4:
    print("{} is less than 4".format(a))
else:
    print("{} is not less than 4".format(a))

a=1
i=0
while i<len(x):
    a=a*x[i]
    i=i+1
print("product of numbers in x is {}".format(a))
    

#identifying prime numbers
i=10
j=20
print("Prime numbers between {} and {}".format(i,j))
for a in range(i,j+1):
    prime=True
    for b in range(2,i):
        if a%b==0:
            prime=False
    if prime:
        print(a)

#using list comprehension
i=10
j=20
print("Prime numbers between {} and {}".format(i,j))        
for num in range(i,j):
    if all(num%i!=0 for i in range(2,num)):
       print (num)
     



#Even numbers
num=1

for num in range(9):
    if num%2==0:
        print (num)
    
#Even Numbers less than that number
a=int(input("Enter number: "))
num=1
while num<a:
    if num%2==0:
        print(num)
    num=num+1

i=list(range(1,10,2))
len(i)

#Running mean function
def runmean(i):
    x=0
    lst=[]
    for a in range(len(i)):
        x=x+i[a]
        lst.append(x/(a+1))
    return lst
runmean(i)


#Timeseries forecasting through Exponential Smoothing
def forecast(i,ph):
    f=[]
    p=0
    for a in range(len(i)):
        if a==0:
            p=i[a]
        else:
            p=round(f[a-1]+(ph*(i[a-1]+f[a-1])),2)
        f.append(p)
    df=pd.concat([pd.DataFrame(i),pd.DataFrame(f)],axis=1)
    df.columns=["Actual",'Forecasted']
    return df
        
    

#Number of primes between two numbers using list comprehensions
def numprimes(int1,int2):
    a=0
    for i in range(int1,int2+1):
        if all(i%b!=0 for b in range(2,i)):
            a=a+1          
    return a
     
numprimes(10,19)

#Number of primes between two numbers 
def numprimes(int1,int2):
    a=0
    for i in range(int1,int2+1):
        prime=True
        for b in range(2,i):
            if i%b==0:
                prime=False
        if prime:
            a=a+1                  
    return a
     
numprimes(10,19)


def primes(int1,int2):
    a=0
    plist=[]
    for i in range(int1,int2+1):
        prime=True
        for b in range(2,i):
            if i%b==0:
                prime=False
        if prime:
            a=a+1
            plist.append(i)                              
    return ("Number of primes {} and List of primes are {}".format(a,plist))
     
primes(10,19)


#Checking sucessive outputs of dice
def dice():
    a=list(range(1,7))
    b=list(np.repeat(1/6,6))
    df=np.random.choice(a,size=2,replace=True,p=b)
    if df[0]==df[1]:
        print("You Win")
    else:
        print('You Lose')
f=dice()
f

#Function to identify missing values, unique values in a data frame
def missingvalue(df):
    ou=pd.DataFrame()
    for i in range(df.shape[1]):
        a=df.columns[i]
        b=df.iloc[:,i].nunique()
        c=df.iloc[:,i].isnull().sum()
        x=pd.DataFrame({"Column Name":[a],"# Unique Values":[b],"# Missing Values":[c]},index=[i])
        ou=pd.concat([ou,x])
    ou=ou[ou.columns[::-1]]
    return ou
missingvalue(df)


#Time taken to complete a task in two different ways 
#first method
t1=list(np.random.uniform(low=5,high=9,size=(10000)))
t2=list(np.random.exponential(10,size=10000))
t3=list(np.random.poisson(lam=4,size=10000))
t4=list(np.random.uniform(low=3,high=10,size=10000))
if (t1>t2):
    
    if (t1>t3):
        a=t1
    else:
        a=t3
else:
    if t2>t3:
        a=t2
    else:
        a=t3
ab=[a[i]+t4[i] for i in range(len(a))]
time=pd.concat([pd.DataFrame(t1),pd.DataFrame(t2),pd.DataFrame(t3),pd.DataFrame(t4)
           ,pd.DataFrame(a),pd.DataFrame(ab)],axis=1)

#Second method
t1=np.random.uniform(low=5,high=9,size=(10000))
t2=np.random.exponential(10,size=10000)
t3=np.random.poisson(lam=4,size=10000)
t4=np.random.uniform(low=3,high=10,size=10000)
t=np.maximum(np.float_(t1),np.float_(t2),np.float_(t3)) +t4
#t=np.fmax(t1,t2,t3)
#len(t[t>15])/len(t)       
time=pd.DataFrame({"t1":np.random.uniform(low=5,high=9,size=(10000)),
                   "t2":np.random.exponential(10,size=(10000)),
                   't3':np.random.poisson(lam=4,size=(10000)),
                   't4':np.random.uniform(low=3,high=10,size=(10000))},
                   index=range(10000))    
time['t']=time.iloc[:,0:2].max(axis=1)+time.t4
p=time.loc[(time.t>15)].shape[0]/time.shape[0]



#top most frequently occuring words
a= ['we', 'are', 'marketing', 'science', 'team', 'we', 'are', 'working', 'ebay']

#using in-built functions
collections.Counter(a)

#without in built function
def frequency(a):
    freq={}
    for i in a:
        try:
            freq[i]=freq[i]+1
        except:
            freq[i]=1
    freq=sorted(freq,key=lambda word: (-freq[word],word))
    return freq
frequency(a)           
        
#second method
d = {}
for word in a:
    d[word] = d.get(word, 0) + 1
ab=[]   
for a,b in freq.items():
    ab.append((a,b))
sorted(ab,key=lambda x: (-x[1],x[0]))

b=[1,3,1,2,4,6,5]  
new=[] 
for i in b:
    m = b[0]
    for s in b:
        if m>s:
            m=s
    new.append(m)
    b.remove(m)


#sorting without using min, max and sort
lst=[1,2,3,5,2,6,3]
n=[]
while lst:
    mn=lst[0]
    for a in lst:
        if mn>a:
            mn=a
    n.append(mn)
    lst.remove(mn)
print(n)

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
            
print (lst)
            
            
     
