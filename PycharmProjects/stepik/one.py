n = int(input())
l = []
for i in range(1, n+1):
    xy = input().split()
    l.append(xy)
one, two, free, four = 0, 0, 0, 0
for xy in l:
    if int(xy[0]) > 0 and int(xy[1]) > 0:
        one += 1
    if int(xy[0]) < 0 and int(xy[1]) > 0:
        two += 1
    if int(xy[0]) < 0 and int(xy[1]) < 0:
        free += 1
    if int(xy[0]) > 0 and int(xy[1]) < 0:
        four += 1
print(f"Первая четверть: {one}\nВторая четверть: {two}\nТретья четверть: {free}\nЧетвертая четверть: {four}")