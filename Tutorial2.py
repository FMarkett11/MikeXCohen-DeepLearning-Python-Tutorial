#MikeXCohen's section 29 https://www.udemy.com/course/deeplearning_x/learn/lecture/27855900?start=0#overview
import numpy as np
import pandas as pd
import copy

def myFunct(num1, num2):
    prod = num1*num2
    sum = num1+num2
    return prod,sum

def myFactorial(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * myFactorial(num - 1)

def mikeFactorial(num):
    return np.prod(np.arange(1, num+1))

class model(object):

    #constructor method
    def __init__(self, numlayers, numunits, name):
        self.layers = numlayers
        self.units = numunits
        self.name = name
        self.weights = 1

    def howManyUnits(self):
        totalUnits = self.layers * self.units
        print(f'There are {totalUnits} units in the model.')

    def trainTheModel(self,x):
        self.weights += x
        return self.weights
    
    def __str__(self):
        return f'This is a {self.name} architecture.'
    
# 1) Weights should be a random numbers matrix of size layers X units
# 2) Change the training method to multiply input X and add input Y
    
class exercise(model):
    def __init__(self, numlayers, numunits, name):
        self.layers = numlayers
        self.units = numunits
        self.name = name
        self.weights = np.random.randn(numlayers, self.units)
    def trainTheModel(self,x,y):
        self.weights = self.weights * x + y
        return self.weights


if __name__ == "__main__":
    var = [10,20,30,40,50.5]
    output = sum(var)
    print("The sum is " + str(output))
    mean = sum(var)/len(var)
    print(mean)

    #importing libraries (numpy)

    numbers = [1,2,3,4,5]
    print(np.mean(numbers))
    x = np.linspace(1,7,5)
    print(x)
    print(type(x))
    numbers_np = np.array(numbers)
    print(numbers_np)

    #importing libraries (pandas)
    
    #create random data

    randnums = np.random.randn(100) *5 + 20
    randnums2 = np.random.randn(100) > 0

    labels = ["temp" , "ice cream"]

    D = {labels[0]:randnums, labels[1]:randnums2}

    # #import dict to pandas dataframe

    df = pd.DataFrame(data = D)
    print(type(df))
    print(df)
    header = df.head()
    count = df.count()
    mean = df.mean()
    print(header)
    print(mean)

    #Create a pandas dataframe with integers from 0,10, their square and their log

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myDict = {}
    for i in range(10):
        myDict[nums[i]] = {"square":nums[i]**2, "log":np.log(nums[i])}
    df = pd.DataFrame(data = myDict)
    print(df)
        
    #creating functions

    num1 = 2
    num2 = 50
    prod,sum = myFunct(num1,num2)
    print(prod)

    functTest = lambda x : x**2 - 1
    print(functTest(4))

    #create a function that computes a factorial

    print(myFactorial(10))
    print(mikeFactorial(10))

    #copies of variables

    a = [4,3]

    b = a
    b[0] = 5 #creates a new pointer, not a new value
    print(a)
    print(b)
    #same ids
    print(id(a))
    print(id(b))

    b = a[:]
    b[0] = 4
    print(a)
    print(b)
    print(id(a))
    print(id(b))

    a = {'q':1, 'w':2}
    b = copy.deepcopy(a)
    print(id(a))
    print(id(b))

    #OBJECT ORIENTED PROGRAMMING (classes) OOP
    #Class is a blueprint for creating a set of attributes and methods
    #instance  ("a class is a cookie cutter, an instrance is an individual cookie")

    m1 = model(12, 5, 'CNN')
    #m1.howManyUnits()

    print(m1.trainTheModel(2.5))
    print(m1.trainTheModel(2.5))
    print(m1.trainTheModel(2.5))
    print(m1.trainTheModel(2.5))

    print(str(m1))

    m2= exercise(12, 5, "ICNN")

    print(m2)
    print(m2.trainTheModel(2.5, 4))
    print('\n')
    print(m2.trainTheModel(2.5, 4))
    print('\n')
    print(m2.trainTheModel(2.5, 4))
    print('\n')
    print(m2.weights)

    #Create a new class 
    # 1) Weights should be a random numbers matrix of size layers X units
    # 2) Change the training method to multiply input X and add input Y
