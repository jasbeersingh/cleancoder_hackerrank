import sys


def solution(src, dest):
    moves = 0
    if src == dest:
        return moves
    src = get_coords(src)
    dest = get_coords(dest)
    locations = []
    moves = 0
    locations.append(get_possible_location_for_next_move(*src))
    while True:
        if dest in locations[moves]:
            return len(locations)
        moves += 1
        for loc in locations[moves-1]:
            try:
                locations[moves].extend(get_possible_location_for_next_move(*loc))
            except:
                locations.append(get_possible_location_for_next_move(*loc))
        locations[moves] = list(set(locations[moves]))


def get_possible_location_for_next_move(x,y):
    next_locs = []
    if is_location_in_board(x-2, y+1): next_locs.append((x-2, y+1))
    if is_location_in_board(x-2, y+1): next_locs.append((x-2, y-1))
    if is_location_in_board(x+2, y+1): next_locs.append((x+2, y+1))
    if is_location_in_board(x+2, y-1): next_locs.append((x+2, y-1))
    if is_location_in_board(x-1, y+2): next_locs.append((x-1, y+2))
    if is_location_in_board(x+1, y+2): next_locs.append((x+1, y+2))
    if is_location_in_board(x-1, y-2): next_locs.append((x-1, y-2))
    if is_location_in_board(x+1, y-2): next_locs.append((x+1, y-2))
    return next_locs


def is_location_in_board(x, y):
    if 0<= x < 8 and 0<=y <8:
        return True
    return False


def get_coords(loc):
    return divmod(loc, 8)


if __name__ == "__main__":
    for x in range(64):
        print("moves: ", solution(0,x))
        print("*" * 10)