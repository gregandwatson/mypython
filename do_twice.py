#!/usr/bin/python

def do_twice(f, v):
    f(v)
    f(v)

def print_twice('ditto'):
    print('spam')

do_twice(print_spam, 'tigger')
