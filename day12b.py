#--- Part Two ---

data = []
direction = ('E', 'S', 'W', 'N')
wayp = [10, 1]
pos = [0, 0]


def man_dist(position):
    return (abs(position[0]) + abs(position[1]))


def move(commd, steps):
    curr_wayp_E_W = wayp[0]
    curr_wayp_N_S = wayp[1]
    curr_E_W = pos[0]
    curr_N_S = pos[1]    
    if commd == 'E':
        wayp[0] = curr_wayp_E_W + steps
    elif commd == 'W':
        wayp[0] = curr_wayp_E_W - steps
    elif commd == 'S':
        wayp[1] = curr_wayp_N_S - steps
    elif commd == 'N':
        wayp[1] = curr_wayp_N_S + steps
    elif commd == 'F':
        pos[0] = curr_E_W + (curr_wayp_E_W * steps)
        pos[1] = curr_N_S + (curr_wayp_N_S * steps)
 

read_file = open('input.txt', 'r', encoding='utf-8')
clean_file = list(map(str,read_file.read().split('\n')))
for item in clean_file:
    a = item[0]
    rest = int(item[1:])
    data.append([a,rest])
for command, stepping in data:
    if command == 'L' or command == 'R':
        idx = int(stepping/90)
        for count in range(idx):
            curr_E_W = wayp[0]
            curr_N_S = wayp[1]
            if command == 'L':
                wayp[0] = curr_N_S - (curr_N_S * 2)
                wayp[1] = curr_E_W
            elif command == 'R':
                wayp[0] = curr_N_S
                wayp[1] = curr_E_W - (curr_E_W * 2)
    else:
        move(command, stepping)

print(f'The manhatten distance is equal to {man_dist(pos)}')
