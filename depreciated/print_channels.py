
def print_channels(file):

    channels = file.search("*", mode = 'wildcard')

    with open(r'channels.txt', 'w') as fp:
        for item in channels:
            print(item)
            fp.write("%s\n" % item)

        print('Done: All available channels saved to "channels.txt"')
        print("There are " + str(len(channels)) + " channels in the datafile")
        

    return
