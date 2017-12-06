def day1(s):
    s = s + s[0]
    return sum(int(s[i]) for i in range(len(s)-1) if s[i] == s[i+1])

def day1b(s):
    l = len(s)
    s = s * 2 
    return sum(int(s[i]) for i in range(int(len(s)/2)) if s[i] == s[i+int((l/2))])

def day2(s):
    tot = 0
    for line in s.split('\n'):
        vals = [int(v) for v in line.split('\t')]
        tot += max(vals) - min(vals)
    return tot

from itertools import product
def day2b(s):
    tot = 0
    for line in s.split('\n'):
        vals = [int(v) for v in line.split('\t')]
        for a,b in product(vals, vals):
            if a!=b and a % b == 0:
                print(a,b)
                tot += a/b
    return tot

def day3(n):
    left = {(1,0): (0,1), (0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0)}
    level = 1
    i = 1
    x,y = 0,0
    dx, dy = 1,0
    while 1:
        for _ in range(2):   
            for _ in range(level-1):
                if i == n: return abs(x) + abs(y)
                i += 1
                x += dx
                y += dy
            dx,dy = left[(dx,dy)]            
        level += 1

def day3b(n):
    left = {(1,0): (0,1), (0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0)}
    grid = {(0,0): 1}
    level = 1
    x,y = 0,0
    dx, dy = 1,0
    while 1:
        for _ in range(2):   
            for _ in range(level-1):
                nbd = [grid.get((a,b)) for a in range(x-1,x+2) for b in range(y-1,y+2)]
                v = sum(n for n in nbd if n)
                if v > n: return v
                grid[(x,y)] = v
                x += dx
                y += dy
            dx,dy = left[(dx,dy)]            
        level += 1

def day4(s):
    count = 0
    for line in s.split('\n'):
        words = line.split()
        if len(set(words)) == len(words):
            count += 1
    return count

def day4b(s):
    count = 0
    for line in s.split('\n'):
        words = [tuple(sorted(l)) for l in line.split()]
        if len(set(words)) == len(words):
            count += 1
    return count

def day5(s):
    n_steps = 1
    L = [int(x) for x in s.split('\n')]
    pos = 0
    while 1:
        val = L[pos]
        L[pos] += 1
        pos += val 
        if pos >= len(L):
            return n_steps
        n_steps += 1
day5(s)

def day5b(s):
    n_steps = 1
    L = [int(x) for x in s.split('\n')]
    pos = 0
    while 1:
        val = L[pos]
        if val >= 3:
            L[pos] -= 1
        else:
            L[pos] += 1
        pos += val 
        if pos >= len(L):
            return n_steps
        n_steps += 1

import numpy as np
def day6(s):
    dat = [int(i) for i in s.split()]
    states = [dat.copy()]
    while 1:
        c = np.argmax(dat)
        v = dat[c]
        dat[c] = 0
        c = (c + 1) % len(dat)
        while v > 0:
            dat[c] += 1
            v -= 1
            c = (c + 1) % len(dat)
        if dat in states:
            return len(states)
        states.append(dat.copy())

def day6b(s):
    dat = [int(i) for i in s.split()]
    states = [dat.copy()]
    while 1:
        c = np.argmax(dat)
        v = dat[c]
        dat[c] = 0
        c = (c + 1) % len(dat)
        while v > 0:
            dat[c] += 1
            v -= 1
            c = (c + 1) % len(dat)
        if dat in states:
            return len(states) - states.index(dat)
        states.append(dat.copy())
