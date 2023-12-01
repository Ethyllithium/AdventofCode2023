units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]
calibration_total = 0
with open("input.txt", "r") as file:
    for line in file:
        calibration = ""
        for unit in units:
            line = line.replace(unit, (unit + str(units.index(unit)) + unit))
        for char in line:
            if char.isdigit():
                calibration += char
        calibration = calibration[0] + calibration[-1]
        calibration_total += int(calibration)
print(calibration_total)