calibration_total = 0
with open("input.txt", "r") as file:
    for line in file:
        calibration = ""
        for char in line:
            if char.isdigit():
                calibration += char
                break
        for char in reversed(line):
            if char.isdigit():
                calibration += char
                break
        print(calibration)
        calibration_total += int(calibration)
print(calibration_total)