#I skipped lec. 248, 249, and 250 because I am confident 100 percent with those topics already, although I was confident with prior topics too, those are long videos, so I prefer to skip them
import numpy as np
import random

def poissonCounter(lam):
    counter,currval = 0,1
    target = np.exp(-lam)

    while currval > target:
        counter += 1
        currval *= np.random.rand()

    return counter


def errorCheck(num1, num2):
    if not isinstance(num1,(int, float)) or not isinstance(num2,(int, float)):
        if isinstance(num1,str):
            if(num1.isnumeric()):
                num1 = float(num1)
                print("x converted to float")
        else:   
            raise Exception("Input x must be a number!")
    

    return num1 * num2

def errorCheck2(x, y):
    z = 0 
    try:
        z = x**y
        print("I succeeded")
    except:
        print("I failed.")
    
    return z


if __name__ == "__main__":
    #enumerate and zip

    ns = np.linspace(-5,5,7)
    for i in range(len(ns)):
        print(f'Index {i} has a value of {ns[i]}')

    for i,n in enumerate(ns):
        print(f'Index {i:.2f} has a value {n:.2f}')

    text = "Hello I am Frank"
    thevowels = ['a', 'e', 'i', 'o', 'u']
    vowels = np.zeros(len(text))

    for i,n in enumerate(text):
        if(n.lower() in thevowels):
           vowels[i] = 1
           
    print(vowels)
    listA = [3,4,5,6,3,-17]
    listB = ['q','w','e','r','t','y']

    for i in range(len(listA)):
        print(str(listA[i]) + ' ' + listB[i])

    #or you can do

    for a,b in zip(listA, listB):
        print(str(a) + ' ' + b)


    # exercise: given the following list, create a dictionary using zip
    names = ['alpha', 'beta', 'gamma']
    values = [10,20,30]
    D = dict(zip(names, values))
    
    #Skipped continue

    #Single line loops
        
    randNum = random.randint(1,10)


    print("r is large") if randNum > 5 else print("r is small")

    #These two do the same thing
    for i in range(10):
        print(i**2)

    squaredList = [i**2 for i in range(5,10)]
    print(squaredList)

    #Exercise : convert the following loops into single-line loops
    text = ["Promising", "Yves", "that", "home", "on", "Nobb"]

    for word in text:
        print(word[0])

    newlist = [' ']*10
    for i in range(10):
        if i % 2 == 1:
            newlist[i] = "Odd"
        else:
            newlist[i] = i
    print(newlist)

    #Converted to

    [print(word[0]) for word in text]

    newList = ["Odd" if i % 2 == 1 else i for i in range(10)]
    print(newList)

    # while loops

    toggle = True

    i= 0

    while toggle:
        print(i)
        i += 1

        if i == 8:
            toggle = False

    print(poissonCounter(10))


    # Broadcasting in numpy

    X = np.array([ [1, 2, 3], 
                  [2, 3, 4], 
                  [3, 4, 5], 
                  [4 , 5, 6] ])
    w = np.array([10, 20, 30])

    print(X), print(' '), print(w)
    Y = np.zeros(X.shape)

    for i in range(X.shape[0]):
        Y[i,:] = X[i,:] + w

    print(' '), print(Y)

    #Broadcasting

    Z = X + w

    print(' '), print(Z), print(' '), print(Y)

    v = np.array([-1, 0, 1, 0], ndmin = 2).T

    print(' '), print(X * v)

    #Exercise: 
    # 1) create a vector of integers 0:8 (v)
    # 2) reshape v into a 3x3 matrix (M) (np.reshape)
    # 3) repeat M into a 9x3 (C) (np.tile)
    # 4) broadcast-multiple C with v (B)

    v = np.array(range(9))
    M = v.reshape(3,3)
    print(M)
    C = np.tile(M,(3,1))
    B = C * np.reshape(v, (len(v), 1))
    print(B)

    #Function error checking and handling

    print(errorCheck("2", 2.4))

    print(errorCheck2("2",3))

