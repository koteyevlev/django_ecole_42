#!/usr/bin/env python3

def geohashing():
    import antigravity, sys
    argv = sys.argv
    if (len(argv) != 4):
        print("Invalid Argument exception")
    else:
        antigravity.geohash(float(argv[1]), float(argv[2]), argv[3].encode())


if __name__ == '__main__':
    geohashing()
