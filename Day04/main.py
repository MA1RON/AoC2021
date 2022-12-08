import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2021/Day04')
import numpy as np

# read file
with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# read data
moves = lines[0].split(',')

len_board = 5
boards_number_total = (len(lines)-1) // 6
boards = [ [ [ None for i in range(len_board) ] for j in range(len_board) ] for k in range(boards_number_total)]
board_number = -1
for line in lines[1:]:
    if len(line) > 2: # to avoid empty lines
        char_index = 0
        while char_index < len(line):
            number = int(line[char_index:char_index+2].replace(' ','0'))
            col = char_index // 3
            
            boards[board_number][row][col] = number
            
            char_index += 3
        row += 1
    else: # empty line
        print(boards[board_number])
        row = 0
        board_number += 1
        
# play
for move in moves:
    