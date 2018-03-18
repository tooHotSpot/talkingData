import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import _pickle as pickle
import psutil
from itertools import islice
import time


def mainDrawer(values):
    # values = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    labels = np.linspace(0, 1, 11)
    bin_positions = list(range(len(values)))
    bins_art = plt.bar(bin_positions, values)
    plt.xticks(bin_positions, labels)
    y = []
    x = []
    for i in range(len(bins_art)):
        rect = bins_art[i]
        height = rect.get_height()
        y.append(height)
        x.append(rect.get_x() + rect.get_width() / 2.)
        plt.text(x[i], 1.01 * y[i], '%d' % int(height), ha="center", va="bottom", )
    plt.plot(x, y, 'r--')
    plt.title("Distribution")
    plt.ylabel("Amount of banner networks with according conversion")
    plt.xlabel("Conversion")
    fig = plt.gcf()

    fig.set_size_inches(9, 6, forward=True)
    plt.savefig("myfig.jpg")


def mainKaggle():
    process = psutil.Process(os.getpid())
    t0 = time.time()
    # ip, app, device, os, channel, click_time, attributed_time, is_attributed
    f = open("train_sample.txt", "rb")
    myDict = {}
    print("********************************************************")
    t1 = time.time()
    print("Process label: before reading")
    count = 0
    for line in islice(f, 1, None):
        count += 1
        lineList = str(line).split(',')
        is_attributed = int(lineList[-1][0])
        channel = int(lineList[4])
        if channel in myDict:
            myDict[channel][0] += 1
            myDict[channel][1] += is_attributed
        else:
            myDict[channel] = [1, is_attributed]
    f.close()
    print("Reading ended, ", count, " lines are read")
    print(len(myDict))
    print("Time wasted: ", str(time.time() - t1)[:5], ";", " totally:", str(time.time() - t0)[:5], ";",
          str(process.memory_info().rss / 1024 / 1024)[:2], " MB Used")
    t1 = time.time()
    print("********************************************************")
    print("Process label: before counting conversion ")

    valueslist = {}
    labels = np.linspace(0, 1, 11) * 10
    for label in labels:
        valueslist[int(label)] = 0

    maxc = 0
    for c in myDict:
        if c > maxc:
            maxc = c
        myBin = np.int(np.round(myDict[c][1] / myDict[c][0], 1) * 10)
        valueslist[myBin] = valueslist[myBin] + 1

    print("Important information: maximum channel number is", maxc)
    print("Counting conversion ended")
    print("Time wasted: ", str(time.time() - t1)[:5], ";", " totally:", str(time.time() - t0)[:5], ";",
          str(process.memory_info().rss / 1024 / 1024)[:2], " MB Used")
    t1 = time.time()
    print("********************************************************")
    print("Process label: before histogram creation")
    myList = []
    for v in valueslist:
        myList.append(valueslist[v])  # In bin with value v valueslist[v] networks
    mainDrawer(myList)
    print("Histogram created")
    print("Time wasted: ", str(time.time() - t1)[:5], ";", " totally:", str(time.time() - t0)[:5], ";",
          str(process.memory_info().rss / 1024 / 1024)[:2], " MB Used")
    t1 = time.time()
    print("Process label: end of the program")


mainKaggle()
