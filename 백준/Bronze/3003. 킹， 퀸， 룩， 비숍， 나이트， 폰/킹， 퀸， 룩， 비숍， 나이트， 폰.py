black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))

changing = [str(black[i] - white[i]) for i in range(len(black)]
print(' '.join(changing))
