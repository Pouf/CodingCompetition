# Your objective is to write a program capable of predicting the route Indy
# will take on his way down a tunnel. Indy is not in danger of getting trapped
# in this first mission.


w, h = [int(i) for i in input().split()]
grid = [input().split() for i in range(h)]
exit = input()

while 1:
    xi, yi, [w, *_] = input().split()
    xi, yi = int(xi), int(yi)
    cell = grid[yi][xi]
    D, L, R = [1, 0], [0, -1], [0, 1]
    y, x = {1: D,
            2: {'R': L, 'L': R}.get(w),
            3: D,
            4: {'T': L, 'R': D}.get(w),
            5: {'T': R, 'L': D}.get(w),
            6: {'T': L if xi else R, 'R': L, 'L': R}.get(w),
            7: D,
            8: D,
            9: D,
            10: L,
            11: R,
            12: D,
            13: D}[int(cell)]

    print(xi + x, yi + y)
