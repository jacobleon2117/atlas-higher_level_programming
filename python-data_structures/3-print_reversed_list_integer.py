#!/usr/bin/python3

def print_reversed_list_integer(list=[]):
    if list is not None:
        for i in range(len(list)-1, -1, -1):
            print("{:d}".format(list[i]))