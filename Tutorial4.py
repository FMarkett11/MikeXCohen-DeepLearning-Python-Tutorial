import matplotlib.pyplot as plt
import string
import numpy as np
import pandas as pd
import seaborn as sns
from imageio import imread


if __name__ == "__main__":

    #string formatting
    num = 11.7
    sng = 'cellar doors'

    print(f"I would like to have {num:.2f} {sng}")
    print("I would like to have %.2f %s" %(num, sng))
    # These will both print the same thing

    letters = string.ascii_lowercase

    for i in range(len(letters)):
        if i == 0 or i == 20:
            ordin = "st"
        elif i == 1 or i == 21:
            ordin = "nd"
        elif i == 2 or i == 22:
            ordin = "rd"
        else:
            ordin = "th"

        print(f"{letters[i]} is the {i+1}{ordin} letter of the alphabet")

    #plotting dots and lines

    plt.plot(3,4, 'rp')
    plt.plot(2,4.2,"bo")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Simple Plot")
    plt.legend(["blue", "red"])
    plt.show()

    x = [0,1,3]
    y = [0,2,-1]

    plt.plot(x,y,'ms--')
    plt.show()

    x = np.linspace(0,3*np.pi,101)
    y = np.sin(x)
    plt.plot(x,y)
    plt.show()

    #Exercise: draw your favorite letter "F" is mine :)

    x = [0, 0, 1.5, 0, 0, 1.5]
    y = [0, 3, 3, 3, 1.5, 1.5]

    plt.plot(x,y, 'r')
    plt.show()

    #Part 2

    plt.subplot(2,2,1)
    plt.plot(np.random.randn(10))

    plt.subplot(2,2,4)
    plt.plot(np.random.randn(10))

    plt.show()

    fig, axs = plt.subplots(1,2, figsize = (10,4))

    x = np.arange(10)

    axs[0].plot(x, x**2, 'b')
    axs[1].plot(x,np.sqrt(x), 'r')

    plt.show()

    fig,axs = plt.subplots(2,2)
    
    axs[0,0].plot(np.random.randn(4,4))
    axs[0,1].plot(np.random.randn(4,4))
    axs[1,0].plot(np.random.randn(4,4))
    axs[1,1].plot(np.random.randn(4,4))

    plt.tight_layout()
    plt.show()

    # Exercise : Create a 3x3 subplot geometry in a for loop

    fig,axs = plt.subplots(3,3)
    j = -1

    #My way

    for i in range(9):
        if i % 3 == 0:
            j += 1
        axs[i % 3, j % 3].plot(np.random.randn(4,4))

    
    plt.tight_layout()
    plt.show()   

    #Mike's way

    M = np.random.randint(10, size = (4,4))

    M = M.flatten()
    fig,ax = plt.subplots(3,3,figsize=(7,7))

    for i in ax.flatten():
        i.plot(np.random.randn(3,9))

    plt.show()




    plt.tight_layout()
    plt.show()    

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
    
    fig, ax = plt.subplots(2,3, figsize=(15,7))
    
    ax[0,2].plot(x,x,label = "y = x")
    ax[1,2].plot(x,x**2,label = "y = x**2")
    ax[0,1].plot(x,x**3,label = "y = x**3")

    ax[0,2].legend()
    ax[0,1].set_xlabel('x')
    ax[1,2].set_ylabel('y = f(x)')
    ax[0,1].set_title("big plot")

    ax[0,2].set_xlim([x[0],x[-1]])
    ax[0,2].set_ylim([-10,10])

    fig.gca().set_aspect(.3)
    
    plt.tight_layout()
    plt.show()
    
    #Exercise : Replicate Mike's plot
    
    x = np.linspace(0,10,100)
    
    for i in np.linspace(0, 1, 50):
        plt.plot(x, x ** i, color=[i/2, 0 , i])
    
    plt.xlim(0, 10)
    plt.ylim([0,10])
    plt.show()
    
    #Seaborn
    
    n = 200
    D = np.zeros((n,2))
    
    D[:,0] = np.linspace(0, 10, n) + np.random.randn(n)
    D[:,1] = D[:,0]**2 + np.random.rand(n)*10
    
    sns.jointplot(x = D[:,0],y = D[:,1])
    plt.plot(D[:,0], D[:,1], 'o')
    
    plt.show()
    
    df = pd.DataFrame(data = D, columns=["var1", "var2"])
    print(df)
    sns.jointplot(x = df.columns[0],y = df.columns[1], data = df, kind = 'kde', color = 'purple')
    plt.show()
    
    x = np.linspace(-1, 1, n)
    y1 = x**2
    y2 = np.sin(3 * x)
    y3 = np.exp(-10*x**2)
    
    sns.scatterplot(x = y1, y = y2, hue=y3, legend = False, palette='tab10')
    plt.show()
    
    
    #Exercise: create a regression plot of data in matrix D -> df
    
    sns.regplot(x = df.columns[0], y = df.columns[1], data = df, color = 'red')
    plt.title(f'Regression of {df.columns[0]} on {df.columns[1]}')
    plt.show()
    
    #Images
    
    m = 3
    n = 5
    
    M = np.random.randint(10, size = (m,n))
    print(M)
    
    # plt.plot(M)
    plt.imshow(M)
    
    
    # plt.text(0, 1, 'hi')
    
    for i in range(m):
        for j in range(n):
            plt.text(j,i,M[i,j], fontsize = 20, horizontalalignment = 'center', verticalalignment = 'center')
    
    
    img = imread('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/%EB%8B%A5%EC%8A%A4%ED%9B%88%ED%8A%B8%28%EB%8B%A8%EB%AA%A8%EC%A2%85%29_%28Dachshund_%28Short%29%29.jpg/250px-%EB%8B%A5%EC%8A%A4%ED%9B%88%ED%8A%B8%28%EB%8B%A8%EB%AA%A8%EC%A2%85%29_%28Dachshund_%28Short%29%29.jpg')
    
    plt.imshow(img)
    plt.title('lil puppy')
    
    plt.hist(img.flatten(), bins = 100)
    plt.imshow(img, cmap = 'gray', vmin = 50, vmax = 200)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.show()
    
    # Exercise: Visualize the hilbert matrix using seaborn (heatmap)
    # H is 10x10
    
    H = np.zeros((10,10))
    for i in range(1, 11):
        for j in range(1, 11):
            H[i - 1, j - 1] = (1 / ((i + j) - 1))
            
    sns.heatmap(H, vmax = .4)
    plt.show()
    
    #Export plots in low and high resolution
    
    x = np.linspace(.5, 5, 10)
    y1 = np.log(x)
    y2 = 2 - np.sqrt(x)
    
    plt.plot(x, y1, 'bo-', label = 'log')
    plt.plot(x, y2, 'rs-', label = 'sqrt')
    
    plt.legend()
    
    plt.show()
    
    #Did not code here, because the rest was jupyter notebook exclusive.
    