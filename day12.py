#--- Part One ---

data = []
direction = ('E', 'S', 'W', 'N')
facing = 'E'
pos = [0, 0,]


def man_dist(position):
    return (abs(position[0]) + abs(position[1]))


def move(commd, steps):
    curr_E_W = pos[0]
    curr_N_S = pos[1]
    
    if commd == 'E':
        pos[0] = curr_E_W + steps
    elif commd == 'W':
        pos[0] = curr_E_W - steps
    elif commd == 'S':
        pos[1] = curr_N_S - steps
    elif commd == 'N':
        pos[1] = curr_N_S + steps


read_file = open('index.txt', 'r', encoding='utf-8')
clean_file = list(map(str,read_file.read().split('\n')))
for item in clean_file:
    a = item[0]
    rest = int(item[1:])
    data.append([a,rest])
for command, stepping in data:
    if command == 'L' or command == 'R':
        idx = int(stepping/90)
        curr_dir = direction.index(facing)
        if command == 'L':
            idx_result = curr_dir - idx
            facing = direction[idx_result]
        elif command == 'R':
            if (curr_dir + idx) > 3:
                idx_result = (curr_dir + idx - 4)
            else:
                idx_result = (curr_dir + idx)
            facing = direction[idx_result]
    else:
        if command == 'F':
            move(facing, stepping)
        else:
            move(command, stepping)

print(f'The manhatten distance is equal to {man_dist(pos)}')

