import os
import time
import _pickle as pickle
from itertools import islice
import numpy as np


def myPickler(directory, pathfile):
    t0 = time.time()
    myChannels = set()
    myConvDit = {}
    # Creating empty in order to not check existence
    for i in range(505):
        myConvDit[i] = [0, 0]

    # Opening file by the path given to method
    # For reading lines from a file, you can loop over the file object.
    # This is memory efficient, fast, and leads to simple code:
    f = open(pathfile, "rb")
    # Special variable to count how many lines in the pathfile
    countlines = 0
    for line in islice(f, 1, None):
        lineList = str(line).split(',')
        channel = int(lineList[4])
        myChannels.add(channel)
        # Adding 1 in case of existence
        myConvDit[channel][0] += 1
        # Adding is_attributed to count conversion
        is_attributed = int(lineList[-1][0])
        myConvDit[channel][1] += is_attributed
    f.close()
    print("Time: ", np.around((time.time() - t0) / 60, 2))
    print("There are ", countlines, " lines in the ", pathfile)
    print("For key in myConvDict there are [appearances, downloads]")

    for key in list(myConvDit):
        if myConvDit[key][0] == 0:
            del myConvDit[key]
        else:
            print("myConvDit[", key, "] = ", myConvDit[key])

    print("Chosen not empty from the dictionary")
    print(" len(myChannels) = ", len(myChannels), " len(myConvDict) = ", str(len(myConvDit)))

    name = "channelsNumbers." + pathfile
    f = open(directory + "/" + name, "wb")
    pickle.dump(myChannels, f)
    f.close()
    del myChannels
    print("myChannels saved as ", name, " in ", directory)

    name = "channelsDict." + pathfile
    f = open(directory + "/" + name, "wb")
    pickle.dump(myConvDit, f)
    f.close()
    del myConvDit
    print("myConvDict saved as ", name, " in ", directory)

    print("Time: ", np.around((time.time() - t0)/60, 2))
    return "This line is returned from the myPickler method"


def main():
    myDirectory = "myPickler/"
    if not os.path.exists(myDirectory):
        os.makedirs(myDirectory)
    print(myPickler(directory=myDirectory, pathfile="train_sample.txt"))
    print(myPickler(directory=myDirectory, pathfile="train.txt"))


main()
