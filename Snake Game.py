import time
from tkinter import *
import re
import sys
import os


goRight = None
goLeft = None
goUp = None
goDown = None
canvas_id = None

def listToStringWithoutBrackets(value):
    return str(value).replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(',', '').replace(
        "'", '').replace(' ', '')


file = open('game.txt','w')
file.write("snakexStart = 100\nsnakeyStart = 100\nupLock = 0\ndownLock = 0\nleftLock = 0\nrightLock = 0\nmoveRightLockSave = 1\nmoveLeftLockSave = 1\nmoveUpLockSave = 1\nmoveDownLockSave = 1\nlength = 100")
file.close()

file = open('gameBackup.txt','w')
file.write("snakexStart = 100\nsnakeyStart = 100\nupLock = 0\ndownLock = 0\nleftLock = 0\nrightLock = 0\nmoveRightLockSave = 1\nmoveLeftLockSave = 1\nmoveUpLockSave = 1\nmoveDownLockSave = 1\nlength = 100")
file.close()

file = open('instance.txt','w')
file.write("right = 1\nleft = 1\nupLock = 1\nup = 1\ndown = 1")
file.close()



root = Tk()
root.title = ('Snake Game')
root.geometry("800x600")

w = 800
h = 600
x = w//2
y = h//2


stage = Canvas(root, width=w, height=h, bg='white')
stage.create_line(2, 2, w, 1, fill='red', width=8)
stage.create_line(1, 1, 1, h, fill='red', width=8)
stage.create_line(1, h-2, w, h-2, fill='red', width=8)
stage.create_line(w-2, 1, w-2, h, fill='red', width=8)
stage.pack()




