with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

# part 1
depth = 0
distance = 0
for line in lines:
    [command,amount] = line.split(' ')
    if command == 'forward':
        distance += int(amount)
    if command == 'up':
        depth -= int(amount)
    if command == 'down':
        depth += int(amount)
print(f'Distance: {distance}. Depth: {depth}. Total = {distance * depth}.') 

# part 2
depth = 0
distance = 0
aim = 0
for line in lines:
    [command,amount] = line.split(' ')
    if command == 'forward':
        distance += int(amount)
        depth += int(amount)*aim
    if command == 'up':
        aim -= int(amount)
    if command == 'down':
        aim += int(amount)
print(f'Distance: {distance}. Depth: {depth}. Aim: {aim}.\nTotal = {distance * depth}.')    