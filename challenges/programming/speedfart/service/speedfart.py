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
    index = 0
    for y in range(rounds+1):
        for z in range(difficulty):
            # Get next symbol
            next_symbol = random.choice(symbols)

            # Randomly convert to loop symbols
            if random.randrange(100) < 10:
                next_symbol = random.choice(loops)

            # If index out of bounds swap symbol
            if index == 0 and next_symbol == "<":
                next_symbol = ">"
            elif index == (REGISTERS-1) and next_symbol == ">":
                next_symbol = "<"

            # If closing non-existant loop
            if (challenge.count("[") <= challenge.count("]") and
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

    # If last symbol is [, append -
    if challenge[-1] == "[":
        challenge.append("-")

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
    loops = 0
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

        # Check pointer sanity
        if pointer < 0 or pointer > REGISTERS:
            raise Exception("Pointer out of bounds!")

        # Iterate index
        index += 1

        # Wrap around register
        if registers[pointer] < 0:
            registers[pointer] = 255
        elif registers[pointer] > 255:
            registers[pointer] = 0

        # If loop operations
        if symbol == "[":
            # If register at pointer == 0
            if registers[pointer] == 0:
                # Go to end of loop
                depth = 1
                while depth > 0:
                    symbol = challenge[index]
                    if symbol == "[":
                        depth += 1
                    elif symbol == "]":
                        depth -= 1
                    index += 1
            else:
                # Append to recursions
                recursions.append(index)
        elif symbol == "]":
            # If value at pointer is not 0, loop again
            if registers[pointer] != 0:
                loops += 1
                index = recursions.pop() - 1

            # Check if we are looping too much
            if loops > 100:
                raise Exception("Too many loops!")

    # Check that registers are non-empty
    for register in registers:
        if register != 0:
            return registers

    # If registers empty, raise exception
    raise Exception("Registers empty!")

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

This may or may not help you:
- {REGISTERS} 8-bit registers
- {ROUNDS/2} rounds
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
    while solution[index] == 0:
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
