import math

def pos_to_coords(pos):
    """
    Converts a position [0..63] into a pair of coord (x, y)
    """
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x, y)


def coords_to_pos(x, y):
    """
    Converts a pair of coord (x, y) into a position [0..63]
    """
    return x + y * 8


def get_possible_moves(x, y):
    """
    Returns a list of valid coordinates for next move
    """
    all_moves = []
    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    valid_moves = []
    for (x, y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x, y))

    return valid_moves


def solution(src, dest):
    if src == dest:
        return 0

    # Get the current and target tile
    src_x, src_y = pos_to_coords(src)
    dst_x, dst_y = pos_to_coords(dest)
    
    # Create a queue with all the positions I need to check
    queue = get_possible_moves(src_x, src_y)
    depth_queue = []

    # the depth, or solution
    depth = 0 

    while True:
        depth += 1

        # We check each move available at this depth
        for move in queue:
            # Let's see if we arrived to destination
            if move[0] == dst_x and move[1] == dst_y:
                return depth

            # we build the next depth queue, which will replace the queue after we tested them all
            # this is necessary to test one level at a time
            depth_queue.extend(get_possible_moves(move[0], move[1]))

        queue = depth_queue
        depth_queue = []

# print(solution(19, 36))

'''

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

'''
