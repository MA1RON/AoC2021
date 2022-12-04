import os
os.chdir('/Users/matteocanducci/Documents/Advent of Code 2021/Day01')
import numpy as np

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# part 1
depth_increase = -1
line_previous = 0
for line in lines:
    if int(line) > int(line_previous):
        depth_increase += 1
    line_previous = line
print(depth_increase)

# part 2
depth_increase = 0
depth_history = [0,0,0,0]
depth_index = 0
for line in lines:
    depth_history.append(int(line))
    depth_history.pop(0)
    
    if depth_index >= 3:
        if sum(depth_history[1:]) > sum(depth_history[:-1]):
            depth_increase += 1

    depth_index += 1
print(depth_increase)
    