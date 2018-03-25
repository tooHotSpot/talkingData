import numpy as np
import os
import glob
import math
import matplotlib.pyplot as plt
import _pickle as pickle
import psutil
from itertools import islice
import time


def mainDrawer(name, labels, values, rightedge):
    bin_positions = list(range(len(values)))
    bins_art = plt.bar(bin_positions, values)
    print("max ",max(bin_positions), " min = ", min(bin_positions))
    plt.xticks(bin_positions, labels, rotation=90)
    y = []
    x = []
    for i in range(len(bins_art)):
        rect = bins_art[i]
        height = rect.get_height()
        y.append(height)
        x.append(rect.get_x() + rect.get_width() / 2.)
        text = '%d' % int(height)
        if text == '0':
            text = ""
        plt.text(x[i], 1.01 * y[i], text, ha="center", va="bottom", )
    plt.plot(x, y, 'r-')
    plt.ylabel("Amount of banner networks with according conversion")
    plt.xlabel("Conversion")
    fig = plt.gcf()
    plt.xlim(-1, 101)
    fig.set_size_inches(18, 6, forward=True)
    k = name + " in [0; " + str(rightedge) + "]"
    plt.title(k)
    plt.tight_layout(pad=0.3)
    plt.savefig("distributiondiagrams/" + k + ".jpg")
    plt.clf()
    # plt.show()


def mainKaggle(myDecimals, rightedge, precision, path):
    t0 = time.time()
    f = open(path, "rb")
    myDict = pickle.load(f)
    f.close()

    valueslist = {}
    labels = np.linspace(0, rightedge, 101)

    for label in labels:
        valueslist[str(label)] = 0
    #print(valueslist)
    # Counting the conversion with given precision
    for channel in myDict:
        if myDict[channel][1] == 0:
            myBin = 0.0
        else:
            f = myDict[channel][1] / myDict[channel][0]
            g = np.around(f, decimals=myDecimals)
            myBin = np.around(f, decimals=myDecimals)
            #print("!: ", f, " ", g, " ", myBin, end=" / ")
            if myBin < labels[1] or myBin == 0:
                myBin = labels[1]
            #print("finally myBin = ", myBin)
        if myBin > rightedge:
            continue
        valueslist[str(myBin)] += 1

    #print(valueslist)
    # region Statistics
    print("Counting conversion ended")
    print("Time: ", np.around(((time.time() - t0)/60), 2))
    print("Process label: before histogram creation")
    # endregion
    myList = []
    for v in valueslist:
        myList.append(valueslist[v])  # In bin with value v valueslist[v] networks

    mainDrawer(str(path).split('.')[-2], labels, myList, rightedge)
    # region Statistics
    print("Histogram created")
    print("Time: ", np.around(((time.time() - t0) / 60), 2))
    print("Process label: end of the program")
    # endregion



def main():
    psample = "myPickler/channelsDict.train_sample.txt"
    ptrain = "myPickler/channelsDict.train.txt"
    mainKaggle(myDecimals=2, rightedge=1, precision=0.1, path=psample)
    mainKaggle(myDecimals=2, rightedge=1, precision=0.1, path=ptrain)
    mainKaggle(myDecimals=3, rightedge=0.1, precision=0.01, path=psample)
    mainKaggle(myDecimals=3, rightedge=0.1, precision=0.01, path=ptrain)
    mainKaggle(myDecimals=4, rightedge=0.01, precision=0.001, path=psample)
    mainKaggle(myDecimals=4, rightedge=0.01, precision=0.001, path=ptrain)
    mainKaggle(myDecimals=5, rightedge=0.001, precision=0.0001, path=psample)
    mainKaggle(myDecimals=5, rightedge=0.001, precision=0.0001, path=ptrain)


main()