#!/usr/bin/python2
from pwn import *
import re

local = True
if local:
    p = remote('localhost', 5000)
else:
    p = remote('web.red.csaw.io', 5010)


#print(data)

def blank(line):
    return len(line) > 1 and line.strip()==''

def is_header(line):
    return (len(line.split("|")) > 1) or len(line.split("#") > 1) or len(line.split("+") > 1) or len(line.split(".") > 1)

def get_column_character(line):
    #print("In get_column_character: line = " + line)
    if len(line.split("|")) > 1:
        return("|")
    elif len(line.split("#")) > 1:
        return("#")
    elif len(line.split("+")) > 1:
        return("+")
    elif len(line.split("*")) > 1:
        return("*")
    elif len(line.split("@")) > 1:
        return("@")
    elif len(line.split(":")) > 1:
        return(":")
    elif len(line.split("<")) > 2:
        return("<")
    elif len(line.split("[")) > 1:
        return("[")
    elif len(line.split("{")) > 1:
        return("{")
    elif len(line.split(".")) > 4:
        return(".")
    else:
        print("ERROR: Count not determine column character.")
        return 0

def get_column(line):
    column_character = get_column_character(line)
    #print("column_character = " + column_character)
    col = -1
    cursor = 0
    in_column = 0
    if column_character != "<" and column_character != "[" and column_character != "{":
        while (cursor < len(line)):
            if line[cursor]==column_character:
                in_column = 1-in_column
                if in_column:
                    col += 1
            elif line[cursor] == "O":
                if column_character != ".":
                    #print("Found mole in column " + str(col))
                    return(col)
                else: # two periods in the mole prior to reaching the mole's nose
                    #print("Found mole in column " + str(col-1))
                    return(col-1)
            cursor += 1
    else:
        while (cursor < len(line)):
            if line[cursor]==column_character:
                col += 1
            elif line[cursor] == "O":
                #print("Found mole in column " + str(col))
                return(col)
            cursor += 1
    print("Did not find mole column.")
    return -1

def get_row_and_column(data):
    row = 0
    col = 0
    prev_blank_line = 0
    lines = data.split("\n")
    for line in lines:
        #print("line = " + line)
        if blank(line):
            if not prev_blank_line:
                row += 1
            prev_blank_line = 1
        else:
            prev_blank_line = 0
            if "../ \" O \" \.." in line: # found nose
                #print("Found nose: " + line)
                col = get_column(line)
                #print("Nose was in column " + str(col))
                #print("Nose was in row " + str(row))
                return(row, col)
    # starting by counting the lines of data.
    print("Did not find mole!")
    return (-1, -1)

def advance_to_first_line_of_board():
    p.recvuntil("Score:")
    p.recvuntil("\n")
    p.recvuntil("\n")

def solve_next_board():
    data = p.recvuntil("(row col): ")
    lines = data.split("\n")
    #print("nlines: " + str(len(lines)))
    row, col = get_row_and_column(data)
    #print("Row: " + str(row) + "and Column: " + str(col))
    p.send(str(row) + " " + str(col) + "\n")

for i in range(101):
    advance_to_first_line_of_board()
    solve_next_board()

p.interactive()

