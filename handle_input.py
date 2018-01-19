from collections import namedtuple
import othello_logic




def lines_of_input()->'input_info':
    """takes 5 lines of input and puts them into the tuple input_info which will be used to initialize the othello object"""

    row_num = input_1_row()    #simply gives error if you put in an invalid input and doesnt loop again, ask why
    col_num = input_2_col()
    first_turn = input_3_turn()
    top_left = input_4_top_left()
    win_cond = input_5_win()

    all_inputs = othello_logic.input_info(row_num, col_num, first_turn, top_left, win_cond)
    return all_inputs






def get_coord()->list:
    """takes the input in the format 'Y X' and puts them into a list, splitting them up and converting them into integers.
    The end result will be a list in the form of [Y, X]"""
    in_coord = input()
    coord = in_coord.split()
    for x in range(len(coord)):
        coord[x] = int(coord[x])-1
    return coord


def get_move_info(color: str)-> othello_logic.move_info:
    """calls get_coord to get the coordinate input from the user and puts the coordinates and the specified color
     into a player_move namedtuple which will then be used by the Othello game object"""
    coord = get_coord()
    player_move = othello_logic.move_info(coord[0], coord[1], color)
    return player_move




def input_1_row()->int:
    """the number of rows on the board. The number has to be an
    even number between 4 and 16 inclusive"""
    row_num = int(input())

    if row_num <4 or row_num>16:
        print("Please enter an even number between 4 and 16 inclusive")
        input_1_row()
    elif row_num%2 != 0:
        print("Please enter an even number between 4 and 16 inclusive")
        input_1_row()
    else:
        return row_num


def input_2_col()-> int:
    """the number of columns on the board. The number has to be an
    even number between 4 and 16 inclusive"""
    col_num = int(input())
    if col_num <4 or col_num>16:
        print("Please enter an even number between 4 and 16 inclusive")
        input_2_col()
    elif col_num%2 != 0:
        print("Please enter an even number between 4 and 16 inclusive")
        input_2_col()
    else:
        return col_num

def input_3_turn()-> str:
    """ which colored player will move first, (B)lack or (W)hite"""
    turn = input()
    #burn = turn
    if turn == 'B' or turn == 'W':  # why doesn't it work for W?
        return turn
    else:
        print("Please enter either B for black or W for white")
        input_3_turn()

def input_4_top_left()-> str:
    """ which colored player will be on the top-left position of the four center cells,
     (B)lack or (W)hite"""
    top_left = input()
    if top_left == 'B' or top_left == 'W':
        return top_left
    else:
        print("Please enter either B for black or W for white")
        input_4_top_left()

def input_5_win()-> str:
    """ the condition for winning, > for the player with the most discs,
    or < for the player with the fewest discs"""
    win_cond = input()
    if win_cond == '<' or win_cond == '>':
        return win_cond
    else:
        print("Please enter either B for black or W for white")
        input_5_win()


if __name__ == "__main__":
    print("FULL")
    all_inputs = lines_of_input()
    game = othello_logic.overall_othello(all_inputs)
    game.game_start()
    new_turn = get_move_info(game._currentturn)
    game.obtain_move_info(new_turn)
    while game._valid_move() == False:
        print("INVALID")
        new_turn = get_move_info(game._currentturn)
        game.obtain_move_info(new_turn)

    game.eachturn()

    while game.game_over():
        game.turn_print()
        new_turn = get_move_info(game._currentturn)
        game.obtain_move_info(new_turn)

        while not game._valid_move():
            print("INVALID")
            new_turn = get_move_info(game._currentturn)
            game.obtain_move_info(new_turn)

        game.eachturn()
    game.determine_winner()
