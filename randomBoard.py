import random


board = [[random.randint(0, 9) for i in range(10)] for y in range(10)]


def printBoard(table):
    for i in range(len(table)):
        for k in range(len(table[i])):
            print("%s " % table[i][k], end="")
        print()


def findSum(table):
    total = 0
    for row in table:
        for column in row:
            total += column
    print(total)


printBoard(board)
findSum(board)
