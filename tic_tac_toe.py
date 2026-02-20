"""
Task - 13: Create a Tic-Tac-Toe Game in Python.
1. You should be able to play with two players.
2. You should be able to play against computer.
After you complete simple game implement it in a way that computer never loses.
"""

# import random module to generate random moves for computer
# from random import choice

# define a tictactoe class to manage game logic
class TicTacToe:

    # constructor to initialize the game board
    def __init__(self):
        self.board = [" " for i in range(9)]

    # define function to display the game board
    def display_board(self):
        print("\nBoard:")
        
        for i in range(0,9,3):
            print(self.board[i], "|", self.board[i+1], "|", self.board[i+2])
            
            if i < 6:
                print("----------")        

    # define function to make a move on the board
    def make_move(self, position, symbol):
        if position >= 0 and position < 9 and self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False
    
    # define function to play the game
    def play_game(self, player1, player2, vs_computer=False):
        current_player = player1

        while True:
            self.display_board()
    
            if vs_computer and isinstance(current_player, Computer):
                move = current_player.get_computer_move(self.board)
                print(f"\nComputer chooses position {move}")
            else:
                move = current_player.get_move()
    
            if not self.make_move(move, current_player.symbol):
                print("\nPosition already taken.")
                continue
    
            if self.check_winner(current_player.symbol):
                self.display_board()

                if not isinstance(current_player, Computer):
                    print(f"\n{current_player.name} Wins the Game!") 
                else:
                    print("\nComputer Wins the Game!")
                break
    
            if self.is_draw():
                self.display_board()
                print("\nGame is a Draw!")
                break

            if current_player == player1:
                current_player = player2 
            else:
                current_player = player1

    # define function to check if a player has won the game or not
    def check_winner(self, symbol):
        win_positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for combo in win_positions:
           if all(self.board[i] == symbol for i in combo):
                return True
        
        return False

    # define function to check if the game is a drawn or not
    def is_draw(self):
        if " " not in self.board:
            return True
        return False

# define Player class to manage player details
class Player:

    # constructor to initialize player details
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # define function to get player's move
    def get_move(self):
        while True:
            try:
                move = int(input(f"\n{self.name} ({self.symbol}) - Enter position (0-8): "))
                
                if move >= 0 and move <= 8:
                    return move
                else:
                    print("\nEnter number between (0-8).")
            except ValueError:
                print("\nValueError: Enter a valid integer input only.")
            except Exception:
                print("\nUnknownError Occurred.")

# define Computer class to manage computer's move
class Computer:

    # constructor to initialize computer's symbol
    def __init__(self, symbol):
        self.symbol = symbol

    # define function to get computer's move
    def get_computer_move(self, board):
        # simple game logic to make computer's move
        # available_moves = [i for i in range(9) if board[i] == " "]
        # return choice(available_moves)

        # logic to make computer's move so that it never loses
        if self.symbol == 'o':
            player_symbol = 'x'
        else:
            player_symbol = 'o'

        win_positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for combo in win_positions:
            positions = [board[i] for i in combo]
            if positions.count(self.symbol) == 2 and positions.count(" ") == 1:
                return combo[positions.index(" ")]

        for combo in win_positions:
            positions = [board[i] for i in combo]
            if positions.count(player_symbol) == 2 and positions.count(" ") == 1:
                return combo[positions.index(" ")]
            
        if board[4] == " ":
            return 4

        for i in [0,2,6,8]:
            if board[i] == " ":
                return i

        for i in [1,3,5,7]:
            if board[i] == " ":
                return i
       
# define menu function to interact with user
def menu():
    print("\nWelcome to Tic-Tac-Toe Game!")
    
    game_symbol = ["o", "x"]

    while True:
        print("\n1. Play with Two Players")
        print("2. Play against Computer")
        print("3. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                player_1_name = input("\nEnter Player-1 Name: ")
                player_2_name = input("\nEnter Player-2 Name: ")

                player_1_symbol = input(f"\nEnter Symbol for {player_1_name} (o/x): ")

                if player_1_symbol not in game_symbol:
                    print("\nEnter valid game symbol.")
                    continue

                if player_1_symbol == 'o':
                    player_2_symbol = 'x'
                else:
                    player_2_symbol = 'o'

                player1 = Player(player_1_name, player_1_symbol)
                player2 = Player(player_2_name, player_2_symbol)

                tictactoe = TicTacToe()
                tictactoe.play_game(player1, player2)
            elif choice == 2:
                player_name = input("\nEnter Player Name: ")
                player_symbol = input(f"\nEnter Symbol for {player_name} (o/x): ")

                if player_symbol not in game_symbol:
                    print("\nEnter valid game symbol.")
                    continue

                if player_symbol == 'o':
                    computer_symbol = 'x'
                else:
                    computer_symbol = 'o'

                player = Player(player_name, player_symbol)
                computer = Computer(computer_symbol)

                tictactoe = TicTacToe()
                tictactoe.play_game(player, computer, vs_computer=True)
            elif choice == 3:
                print("\nYou selected Exit.\nThank You!")
                break
            else:
                print("\nPlease enter a valid choice (1-3).")
        except ValueError:
            print("\nValueError: Please enter a valid choice (1-3).")
        except Exception:
            print("\nUnknownError Occurred.")

# start the tic-tac-toe game
menu()