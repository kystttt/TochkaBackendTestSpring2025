
import sys

from collections import deque


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    robots = []
    key_count = 0
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '@':
                robots.append((i, j))
            elif 'a' <= data[i][j] <= 'z':
                key_count += 1
    initial_pos = tuple(robots)
    initial_mask = 0
    visited = {}
    queue = deque()

    queue.append((initial_pos, initial_mask, 0))
    visited[(initial_pos, initial_mask)] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        positions, mask, steps = queue.popleft()
        if bin(mask).count('1') == key_count:
            return steps
        for robot_idx in range(4):
            i, j = positions[robot_idx]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and data[ni][nj] != '#':
                    new_positions = list(positions)
                    new_positions[robot_idx] = (ni, nj)
                    new_positions = tuple(new_positions)
                    new_mask = mask
                    cell = data[ni][nj]
                    if 'a' <= cell <= 'z':
                        key_num = ord(cell) - ord('a')
                        new_mask = mask | (1 << key_num)
                    elif 'A' <= cell <= 'Z':
                        door_num = ord(cell) - ord('A')
                        if not (mask & (1 << door_num)):
                            continue
                    if (new_positions, new_mask) not in visited:
                        visited[(new_positions, new_mask)] = True
                        queue.append((new_positions, new_mask, steps + 1))
    return -1


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()