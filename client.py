#!/usr/bin/env python
import urllib2
import sys
import time

if __name__ == "__main__":
    addr = sys.argv[1]
    port = sys.argv[2]
    msg = sys.argv[3]
    while True:
        time.sleep(1)
        context = urllib2.urlopen('http://%s:%s/' % (addr,port)).read()
        print(context)