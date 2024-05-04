#!/usr/bin/env python3

def sort(width, height, length, mass):
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise Exception("Invalid input")

    volume = width * height * length
    bulky = False
    heavy = False

    if volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150:
        bulky = True
    if mass >= 20:
        heavy = True

    if not bulky and not heavy:
        return "STANDARD"
    elif bulky and heavy:
        return "REJECTED"
    else:
        return "SPECIAL"

# Base case
assert(sort(0, 0, 0, 0) == "STANDARD")
assert(sort(1, 1, 1, 1) == "STANDARD")

# More basic cases
assert(sort(15, 0, 0, 0) == "STANDARD")
assert(sort(0, 15, 0, 0) == "STANDARD")
assert(sort(0, 0, 15, 0) == "STANDARD")

# SPECIAL: Bulky because of length
assert(sort(150, 0, 0, 0) == "SPECIAL")
assert(sort(0, 150, 0, 0) == "SPECIAL")
assert(sort(0, 0, 150, 0) == "SPECIAL")

# SPECIAL: Bulky because of volume
assert(sort(1_000_000, 1, 1, 0) == "SPECIAL")
assert(sort(1, 1_000_000, 1, 0) == "SPECIAL")
assert(sort(1, 1, 1_000_000, 0) == "SPECIAL")

# SPECIAL: Bulky because heavy
assert(sort(0, 0, 0, 20) == "SPECIAL")
assert(sort(0, 0, 0, 1000) == "SPECIAL")

# REJECTED: A combination of point 1 and 2
assert(sort(150, 0, 0, 20) == "REJECTED")
assert(sort(0, 150, 0, 20) == "REJECTED")
assert(sort(0, 0, 150, 20) == "REJECTED")

assert(sort(1_000_000, 1, 1, 20) == "REJECTED")
assert(sort(1, 1_000_000, 1, 20) == "REJECTED")
assert(sort(1, 1, 1_000_000, 20) == "REJECTED")
