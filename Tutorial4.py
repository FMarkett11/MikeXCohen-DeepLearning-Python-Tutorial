import matplotlib.pyplot as plt
import string
import numpy as np

if __name__ == "__main__":

    # #string formatting
    # num = 11.7
    # sng = 'cellar doors'

    # print(f"I would like to have {num:.2f} {sng}")
    # print("I would like to have %.2f %s" %(num, sng))
    # # These will both print the same thing

    # letters = string.ascii_lowercase

    # for i in range(len(letters)):
    #     if i == 0 or i == 20:
    #         ordin = "st"
    #     elif i == 1 or i == 21:
    #         ordin = "nd"
    #     elif i == 2 or i == 22:
    #         ordin = "rd"
    #     else:
    #         ordin = "th"

    #     print(f"{letters[i]} is the {i+1}{ordin} letter of the alphabet")

    # #plotting dots and lines

    # plt.plot(3,4, 'rp')
    # plt.plot(2,4.2,"bo")
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.title("Simple Plot")
    # plt.legend(["blue", "red"])
    # plt.show()

    # x = [0,1,3]
    # y = [0,2,-1]

    # plt.plot(x,y,'ms--')
    # plt.show()

    # x = np.linspace(0,3*np.pi,101)
    # y = np.sin(x)
    # plt.plot(x,y)
    # plt.show()

    # #Exercise: draw your favorite letter "F" is mine :)

    # x = [0, 0, 1.5, 0, 0, 1.5]
    # y = [0, 3, 3, 3, 1.5, 1.5]

    # plt.plot(x,y, 'r')
    # plt.show()

    # #Part 2

    # plt.subplot(2,2,1)
    # plt.plot(np.random.randn(10))

    # plt.subplot(2,2,4)
    # plt.plot(np.random.randn(10))

    # plt.show()

    # fig, axs = plt.subplots(1,2, figsize = (10,4))

    # x = np.arange(10)

    # axs[0].plot(x, x**2, 'b')
    # axs[1].plot(x,np.sqrt(x), 'r')

    # plt.show()

    # fig,axs = plt.subplots(2,2)
    
    # axs[0,0].plot(np.random.randn(4,4))
    # axs[0,1].plot(np.random.randn(4,4))
    # axs[1,0].plot(np.random.randn(4,4))
    # axs[1,1].plot(np.random.randn(4,4))

    # plt.tight_layout()
    # plt.show()

    #Exercise : Create a 3x3 subplot geometry in a for loop

    # fig,axs = plt.subplots(3,3)
    # j = -1

    # #My way

    # for i in range(9):
    #     if i % 3 == 0:
    #         j += 1
    #     axs[i % 3, j % 3].plot(np.random.randn(4,4))

    
    # plt.tight_layout()
    # plt.show()   

    # #Mike's way

    # M = np.random.randint(10, size = (4,4))

    # M = M.flatten()
    # fig,ax = plt.subplots(3,3,figsize=(7,7))

    # for i in ax.flatten():
    #     i.plot(np.random.randn(3,9))

    # plt.show()




    # plt.tight_layout()
    # plt.show()    

    # How to make plots look better

    x = np.linspace(-3,3,101)

    plt.plot(x,x,label = "y = x")
    plt.plot(x,x**2,label = "y = x**2")
    plt.plot(x,x**3,label = "y = x**3")

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y = f(x)')
    plt.title("big plot")

    plt.xlim([x[0],x[-1]])
    plt.ylim([-10,10])

    plt.gca().set_aspect(.3)

    plt.show()



    