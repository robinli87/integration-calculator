import math
import multiprocessing as mp
#from tkinter import *

function = str(input("Enter f(x) as an expression containing only x: "))

with open("funcfile.py", "w") as transfile:
    #we attempt to write your mathematical function as a python function and save it into a new funcfile
    #we will then attempt to import this function and run it
    transfile.write("import math")
    transfile.write("e = math.e") #get the frequently used constants out of the way
    transfile.write("pi = math.pi")
    transfile.write("def f(x):" + "\n")
    transfile.write("    " + "y = " +function + "\n")
    transfile.write("    return(y)")

upper = float(input("Enter upper bound"))
lower = float(input("Enter lower bound"))
dx = 0.000001

import funcfile

threadcount = 16
chunk_size = (upper-lower) / threadcount
parts = []

def calculate(i):
    start = lower + i * chunk_size
    end = start + chunk_size
    x = start
    this_A = 0
    while x < end:
        dA = (funcfile.f(x) + funcfile.f(x+dx)) * dx / 2
        this_A += dA
        x += dx
    return(this_A)

def log(result):
    parts.append(result)
    return(result)

pool = mp.Pool()

for i in range(0, threadcount):
    p = pool.apply_async(calculate, args=(i, ), callback=log)

pool.close()
pool.join()

print(sum(parts))

# class GUI:
#     def __init__(self, master):
#         self.master = master
#
#         self.master.title("Integration Calculator")
#
#         self.entries = []
#         new_entry = Entry(self.master)
#         new_entry.grid()
#         self.entries.append(new_entry)
#         self.entry.pack()
