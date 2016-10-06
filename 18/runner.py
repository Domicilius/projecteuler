#!/usr/bin/python

f = open('data', 'r')
data = ''
i = 0
stuff = []
for line in f:
    stuff.append(line.split())

def recurse(stuff):
    if len(stuff) == 1:
        print stuff
        return
    else:
        holder=[]
        newlastrow=len(stuff)-2
        mergedrow=len(stuff)-1

        for i in range(0, len(stuff[newlastrow])):
            holder.append(int(stuff[newlastrow][i])+int(max(stuff[mergedrow][i], stuff[mergedrow][i+1])))

        stuff[newlastrow]=holder
        del stuff[-1]
        recurse(stuff)

recurse(stuff)