def lefties():
    global goRight
    global goLeft
    global goUp
    global goDown
    global canvas_id
    with open('gameBackup.txt', 'r') as firstfile, open('game.txt', 'w') as secondfile:

        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)


    with open('game.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'snakexStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                acidGrowth = int(game)
            if 'snakeyStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                liquidGrowth = int(game)
            if 'rightLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                rightLock = int(game)
            if 'leftLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                leftLock = int(game)
            if 'upLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                upLock = int(game)
            if 'downLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                downLock = int(game)
            if 'moveRightLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveRightLock = int(game)
            if 'moveLeftLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveLeftLock = int(game)
            if 'moveUpLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveUpLock = int(game)
            if 'moveDownLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveDownLock = int(game)
            if 'length' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                length = int(game)


        if leftLock == 0:
            # x = 1
            # y = 0
            # stage.move(snake, x, y)

            xStartline = acidGrowth
            yStartline = liquidGrowth

            acidGrowth -= 10

            if acidGrowth < 8:
                acidGrowth = 8
            liquidGrowth = liquidGrowth

            xGrowthline = acidGrowth
            yGrowthline = liquidGrowth

            stage.delete(canvas_id)
            canvas_id = stage.create_line(xStartline, yStartline + length, xGrowthline + length, yGrowthline + length, fill='black', width=8)
            print(f"Starting Cordinates: x1={xStartline},y1={yStartline} to Ending Cordinates: x2={xGrowthline},y2={yGrowthline}")

            rightLock = 1
            leftLock = 0
            upLock = 0
            downLock = 0

            moveRightLock = 0
            moveLeftLock = 1
            moveUpLock = 0
            moveDownLock = 0

            xStartline = str(xGrowthline)
            yStartline = str(yGrowthline)

            leftLockSave = str(leftLock)
            rightLockSave = str(rightLock)
            upLockSave = str(upLock)
            downLockSave = str(downLock)

            moveRightLockSave = str(moveRightLock)
            moveLeftLockSave = str(moveLeftLock)
            moveUpLockSave = str(moveUpLock)
            moveDownLockSave = str(moveDownLock)

            file = open('game.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))
            file = open('gameBackup.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave  + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))


        else:
            print("Lock")

    if moveLeftLock == 1:
        goLeft = root.after(200, lefties)
    else:
        pass

def left(none):
    with open('instance.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'right' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                right = int(game)
            if 'left' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                left = int(game)
            if 'up' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                up = int(game)
            if 'down' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                down = int(game)
    if left == 1:
        with open('game.txt') as f:
            for line in f:
                if 'rightLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    rightLock = int(game)
                if 'leftLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    leftLock = int(game)
                if 'upLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    upLock = int(game)
                if 'downLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    downLock = int(game)
            if leftLock == 0:
                lefties()
                stopRight()
                stopDown()
                stopUp()
                right = str(1)
                left = str(0)
                up = str(1)
                down = str(1)
                file = open('instance.txt', 'w')
                file.write(
                    "right = " + right + "\nleft = " + left + "\nup = " + up + "\ndown = " + down)




def rights():
    global goRight
    global goLeft
    global goUp
    global goDown
    global canvas_id
    with open('gameBackup.txt', 'r') as firstfile, open('game.txt', 'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    with open('game.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'snakexStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                acidGrowth = int(game)
            if 'snakeyStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                liquidGrowth = int(game)
            if 'rightLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                rightLock = int(game)
            if 'leftLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                leftLock = int(game)
            if 'upLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                upLock = int(game)
            if 'downLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                downLock = int(game)
            if 'moveRightLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveRightLock = int(game)
            if 'moveLeftLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveLeftLock = int(game)
            if 'moveUpLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveUpLock = int(game)
            if 'moveDownLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveDownLock = int(game)
            if 'length' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                length = int(game)

        if rightLock == 0:
            # x = 1
            # y = 0
            # stage.move(snake, x, y)


            xStartline = acidGrowth
            yStartline = liquidGrowth



            acidGrowth += 10

            if acidGrowth > w-8:
                acidGrowth = w-8

            liquidGrowth = liquidGrowth
            xGrowthline = acidGrowth

            if xStartline == 100 and yStartline == 100:
                xGrowthline = 150


            yGrowthline = liquidGrowth

            stage.delete(canvas_id)
            canvas_id = stage.create_line(xStartline, yStartline, xGrowthline+length, yGrowthline, fill='black', width=8)
            # canvas_id = stage.create_line(xStartline, yStartline, xGrowthline, yGrowthline, fill='black', width=8)
            print(f"Starting Cordinates: x1={xStartline},y1={yStartline} to Ending Cordinates: x2={xGrowthline},y2={yGrowthline}")

            leftLock = 1
            rightLock = 0
            upLock = 0
            downLock = 0

            moveRightLock = 1
            moveLeftLock = 0
            moveUpLock = 0
            moveDownLock = 0

            right = 0


            xStartline = str(xGrowthline)
            yStartline = str(yGrowthline)

            leftLockSave = str(leftLock)
            rightLockSave = str(rightLock)
            upLockSave = str(upLock)
            downLockSave = str(downLock)

            moveRightLockSave = str(moveRightLock)
            moveLeftLockSave = str(moveLeftLock)
            moveUpLockSave = str(moveUpLock)
            moveDownLockSave = str(moveDownLock)

            rightInstance = str(right)

            file = open('game.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))
            file = open('gameBackup.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))

        else:
            print("Lock")

    if moveRightLock == 1:
       goRight = root.after(200, rights)

    else:
        # root.after_cancel(goRight)
        # goRight = None
        pass


def right(none):
    with open('instance.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'right' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                right = int(game)
            if 'left' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                left = int(game)
            if 'up' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                up = int(game)
            if 'down' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                down = int(game)
    if right == 1:
        with open('game.txt') as f:
            for line in f:
                if 'rightLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    rightLock = int(game)
                if 'leftLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    leftLock = int(game)
                if 'upLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    upLock = int(game)
                if 'downLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    downLock = int(game)
            if rightLock == 0:
                rights()
                stopDown()
                stopLeft()
                stopUp()
                right = str(0)
                left = str(1)
                up = str(1)
                down = str(1)
                file = open('instance.txt', 'w')
                file.write("right = " + right + "\nleft = " + left + "\nup = " + up + "\ndown = " + down)









def upper():
    global goRight
    global goLeft
    global goUp
    global goDown
    global canvas_id
    with open('gameBackup.txt', 'r') as firstfile, open('game.txt', 'w') as secondfile:

        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    with open('game.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'snakexStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                acidGrowth = int(game)
            if 'snakeyStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                liquidGrowth = int(game)
            if 'rightLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                rightLock = int(game)
            if 'leftLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                leftLock = int(game)
            if 'upLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                upLock = int(game)
            if 'downLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                downLock = int(game)
            if 'moveRightLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveRightLock = int(game)
            if 'moveLeftLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveLeftLock = int(game)
            if 'moveUpLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveUpLock = int(game)
            if 'moveDownLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveDownLock = int(game)
            if 'length' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                length = int(game)

        if upLock == 0:
            # x = 0
            # y = 1
            # stage.move(snake, x, y)

            xStartline = acidGrowth
            yStartline = liquidGrowth

            liquidGrowth -= 10

            xGrowthline = acidGrowth
            yGrowthline = liquidGrowth

            if liquidGrowth < 8:
                liquidGrowth = 8

            if xStartline == 100 and yStartline == 100:
                xGrowthline = 150
                xStartline = 150

            stage.delete(canvas_id)
            canvas_id = stage.create_line(xStartline, yStartline, xGrowthline, yGrowthline + length, fill='black', width=8)
            print(f"Starting Cordinates: x1={xStartline},y1={yStartline} to Ending Cordinates: x2={xGrowthline},y2={yGrowthline}")

            leftLock = 0
            rightLock = 0
            upLock = 0
            downLock = 1

            moveRightLock = 0
            moveLeftLock = 0
            moveUpLock = 1
            moveDownLock = 0


            xStartline = str(xGrowthline)
            yStartline = str(yGrowthline)
            leftLockSave = str(leftLock)
            rightLockSave = str(rightLock)
            upLockSave = str(upLock)
            downLockSave = str(downLock)

            moveRightLockSave = str(moveRightLock)
            moveLeftLockSave = str(moveLeftLock)
            moveUpLockSave = str(moveUpLock)
            moveDownLockSave = str(moveDownLock)

            file = open('game.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))
            file = open('gameBackup.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))

        else:
            print("Lock")

    if moveUpLock == 1:
        goUp = root.after(200, upper)
    else:
        root.after(0, downtown)

def up(none):
    with open('instance.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'right' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                right = int(game)
            if 'left' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                left = int(game)
            if 'up' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                up = int(game)
            if 'down' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                down = int(game)
    if up == 1:
        with open('game.txt') as f:
            for line in f:
                if 'rightLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    rightLock = int(game)
                if 'leftLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    leftLock = int(game)
                if 'upLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    upLock = int(game)
                if 'downLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    downLock = int(game)
            if upLock == 0:
                upper()
                stopDown()
                stopRight()
                stopLeft()
                right = str(1)
                left = str(1)
                up = str(0)
                down = str(1)
                file = open('instance.txt', 'w')
                file.write(
                    "right = " + right + "\nleft = " + left + "\nup = " + up + "\ndown = " + down)



def downtown():
    global goRight
    global goLeft
    global goUp
    global goDown
    global canvas_id
    with open('gameBackup.txt', 'r') as firstfile, open('game.txt', 'w') as secondfile:

        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)

    with open('game.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'snakexStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                acidGrowth = int(game)
            if 'snakeyStart' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                liquidGrowth = int(game)
            if 'rightLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                rightLock = int(game)
            if 'leftLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                leftLock = int(game)
            if 'upLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                upLock = int(game)
            if 'downLock' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                downLock = int(game)
            if 'moveRightLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveRightLock = int(game)
            if 'moveLeftLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveLeftLock = int(game)
            if 'moveUpLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveUpLock = int(game)
            if 'moveDownLockSave' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                moveDownLock = int(game)
            if 'length' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                length = int(game)

        if downLock == 0:
            # x = 0
            # y = 1
            # stage.move(snake, x, y)

            xStartline = acidGrowth
            yStartline = liquidGrowth

            liquidGrowth += 10

            if liquidGrowth > h-10:
                liquidGrowth = h-10
            acidGrowth = acidGrowth

            xGrowthline = acidGrowth
            yGrowthline = liquidGrowth

            if xStartline == 100 and yStartline == 100:
                xGrowthline = 150
                xStartline = 150

            stage.delete(canvas_id)
            canvas_id = stage.create_line(xStartline + length, yStartline, xGrowthline + length, yGrowthline + length, fill='black', width=8)
            print(f"Starting Cordinates: x1={xStartline},y1={yStartline} to Ending Cordinates: x2={xGrowthline},y2={yGrowthline}")

            leftLock = 0
            rightLock = 0
            upLock = 1
            downLock = 0

            moveRightLock = 0
            moveLeftLock = 0
            moveUpLock = 0
            moveDownLock = 1

            xStartline = str(xGrowthline)
            yStartline = str(yGrowthline)
            leftLockSave = str(leftLock)
            rightLockSave = str(rightLock)
            upLockSave = str(upLock)
            downLockSave = str(downLock)

            moveRightLockSave = str(moveRightLock)
            moveLeftLockSave = str(moveLeftLock)
            moveUpLockSave = str(moveUpLock)
            moveDownLockSave = str(moveDownLock)

            file = open('game.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(length))
            file = open('gameBackup.txt', 'w')
            file.write(
                "snakexStart = " + xStartline + "\nsnakeyStart = " + yStartline + "\nleftLock = " + leftLockSave + "\nrightLock = " + rightLockSave + "\nupLock = " + upLockSave + "\ndownLock = " + downLockSave + "\nmoveRightLockSave = " + moveRightLockSave + "\nmoveLeftLockSave = " + moveLeftLockSave + "\nmoveUpLockSave = " + moveUpLockSave + "\nmoveDownLockSave = " + moveDownLockSave + "\nlength = " + str(
                    length))
        else:
            print("Lock")

    if moveDownLock == 1:
        goDown = root.after(200, downtown)


    else:
        # root.after_cancel(go)
        None

def down(none):
    with open('instance.txt') as f:
        for line in f:
            # For Python3, use print(line)
            if 'right' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                right = int(game)
            if 'left' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                left = int(game)
            if 'up' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                up = int(game)
            if 'down' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                down = int(game)
    if down == 1:
        with open('game.txt') as f:
            for line in f:
                if 'rightLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    rightLock = int(game)
                if 'leftLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    leftLock = int(game)
                if 'upLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    upLock = int(game)
                if 'downLock' in line:
                    txt = str(line)
                    receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                    game = listToStringWithoutBrackets(receipts)
                    downLock = int(game)
            if downLock == 0:
                downtown()
                stopRight()
                stopLeft()
                stopUp()
                right = str(1)
                left = str(1)
                up = str(1)
                down = str(0)
                file = open('instance.txt', 'w')
                file.write(
                    "right = " + right + "\nleft = " + left + "\nup = " + up + "\ndown = " + down)

def stopRight():
    global goRight

    if goRight:
        root.after_cancel(goRight)
        goRight = None

def stopDown():
    global goDown

    if goDown:
        root.after_cancel(goDown)
        goDown = None


def stopLeft():
    global goLeft

    if goLeft:
        root.after_cancel(goLeft)
        goLeft = None

def stopUp():
    global goUp

    if goUp:
        root.after_cancel(goUp)
        goUp = None

# def stop():
#     global goRight
#     global goLeft
#     global goUp
#     global goDown
#
#     if goRight:
#         root.after_cancel(goRight)
#         goRight = None
#
#     elif goLeft:
#         root.after_cancel(goLeft)
#         goLeft = None
#
#     elif goUp:
#         root.after_cancel(goUp)
#         goUp = None
#
#     elif goDown:
#         root.after_cancel(goDown)
#         goDown = None


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
canvas_id = stage.create_line(100, 100, 200, 100, fill='black', width=8)

# snake = stage.create_rectangle(x, y, x+10, y+10, fill='black')



root.mainloop()




