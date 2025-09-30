import math as math

if __name__ == "__main__":
    # Basic input and print

    A = int(input("Input a number: "))
    B = int(input("Input a number: "))
    C = math.sqrt(A**2 + B**2)
    print(f"Side C = {int(C)}")

    # lists
    aList = [4,5,6,2,0,3]
    strList = ['hi','my','name','is','Frank']
    mixedList = [8,4.0,'Frank',True]
    listList = [1, 2, 3, 'hi', 'bye', [.5, 1/4, 'i'], 5, 6 ,3]

    print(listList)
    listList.append(952)
    print(listList)
    aList.sort()
    print(aList)
    print(aList.count(-100))
    aList.insert(2,9)
    aList.remove(6)
    aList.sort(reverse=True)
    print(aList)

    # tuples

    atuple = (3, "hello", 3.4)
    aList = [3, "hello", 3.4]

    #List is mutable, tuple is immutable, so we cannot change tuple values but we can change list values

    aList[0] = 13 #Cannot do this with tuple
    print(aList)
    print(type(atuple))

    # Booleans

    t = True
    f = False

    true = 4 == 4.0
    print(f"{true} xOr {t} is {f}")

    a = int(input())
    b = int(input())
    c = int(input())

    pythagTriple = False
    if((a**2 + b**2) == c**2):
        pythagTriple = True
    print(pythagTriple)

    # dictionary: key/value pairs

    D = dict()
    print(D) #uses curlybrackets{}
    D['name'] = "Frank"
    print(D) #{'name': 'Frank'}
    D["ageRange"] = [19,20]
    print(D)
    E = {'Name': "frank", "favoriteFootballTeam": "Falcons"}
    print(E)
    print(E["favoriteFootballTeam"])
    print(E.keys()) #dict_keys(['Name', 'favoriteFootballTeam'])
    print("Name" in E) #True
    print(E.items()) #dict_items([('Name', 'frank'), ('favoriteFootballTeam', 'Falcons')])

    a = int(input())
    b = int(input())

    dict = {"firstNum": a, "secondNum": b, "product": a * b}
    print(dict)