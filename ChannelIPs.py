import os
import time
import _pickle as pickle
from itertools import islice
import numpy as np
import matplotlib.pyplot as plt


def dataMiner(directory, pathfile):
    name = "channelsUniqueIPs." + pathfile
    file1existence = os.path.isfile(directory + "/" + name)
    name = name = "channelsUniqueIPsAmount." + pathfile
    file2existence = os.path.isfile(directory + "/" + name)
    if file1existence and file2existence:
        print("files already exists")
        return
    t0 = time.time()
    channelsUniqueIPs = {}
    channelsUniqueIPsAmount = {}
    for i in range(505):
        channelsUniqueIPs[i] = set()

    f = open(pathfile, "rb")
    # Special variable to count how many lines in the pathfile
    for line in islice(f, 1, None):
        lineList = str(line).split(',')
        channel = int(lineList[4])
        ip = int(str(lineList[0])[2:])
        channelsUniqueIPs[channel].add(ip)
    f.close()
    print("Time: ", np.around((time.time() - t0) / 60, 2))

    for key in list(channelsUniqueIPs):
        if len(channelsUniqueIPs[key]) == 0:
            del channelsUniqueIPs[key]
        else:
            channelsUniqueIPs[key] = sorted(channelsUniqueIPs[key])
            channelsUniqueIPsAmount[key] = len(channelsUniqueIPs[key])
            print("[", key, "] =  ", channelsUniqueIPsAmount[key])

    print("Not empty from the dictionary", len(channelsUniqueIPs))
    # region save
    name = "channelsUniqueIPs." + pathfile
    f = open(directory + "/" + name, "wb")
    pickle.dump(channelsUniqueIPs, f)
    f.close()
    del channelsUniqueIPs
    print("channelsUniqueIPs saved as ", name, " in ", directory)

    name = "channelsUniqueIPsAmount." + pathfile
    f = open(directory + "/" + name, "wb")
    pickle.dump(channelsUniqueIPsAmount, f)
    f.close()
    del channelsUniqueIPsAmount
    print("channelsUniqueIPsAmount saved as ", name, " in ", directory)
    # endregion


def stats(x, y):
    plt.hist(y)
    plt.title("Distribution of amount of channels within amount of IP")
    plt.ylabel("Amount of channels")
    plt.xlabel("Amount of IPs per channel")
    plt.savefig("ChannelsIPs/histogram.jpg")


def main():
    myDirectory = "ChannelsIPs/"
    dataMiner(directory=myDirectory, pathfile="train.txt")

    f = open("ChannelsIPs/channelsUniqueIPsAmount.train.txt", "rb")
    channelsUniqueIPsAmount = pickle.load(f)
    f.close()
    x = []
    y = []
    for channel in channelsUniqueIPsAmount:
        x.append(channel)
        y.append(channelsUniqueIPsAmount[channel])
        # print("For channel ", channel, " there are ", channelsUniqueIPsAmount[channel], " unique ip")
    stats(x, y)




main()
