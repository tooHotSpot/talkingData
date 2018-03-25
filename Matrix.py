import os
import time
import _pickle as pickle
from itertools import islice
import numpy as np
import cv2
import matplotlib.pyplot as plt


def matrixMiner(ordered):
    myMatrixFile = "matchMatrix/matchMatrix.txt"
    if os.path.isfile(myMatrixFile):
        print(myMatrixFile, " already exists")
        f = open(myMatrixFile, "rb")
        m = pickle.load(f)
        f.close()
        return m
    f = open("ChannelsIPs/channelsUniqueIPs.train.txt", "rb")
    cIPs = pickle.load(f)  # cIPs = channelsUniqueIPs
    f.close()
    t0 = time.time()
    matchMatrix = np.zeros([202, 202])
    for i in range(len(ordered)):
        channelX = ordered[i]
        print("comparing", i, "; time: ", np.around((time.time() - t0) / 60, 2))
        amaxIP = cIPs[channelX][-1]
        # print("amaxIP = ", amaxIP)
        a = np.zeros([amaxIP + 1])
        a[cIPs[channelX][:]] = 1
        for j in range(len(ordered)):
            channelY = ordered[j]
            if channelX != channelY:
                # print(channelX, " with ",  len(cIPs[channelX])," IPs comparing with ", channelY, " with ",  len(cIPs[channelY]))
                bmaxIP = cIPs[channelY][-1]
                b = np.zeros([max(amaxIP + 1, bmaxIP + 1)])
                b[cIPs[channelY][:]] = 1
                b = b[:amaxIP + 1]
                # print(len(a), " ", len(b))
                sum = np.dot(a, b.T)
                matchMatrix[i, j] = sum
                matchMatrix[j, i] = sum
                # print(matchMatrix[i, j])
                del b
        del a
    f = open(myMatrixFile, "wb")
    pickle.dump(matchMatrix, f)
    f.close()
    print(matchMatrix, " is created and saved as ", myMatrixFile)
    return matchMatrix


def getOrderedListByConversion():
    myListFile = "Conversion/myConversionList.train.txt"
    if os.path.isfile(myListFile):
        print(myListFile, " already exists")
        f = open(myListFile, "rb")
        l = pickle.load(f)
        f.close()
        return l
    f = open("myPickler/channelsDict.train.txt", "rb")
    myDict = pickle.load(f)
    f.close()
    myConversionList = []
    for channel in myDict:
        if myDict[channel][1] == 0:
            myConversionList.append([0, channel])
        else:
            f = myDict[channel][1] / myDict[channel][0]
            conversion = np.around(f, decimals=5)
            myConversionList.append([np.float(conversion), channel])

    print("**************************")
    # myConversionList = sorted(myConversionList, key=lambda x: x[0])
    # sorted will sort by the first value anyway
    myConversionList = sorted(myConversionList)
    onlyChannels = []
    for row in myConversionList:
        onlyChannels.append(row[1])
    f = open(myListFile, "wb")
    pickle.dump(onlyChannels, f)
    f.close()
    return onlyChannels


def main():
    myDirectory = "Conversion/"
    ordered = getOrderedListByConversion()
    m = matrixMiner(ordered)

    print(m.shape)
    myMax = np.max(m)

    H = np.ones([205, 205, 3])
    xLen, yLen = m.shape
    for x in range(xLen):
        for y in range(yLen):
            if m[x, y] != 0:
                myColor = np.around(m[x, y] / myMax, decimals=5) * 256
                H[x, y] = [myColor, 0, 0]

    plt.imshow(H)
    plt.grid(True)
    plt.xlabel("ChannelX")
    plt.ylabel("ChannelY")
    plt.ylim(-5, 205)
    plt.xlim(-5, 205)
    textstr = "Каналы упорядочены в возрастающем порядке по конверсии"
    conclusion = "Первые 25 каналов (с конверсией 0) плохо связаны между собой"
    red = "Чем краснее пиксель, тем теснее связь"
    plt.text(0.2, 0.06, textstr, fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.2, 0.04, conclusion, fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.2, 0.02, red, fontsize=14, transform=plt.gcf().transFigure)
    plt.tight_layout(pad=1.5)
    fig = plt.gcf()
    fig.set_size_inches(10, 10, forward=True)
    name = "train.txt"
    plt.title("AdjacencyMatrix." + name + ".png")
    plt.savefig("matchMatrix/AdjacencyMatrix.Red." + name + ".png")
    plt.clf()

def TryingAnotherVisualisation():
    myDirectory = "Conversion/"
    ordered = getOrderedListByConversion()
    m = matrixMiner(ordered)

    plt.imshow(m)
    plt.grid(True)
    plt.xlabel("ChannelX")
    plt.ylabel("ChannelY")
    plt.ylim(-5, 205)
    plt.xlim(-5, 205)
    fig = plt.gcf()
    fig.set_size_inches(10, 10, forward=True)
    name = "train.txt"
    plt.title("AdjacencyMatrix." + name + ".png")
    plt.savefig("matchMatrix/AdjacencyMatrix.TryingAnotherVisualisation." + name + ".png")

main()
#TryingAnotherVisualisation()
