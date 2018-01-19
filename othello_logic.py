from collections import namedtuple


input_info = namedtuple('input_info', "row_num col_num first_turn top_left win_cond")
move_info = namedtuple('move_info', "row col color")


class overall_othello:   #all board manipulate each time you want to do something
    """the object that contains the othello game object and manipulates the functions that alter the game"""


    def __init__(self, input_info: 'input_info'):
        """takes the tuple input_info and stores the information within it in the class"""
        self.input_info = input_info
        self._topleft = input_info.top_left
        self._win_cond = input_info.win_cond
        self._maxrow = input_info.row_num
        self._maxcol = input_info.col_num
        self._firstturn = input_info.first_turn
        self._currentturn = input_info.first_turn



    def obtain_move_info(self, move_info: 'move_info'):
        """takes the tuple move_info and turns the move, row, and color within it into an item useable by the class"""
        self._row = move_info.row
        self._col = move_info.col
        self._currentturn = move_info.color


    def _black_white_initialize(self, board) -> list:
        """according to what color the user wants as top-left, arranges the central 4 tiles such that the specified color takes the top-left
        and bottom-right of the 4 tiles while the opposite colors fill the other 2 tiles and returns the board"""
        rowo = self._maxrow
        colo = self._maxcol
        boardo = board
        first = ''
        second = ''
        if self._topleft == 'B':
            first = 'B'
            second = 'W'
        elif self._topleft == 'W':
            first = 'W'
            second = 'B'
        boardo[int((rowo/2)-1)][int((colo/2)-1)] = first
        boardo[int((rowo/2)-1)][int(((colo/2)))] = second
        boardo[int((rowo/2))][int(colo/2)] = first
        boardo[int((rowo/2))][int((colo/2)-1)] = second
        return boardo


    def _new_board(self)-> list:   #this is different input from rest of the class
        """creates a new board object according to the specified number of rows and columns, and waht the player
        wanted tp be the color of the top left tile of the central 4 pieces"""
        board = []
        for x in range(self._maxrow): #creates rows
            board.append([])
        for x in board:
            for y in range(self._maxcol): #creates columns
                x.append('.')
        board = self._black_white_initialize(board)
        self._board = board

    def game_start(self):
        """at the very start of the game, a board will be created. Then the following objects will be printed:
        the counter for each color, the board, and the turn of the current turn"""
        self._new_board()
        self.print_color_count()
        self.print_board()
        self.turn_print()





    def _inside_board(self, row, col):
        """Checks whether the specified row and column are within the board"""
        return ((row >= 0) and (row< self._maxrow) and (col >= 0) and (col < self._maxcol))


    def _get_opposite_color(self, turn : str):
        """returns the opposite color. If B, then W will be returned. If W, then B will be returned"""
        if turn == 'B':
            other_color = 'W'
        else:
            other_color = 'B'
        return other_color





    def _flippable_list3(self, row: int, col: int):
        """Given a coordinate, this function will check in all 8 directions if there are tiles of the opposite color that can be flipped. If
        there are then a list containing the coordinates of these flippable tiles will be returned. If not, then an empty list will be returned"""
        poss_directions = [[0,1], [0,-1], [-1, -1], [-1, 0], [1, 1],[1, -1] ,[-1, 1], [1,0]]
        board = self._board
        turn = self._currentturn
        if self._inside_board(row, col) == False:
            return []
        elif board[row][col] != '.':
            return []
        other_color = self._get_opposite_color(turn)
        convert_coords = []

        for x in poss_directions:
            row_sum = row + x[0]
            col_sum = col + x[1]

            mini_list = []
            if self._inside_board(row_sum, col_sum) == False:
                continue
            try:
                while board[row_sum][col_sum] == other_color:
                    mini_list.append([row_sum, col_sum])
                    row_sum += x[0]
                    col_sum += x[1]
                    if self._inside_board(row_sum, col_sum) == False:
                        continue
            except:
                pass
            if self._inside_board(row_sum, col_sum) == False:
                continue
            elif board[row_sum][col_sum] == turn:
                convert_coords.extend(mini_list)
        return convert_coords







    def _change_turn(self):
        """switches the current turn color of the game object into the opposite color
    """
        self._currentturn = self._get_opposite_color(self._currentturn)
        return None

    def turn_print(self):
        """prints the current turn"""
        print("TURN: "+self._currentturn)

    def _valid_move(self):
        """checks whether a move is valid. Returns False if invalid and True if valid."""
        val_list = self._flippable_list3(self._row, self._col)

        if len(val_list) == 0:
            return False
        else:
            return True


    def _flip_the_colors(self):
        """for all the specified coordinates in a list of flippable coordinates, those tiles will be replaced by the opposite color"""
        flip_list = self._flippable_list3(self._row, self._col)
        for rowa, cola in flip_list:
            self._board[rowa][cola] = self._currentturn

    def _empty_moves(self):
        """returns a list of all tiles which have a blank space"""
        all_empty_moves = []
        for a in range(self._maxrow):
            for b in range(self._maxcol):
                if self._board[a][b] == '.':
                    all_empty_moves.append([a, b])
        return all_empty_moves



    def _check_for_validmoves(self):
        """returns a list of all the valid moves possible on the board"""
        all_empty_moves = self._empty_moves()
        valid_moves = []

        for x in all_empty_moves:
            if len(self._flippable_list3(x[0], x[1])) != 0:
                valid_moves.append([x[0], x[1]])
        return valid_moves




    def make_move(self):
        """the function called every time a move is made. If the user's move is not valid, then it will print INVALID and return an empty list.
        If the move is valid, VALID will be printed and all the tiles that should be flipped are flipped, the turn is changed, and the board is returned"""
        if self._valid_move() == False:
            print('INVALID')
            return []
        else:
            print('VALID')
            convert_color = self._get_opposite_color(self._currentturn)
            convert_coord = self._flippable_list3(self._row, self._col)
            self._flip_the_colors()
            self._board[self._row][self._col] = self._currentturn
            self._change_turn()
            return self._board

    def game_over(self):
        """checks whether a game is over, returns False if the game is over and returns True if the game is not over"""
        if self._check_for_validmoves() == []:
            return False
        else:
            return True

    def print_board(self):
        """uses a 2-D list and prints out a board object"""
        for x in self._board:
            big_word = ""
            for t in x:
                big_word += t[0] + ' '

            print(big_word)

    def _count_colors(self):
        """counts the total number of Black and White tiles on the board and returns a list of two objects, the first
        being the Black tile count and the second being the White tile count."""
        Btotal  = 0
        Wtotal = 0
        for x in self._board:
            for y in x:
                if y == 'B':
                    Btotal += 1
                elif y == 'W':
                    Wtotal += 1
        return [Btotal, Wtotal]

    def print_color_count(self):
        """print the total number of Black and White tiles on the board in the format  B:  Number  W: Number   """
        color_count = self._count_colors()
        format_str = str(color_count[0]) + "," + str(color_count[1])
        print("B: {0:2}  W: {1:2}".format(color_count[0], color_count[1]))



    def determine_winner(self):
        """depending on the inputted win conditin > or <, will print the winner of the game. If it is a tie, the winner will be specified as NONE"""
        two_sums = self._count_colors()
        if self._win_cond == '<':
            if two_sums[0] < two_sums[1]:
                print("WINNER: B")
            elif two_sums[1] < two_sums[0]:
                print ("WINNER: W")
            else:
                print("WINNER: NONE")
        elif self._win_cond  == '>':
            if two_sums[0] > two_sums[1]:
                print("WINNER: B")
            elif two_sums[1] > two_sums[0]:
                print ("WINNER: W")
            else:
                print("WINNER: NONE")

    def eachturn(self):
        """makes a move, prints the color count, and then will print the board"""
        self.make_move()
        self.print_color_count()
        self.print_board()
