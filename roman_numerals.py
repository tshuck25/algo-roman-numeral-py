def to_roman(toenums):
    OUTPUT = ""
    ROMAN_NUMERAL_TO_ARABIC_MAP = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in ROMAN_NUMERAL_TO_ARABIC_MAP:
        ROMAN_NUMERAL = 0
        ARABIC_NUMBER = 0
    EVENLY_DIVISIBLE_TIMES = toenums / ARABIC_NUMBER
    if EVENLY_DIVISIBLE_TIMES >= 1:
        ROMAN_NUMERAL.append(EVENLY_DIVISIBLE_TIMES)
print()
    return
# Arabic = [1, 5, 10, 50, 100, 500, 1000]
# RomanNumerals = ["I", "V", "X", "L", "C", "D", "M"]
# newera = Arabic.split()
# RomanNumerals.split ()
# We want to break them down and them pair them together
    # pass
# print(newera)


# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)