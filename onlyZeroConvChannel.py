import numpy as np
import os
import glob
import math
import matplotlib.pyplot as plt
import _pickle as pickle
import psutil
from itertools import islice
import time


def mainKaggle(path):
    f = open(path, "rb")
    myDict = pickle.load(f)
    f.close()
    onlyzero = []
    for channel in myDict:
        if myDict[channel][1] == 0:
            onlyzero.append(channel)
    return onlyzero

def main():
    psample = "myPickler/channelsDict.train_sample.txt"
    ptrain = "myPickler/channelsDict.train.txt"
    onlyzero = mainKaggle(path=ptrain)
    print(onlyzero)

main()
