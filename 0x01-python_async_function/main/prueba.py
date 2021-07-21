#!/usr/bin/env python3
argv = open('/proc/self/cmdline').read().split('\0')[2]
print(type(int(argv)))
print(argv)