x = input().split()
row = int(x[0])
col = int(x[1])       
grid = input().split(';')

# TwoD array of true/false for corresponding cells to the grid
visited = []
for i in range(row):
    row_list = []
    for j in range(col):
        row_list.append(False)
    visited.append(row_list)

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def find_area(start_r, start_c):
    pos = [(start_r, start_c)]
    visited[start_r][start_c] = True
    size = 0
    while pos:
        cr, cc = pos.pop()
        size += 1
        for dr, dc in directions:
            newr, newc = cr + dr, cc + dc
            if 0 <= newr < row and 0 <= newc < col:
                if not visited[newr][newc] and grid[newr][newc] == 'G':
                    visited[newr][newc] = True
                    pos.append((newr, newc))
    return size

max_grass = 0
area = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == 'G' and not visited[i][j]:
            area = find_area(i, j)
            if area > max_grass:
                max_grass = area

print(max_grass)

'''
Examples: 
6 8
GGWWRRRG;GWWWGRRG;GGGGGWRG;WRWWGWRG;WWWWGGGG;RRGGGGGG
24

5 5
WWWWW;WGGGW;WGWGW;WGGGW;WWWWW
8

4 4
WWWW;WRRW;WRRW;WWWW
0
'''