def read_lab():
    row = int(input())
    col = int(input())
    lab = []

    for x in range(row):
        lab.append(list(input()))

    return lab

print(read_lab())