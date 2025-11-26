#!/usr/bin/env python3

def f():
    l = [1,2,3,4,5,6]
    fs = frozenset(l)
    try:
        fs.add(7)
    except AttributeError:
        print("Método no permitido en los datos frozenset")
    else:
        return fs

f()
