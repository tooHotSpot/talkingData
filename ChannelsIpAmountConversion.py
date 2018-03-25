import os
import time
import _pickle as pickle
from itertools import islice
import numpy as np
import matplotlib.pyplot as plt


def main():
    myDirectory = "ChannelsIPs/"

    f = open("ChannelsIPs/channelsUniqueIPsAmount.train.txt", "rb")
    channelsUniqueIPsAmount = pickle.load(f)
    f.close()
    f = open("myPickler/channelsDict.train.txt", "rb")
    myDict = pickle.load(f)
    f.close()

    x = []
    y = []
    for channel in channelsUniqueIPsAmount:
        f = myDict[channel][1] / myDict[channel][0]
        conversion = np.around(f, decimals=5)
        x.append(channelsUniqueIPsAmount[channel])
        y.append(conversion)

    plt.plot(x, y, 'r.')
    plt.xlabel("Unique IP Amount")
    plt.ylabel("Conversion ")
    name = "train.txt"
    plt.title("ChannelsIPAmountConversion." + name + ".png")
    plt.tight_layout(h_pad=0, pad=0.4)
    fig = plt.gcf()
    fig.set_size_inches(10, 10, forward=True)
    plt.grid(True)
    plt.savefig(myDirectory + "ChannelsIPAmountConversion." + name + ".png")


main()
