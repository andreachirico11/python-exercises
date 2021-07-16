
# 0.0.1 1. Robot
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The movements are parsed and processed one at a time as input from the user until it writes STOP.
# Write a program that computes the distance from the starting point to the point in which the robot stopped.
# e.g.,
# UP 5 DOWN 3 LEFT 3 RIGHT 2
# Then, the output of the program should be: 51/2
import math


pos = (0, 0)


def check_for_stop(instruction):
    return instruction.find("stop") > 0 or instruction == "stop"


def update_pos(prev_pos, command, steps):
    if command == "up":
        return (prev_pos[0] + steps, prev_pos[1])
    elif command == "down":
        return (prev_pos[0] - steps, prev_pos[1])
    elif command == "left":
        return (prev_pos[0], prev_pos[1] - steps)
    elif command == "right":
        return (prev_pos[0], prev_pos[1] + steps)
    else:
        return prev_pos


def collect_move(robot_pos):
    while True:
        instruction = input('Give me the move: ')
        if check_for_stop(instruction):
            break
        command, steps = instruction.split()
    return update_pos(robot_pos, command, int(steps))


def count_distnance(firstPos, secondPos):
    deltaX = abs(secondPos[0] - firstPos[0])
    deltaY = abs(secondPos[1] - firstPos[1])
    return math.sqrt(deltaX**2 + deltaY**2)


print(count_distnance(pos, collect_move(pos)))
