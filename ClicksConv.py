import os
import time
import _pickle as pickle
import matplotlib.pyplot as plt
from itertools import islice
import numpy as np


def myClicksConv(directory, pathfile):
    x = []
    y = []
    f = open(pathfile, "rb")
    myDict = pickle.load(f)
    f.close()
    for channel in myDict:
        x.append(myDict[channel][0])
        f = myDict[channel][1] / myDict[channel][0]
        conversion = np.around(f, decimals=5)
        y.append(conversion)
    plt.plot(x, y, 'r.')
    plt.xlabel("Clicks")
    plt.ylabel("Conversion")
    name = str(pathfile).split('.')[-2]
    plt.title("ClicksConv_" + name + ".png")
    #
    plt.xlim(-1000, 100000)
    print(-np.average(x) / 10)
    fig = plt.gcf()
    fig.set_size_inches(18, 6, forward=True)
    plt.savefig(directory + "ClicksConv_" + name + ".png")


def main():
    myDirectory = "ClicksConv/"
    ptrain = "myPickler/channelsDict.train.txt"
    myClicksConv(directory=myDirectory, pathfile=ptrain)


main()
