# Made my Oliver Davis


#######;#S#...#;#.#.#.#;#...#.F;#######

#######;
#S#...#;
#.#.#.#;
#...#.F;
####### 

class mazePosition:
    def __init__(self,pos,path=None):
        self.pos = pos
        self.traceback = path
input_one = "5 7"
#input_two = "#######;#S#...#;#.#.#.#;#...#.F;#######"
input_two = "######;#S#..F;#...##;######"

dimensions = input_one.split(' ')
input_two = input_two.split(';')

input_two = [list(i) for i in input_two]

print(input_two)
searchables = []
step_count = 0
for y in enumerate(input_two):
    for x in enumerate(y[1]):
        index = (y[0],x[0])
        if input_two[index[0]][index[1]] == 'S': 
            searchables.append(mazePosition((index[0],index[1])))

path_to_start = []
count = 0
pathing_matrix = input_two
pathing = True
while pathing:
    print(len(searchables))
    for currentSearchIndex in searchables:
        index = currentSearchIndex.pos
        count+=1
        if index[0] < int(dimensions[0])-1:
            target=pathing_matrix[index[0]+1][index[1]]
            if target == '.':
                searchables.append(mazePosition((index[0]+1,index[1]),currentSearchIndex))
                pathing_matrix[index[0]+1][index[1]] = 'o'
            if target == 'F':
                path_to_start.append(currentSearchIndex.traceback)
        if index[1] < int(dimensions[1])-1:
            target=pathing_matrix[index[0]][index[1]+1]
            if target == '.':
                searchables.append(mazePosition((index[0],index[1]+1),currentSearchIndex))
                pathing_matrix[index[0]][index[1]+1] = 'o'
            if target == 'F':
                path_to_start.append(currentSearchIndex.traceback)
        if index[1] >= 0:
            target=pathing_matrix[index[0]][index[1]-1]
            if target == '.':
                searchables.append(mazePosition((index[0],index[1]-1),currentSearchIndex))
                pathing_matrix[index[0]][index[1]-1] = 'o'
            if target == 'F':
                path_to_start.append(currentSearchIndex.traceback)
        if index[0] >= 0:
            target = pathing_matrix[index[0]-1][index[1]]
            if target == '.':
                searchables.append(mazePosition((index[0]-1,index[1]),currentSearchIndex))
                pathing_matrix[index[0]-1][index[1]] = 'o'
            if target == 'F':
                path_to_start.append(currentSearchIndex.traceback)
    print(pathing_matrix)
    break
print(path_to_start)
backtracking = True
path = []
current_iteration_node = path_to_start[0]
while backtracking:
    if current_iteration_node != None:
        path.append(current_iteration_node.pos)
        print(current_iteration_node.pos)
        current_iteration_node = current_iteration_node.traceback
    else: backtracking = False
print(path)
print(len(path)+1)