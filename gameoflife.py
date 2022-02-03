import os
import time


# lm = list zakhire

def convertor(file):
    l = []
    counter = 0
    for i in file:
        l.append([])
        for j in i:
            if j == '█':
                l[counter].append(1)
            if j == '░':
                l[counter].append(0)
        counter += 1
    return l


def ezraeil():
    for i in range(n):
        for j in range(m):
            count = 0
            if lm[i][j] == 1:
                for x in range(i - 1, i + 2):
                    if x in range(n):
                        for y in range(j - 1, j + 2):
                            if y in range(m):
                                if lm[x][y] == 1:
                                    count += 1
                if count < 3 or count > 4:
                    l[i][j] = 0


def dastmasih():
    for i in range(n):
        for j in range(m):
            if lm[i][j] == 0:
                count = 0
                for x in range(i - 1, i + 2):
                    if x in range(n):
                        for y in range(j - 1, j + 2):
                            if y in range(m):
                                if lm[x][y] == 1:
                                    count += 1
                if count == 3:
                    l[i][j] = 1


def tasvir():
    for i in l:
        for j in i:
            if j == 1:
                print('█', end='')
            else:
                print('░', end='')
        print()


def clear():
    os.system('cls') if os.name == "nt" else os.system('clear')


f = open('map2.init', 'r', encoding='utf-8')
l = convertor(f)
lm = l.copy()
n = len(l)
m = len(l[0])

while True:
    ezraeil()
    dastmasih()
    tasvir()
    time.sleep(1)
    clear()
    lm = l.copy()
