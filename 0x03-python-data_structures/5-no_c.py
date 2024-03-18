#!/usr/bin/python3
def no_c(my_string):
    another_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            another_string += elements
    return another_string

