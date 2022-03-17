game_board = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'}

players = {'X': [], 'O': []}



def print_game_board():
    print("\n")
    print("\t  1  |  2  |  3")
    print("\t  {}  |  {}  |  {}".format(game_board[1], game_board[2], game_board[3]))
    print('\t_____|_____|_____')
    print("\t  4  |  5  |  6")
    print("\t  {}  |  {}  |  {}".format(game_board[4], game_board[5], game_board[6]))
    print('\t_____|_____|_____')
    print("\t  7  |  8  |  9")
    print("\t  {}  |  {}  |  {}".format(game_board[7], game_board[8], game_board[9]))
    print("\t     |     |")
    print("\n")

def win_check(sign):
    win_rules = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9])
    board_mask = set(players[sign])
    winner = bool([True for rule in win_rules if len(board_mask.intersection(rule)) == 3])
    return winner


def set_cell(cell, sign):
    game_board[cell] = sign
    players[sign].append(cell)


def start():
    sign = 'X'
    step = 1
    while True:
        print_game_board()
        try:
            print('Player ' , sign, ' turn. Choose cell [1-9] or type 0 for exit the game:')
            cell = int(input())
            if cell == 0:
                print('Thank you and good luck!')
                break
            else:
                if cell in range(1,10):
                    if game_board.get(cell) == '-':
                        set_cell(cell, sign)
                    else:
                        print('Cell is busy already. Choose another cell!')
                        continue
                    if win_check(sign):
                        print('Player ', sign, ' wins!')
                        break
                    else:
                        if step == 9:
                            print('Draw!!')
                            break
                        else:
                            step += 1
                    if sign == 'X':
                        sign = 'O'
                    else:
                        sign = 'X'
                else:
                    print("Wrong Input!!! Choose cell [1-9] or type 0 for exit the game:")
                    continue

        except ValueError:
                print("Wrong Input!!! Choose cell [1-9] or type 0 for exit the game:")
                continue



if __name__ == '__main__':
    print('Welcome to XO-game. Game play step by step, from X to O sign.')
    start()