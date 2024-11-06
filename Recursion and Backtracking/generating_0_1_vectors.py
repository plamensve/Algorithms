def gen01(idx, vector):
    counter = 0
    if idx >= len(vector):
        print(*vector, sep='')
        return 1

    for num in range(2):
        vector[idx] = num
        counter += gen01(idx + 1, vector)

    return counter


n = int(input())
vector = [0] * n
total_combinations = gen01(0, vector)
print("Total combinations:", total_combinations)
