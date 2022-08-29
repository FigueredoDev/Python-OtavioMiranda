from itertools import count

contador = count(start=1, step=2)

for i in contador:
    print(i)

    if i >= 10:
        break
