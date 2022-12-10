import re
import os
from turtle import width

x_timeline = []
WIDTH = 40
HEIGTH = 6
def process_add_cmd(arg):
    x_timeline.append(x_timeline[-1])
    x_timeline.append(x_timeline[-1] + arg)

def process_nop():
    x_timeline.append(x_timeline[-1])

def get_x_in_cicle(cycle):
    xpos = x_timeline[cycle]
    return [xpos -1, xpos, xpos+1]

x_timeline.append(1)
input_file = open("input.txt", "r")
lines = input_file.readlines()
if os.path.exists("output.txt"):
    os.remove("output.txt")
output_file = open("output.txt", "x")

for l in lines:
    line = re.split(" |\n",l)

    if line[0] == 'noop':
        process_nop()
    elif line[0] == 'addx':
        process_add_cmd(int(line[1]))
    else:
        print("SHIIIIIIITTT!")

# if len(x_timeline) > 21:
#     idx = 20
#     sum = 0
#     while idx < len(x_timeline) + 1:
#         sum = sum + x_timeline[idx-1] * idx
#         idx = idx + 40
# else:
#     print(0)

for cycle in range(0, WIDTH*HEIGTH):
    xpos = cycle%WIDTH
    ypos = cycle/WIDTH
    if cycle != 0 and cycle%WIDTH == 0:
        output_file.write("\n")
    if xpos in get_x_in_cicle(cycle):
        output_file.write("#")
    else:
        output_file.write(".")
print(sum)