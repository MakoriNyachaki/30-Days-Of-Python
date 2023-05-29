from __future__ import print_function

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort the list and find the min and max age

ages.sort()
print(f"Sort: {ages}\nMin: {min(ages)}\nMax: {max(ages)}")

# add the min and max age again to the list

ages.append(min(ages))
ages.append(max(ages))
print(f"Appended: {ages}")

# Find the median age (one middle item or two middle items divided by two)

median = 0
ages.sort()
length = len(ages)
if (length % 2):
    middle_index = length / 2
    second_index = middle_ndex + 1
    median = (ages[middle_index] + ages[second_index]) / 2
else:
    middle_index = (length // 2) + 1
    median = ages[middle_index]

print(f"Len: {len(ages)}\nSorted: {ages}\nMedian: {median}")

# Find the average age (sum of all items divided by their number)

total = 0
for age in ages:
    total += age
average = total / length
print(f"Average: {average}")

# Find the range of the ages (max minus min)

print(f"Range: {max(ages) - min(ages)}")

# Compare the value of (min - average) and (max - average), use abs() method

val_1 = abs(min(ages) - average)
val_2 = abs(max(ages) - average)

if val_1 > val_2:
    print(f"min - average: {val_1}")
else:
    print(f"max - average: {val_2}")
