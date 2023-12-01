units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]
reversed_units = [i[::-1] for i in units]
calibration_total = 0

with open("input.txt", "r") as file:
    for line in file:
        new_line = ""
        new_line_reversed = ""
        calibration = ""
        for char in line:
            if char.isdigit():
                calibration += char
            else:
                new_line += char
                for unit in units:
                    if unit in new_line:
                        calibration += str(units.index(unit))
                        print(new_line + "+" + unit)
                        break
            if calibration:
                break
        for char in reversed(line):
            if char.isdigit():
                calibration += char
                break
            else:
                new_line_reversed += char
                for unit in reversed_units:
                    if unit in new_line_reversed:
                        calibration += str(reversed_units.index(unit))
                        print(new_line_reversed + "+" + unit)
                        break
            if len(calibration) == 2:
                break
        print(calibration)
        calibration_total += int(calibration)
print(calibration_total)


