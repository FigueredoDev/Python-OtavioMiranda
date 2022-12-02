from itertools import count

count_number = count(start=1, step=2)

for i in count_number:
    print(i)

    if i >= 10:
        break
