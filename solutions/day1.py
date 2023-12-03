import re

with open("data/day1input.txt") as file:
    data = file.readlines()
    repldict_edge = {'zerone':'01', 'oneight':'18','twone':'21','threeight':'38','fiveight':'58', 'sevenine':'79','eightwo':'82', 'eighthree':'83','nineight':'98'}
    repldict = {'zero':'0', 'one':'1' ,'two':'2','three':'3','four':'4', 'five':'5' ,'six':'6','seven':'7', 'eight':'8', 'nine':'9'}
    # Part 1
    calibration_sum_one = 0
    calibration_sum_two = 0
    for entry in data:
        no_chars_one = re.sub(r'[^0-9]', '', entry)
        calibration_sum_one += int(no_chars_one[0]+no_chars_one[len(no_chars_one)-1])

        entry_two = entry
        for key in repldict_edge.keys():
            entry_two = entry_two.lower().replace(key,repldict_edge[key])
        for key in repldict.keys():
            entry_two = entry_two.lower().replace(key,repldict[key])
        
        no_chars_two = re.sub(r'[^0-9]', '', entry_two)
        print(entry, no_chars_two, no_chars_two[0], no_chars_two[len(no_chars_two)-1])
        calibration_sum_two += int(no_chars_two[0]+no_chars_two[len(no_chars_two)-1])
        
    print("Calibration Sum Part 1: ",calibration_sum_one)
    print("Calibration Sum Part 2: ",calibration_sum_two)

    