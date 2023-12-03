f = open('Day3Data', 'r')

visited = set()


def expand_digit(data, x_initial, y_initial, direction: -1 or 1, N):
    x, y = x_initial, y_initial + direction
    global visited
    result = ""
    while (0 <= y < N) and data[x][y].isdigit():
        if (x, y) in visited:
            break
        visited.add((x, y))
        if direction == -1:
            result = data[x][y] + result
        else:
            result = result + data[x][y]
        y += direction
    return result


symbol_locs = []
data = []
for i, line in enumerate(f.readlines()):
    row = []
    for j, char in enumerate(line):
        if char == '\n':
            continue
        row.append(char)
        if (not char.isdigit()) and (char != '.'):
            visited.add((i, j))
            symbol_locs.append((i, j))
    data.append(row)

M = len(data[0])
N = len(data)

final_vals = []
sum = 0
for symbol_loc in symbol_locs:

    # look everywhere 1 away from symbol
    sx, sy = symbol_loc
    for x in range(sx - 1, sx + 2):
        for y in range(sy - 1, sy + 2):
            # skip center which is the symbol location
            if (x, y) == symbol_loc:
                continue

            # skip if outside boundary
            if x < 0 or x >= M:
                continue
            if y < 0 or y >= N:
                continue

            # keep track of visited
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # we gotta digit, expand to create new one
            if data[x][y].isdigit():
                new_number = expand_digit(data, x, y, -1, M) + data[x][y] + expand_digit(data, x, y, 1, N)
                final_vals.append(int(new_number))
                sum += final_vals[-1]

print(final_vals)
print(f"{sum=}")

f.close()