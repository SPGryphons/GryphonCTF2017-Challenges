#! /usr/bin/env python3.6
##
# Created for GryphonCTF 2017_SpeedFart
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import random
import signal
import time

# Variables
ROUNDS = 100
DIFFICULTY = 64
REGISTERS = 16
TIMEOUT = 10
FLAG = "GCTF{1_h0p3_y0u_d1d_n07_7ry_7h15_m4nu4lly}"

# Define brainfuck symbols
symbols = [">", "<", "+", "-"]
loops = ["[", "]"]

# Define our functions
def generate(rounds, difficulty):
    # Reset challenge
    challenge = list()

    # For current round number, generate challenges squared
    looping = False
    index = 0
    for y in range(rounds+1):
        for z in range(difficulty):
            # Get next symbol
            next_symbol = random.choice(symbols)

            # If index out of bounds swap symbol
            if index == 0 and next_symbol == symbols[1]:
                next_symbol = symbols[0]
            elif index == (REGISTERS-1) and next_symbol == symbols[0]:
                next_symbol = symbols[1]

            # If closing non-existant loop
            if (challenge.count("[") < challenge.count("]") and
                    next_symbol == "]"):
                next_symbol = "["

            # If last symbol is [, don't append ]
            if len(challenge) > 0:
                while challenge[-1] == "[" and next_symbol == "]":
                    next_symbol = random.choice(symbols)

            # Update index
            if next_symbol == "<" or next_symbol == ">":
                index += 1 if next_symbol == ">" else -1

            # Append to challenge
            challenge.append(next_symbol)

        # Randomly append loop symbols
        if random.randrange(100) > 90:
            challenge.append(loops[0] if not looping else loops[1])

    # If looping symbols not closed
    if challenge.count("[") > challenge.count("]"):
        difference = challenge.count("[") - challenge.count("]")
        challenge += ["]"] * difference

    # Return challenge
    return challenge


def solve(challenge):
    # Initialize
    registers = [0] * REGISTERS
    pointer = 0
    index = 0
    recursions = []

    # Loop through challenges till end
    while index < len(challenge):
        # Get current symbol
        symbol = challenge[index]

        # If standard operations
        if symbol == ">":
            pointer += 1
        elif symbol == "<":
            pointer -= 1
        elif symbol == "+":
            registers[pointer] += 1
        elif symbol == "-":
            registers[pointer] -= 1

        # Iterate index
        index += 1

        # Wrap around register
        if registers[pointer] < 0:
            registers[pointer] = 255
        elif registers[pointer] > 255:
            registers[pointer] = 0

        # If loop operations
        if symbol == "[":
            # Append index
            recursions.append(index)
            end_loop = len(challenge) - challenge[::-1].index("]")

            # If value at pointer is 0, skip to end
            if registers[pointer] == 0:
                index = end_loop
        elif symbol == "]":
            # If we already looped too much
            if len(recursions) > 100:
                raise Exception("Too many loops!")

            # If value at pointer is not 0, loop again
            if registers[pointer] != 0:
                index = recursions[-1] - 1

    # Return registers
    return registers

def alarm(sig, frm):
    print()
    raise Exception

# Print greeting
print(f"""
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

Hello there! I am the new automated testing machine!
Unfortunately, I am also slightly stupid.

I will ask you a series of questions.
All you have to do, is send me your replies.
The catch? You have to do it within {TIMEOUT} seconds.
""")

# Check if ready
ready = input("Are you ready? [y/n] ")
if ready != "y":
    quit()

# Prepare signal handler
signal.signal(signal.SIGALRM, alarm)

# Loop number of rounds
for x in range(ROUNDS):
    challenge = None
    solution = None

    # Keep generating solvable challenges
    while True:
        try:
            # Get challenge and solution
            challenge = generate(x, DIFFICULTY)
            solution = solve(challenge)
            
            # Break out of loop
            break
        except:
            pass

    # Print challenge
    print(f"\nROUND {x+1}, FIGHT!")
    print(f"{'+-'*10}\n")
    print("\n".join(["".join(challenge[DIFFICULTY * i:DIFFICULTY * (i+1):])
                     for i in range(int(len(challenge) / DIFFICULTY) + 1)]))
    print(f"\n{'+-'*10}")

    # Prepare question
    index = random.randrange(REGISTERS)
    suffix = ""

    # Get suffix
    if index == 0:
        suffix = "st"
    elif index == 1:
        suffix = "nd"
    elif index == 2:
        suffix = "rd"
    else:
        suffix = "th"

    try:
        # Get response
        signal.alarm(TIMEOUT)
        response = int(input(f"What value is in the {index+1}{suffix} register? "))
        signal.alarm(0)

        # Check if response is correct
        if solution[index] == int(response):
            print("Correct!")
            continue
        else:
            print("GeT gOoD aT sPeEdFaRt!")
    except:
        # Print error message
        print("Invalid Input :c")

    # Quit if we reach here
    quit()

# Print flag
print(f"Flag is: {FLAG}")
