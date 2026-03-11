N = int(input().strip())
moves_line = input().strip()

# 공백이 있으면 split, 없으면 문자열을 글자 단위로
moves = moves_line.split() if " " in moves_line else list(moves_line)

x, y = 1, 1

for m in moves:
    nx, ny = x, y
    if m == 'L':
        ny -= 1
    elif m == 'R':
        ny += 1
    elif m == 'U':
        nx -= 1
    elif m == 'D':
        nx += 1

    # 범위 안이면 이동 확정
    if 1 <= nx <= N and 1 <= ny <= N:
        x, y = nx, ny

print(x, y)