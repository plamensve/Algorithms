def drawing_figure(n):
    if n == 0:
        return

    print('*' * n)
    drawing_figure(n - 1)
    print('#' * n)


num = int(input())
drawing_figure(num)
