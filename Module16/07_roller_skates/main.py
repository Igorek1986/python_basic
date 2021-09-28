skates_size = [41, 40, 39, 42]
foot_size = [42, 41, 42]
count = 0
for i in skates_size:
    for i2 in foot_size:
        if i == i2:
            count += 1

print(count)