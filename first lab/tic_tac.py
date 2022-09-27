class TicTacGame:

    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]

    def __init__(self):
        self.maps = [i for i in range (0,10)]

    """    
    maps = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]
    """

    def show_board(self):
        print('_____________')
        print('|', self.maps[0], '|', self.maps[1], '|', self.maps[2],'|')
        print('-------------')
        print('|', self.maps[3], '|', self.maps[4], '|', self.maps[5],'|')
        print('-------------')
        print('|', self.maps[6], '|', self.maps[7], '|', self.maps[8],'|')
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯')


    def do_step(self, step,symbol):
        self.maps[self.maps.index(step)] = symbol


    def validate_input(self, cell, player: int):
        try:
            cell = int(cell)
        except ValueError:
            print("Введите целое натуральное число: ")
            #self.validate_input(player)
            return False
        else:
            if(not(1<=cell<=9)):
                print('Введите число от 1 до 9: ')
                #self.validate_input(player)
                return False
        symbol = 'X' if player==1 else 'O'
        if str(self.maps[cell-1]) not in 'XO':
            self.maps[cell-1] = symbol
        else:
            print('Выберите свободную ячейку ')
            return False
        return True


    def check_winner(self, maps):
        win = ""
        for i in self.wins:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "X"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "O"            
        return win


    def start_game(self):
        game = True #когда игра закончилась - False
        p = True    #True - 1 игрок, False - 2 игрок
        count = 0

        #maps = [1, 2, 3,
        #        4, 5, 6,
        #        7, 8, 9]

        while game and count < 9:
            count+=1
            self.show_board()
            non_valid_input = True
            x = 1 if p == True else 2
            print('Ходит игрок:', x)
            while non_valid_input:
                if p == True: #X
                    #print('Ходит игрок 1: ')
                    cell = input()
                    non_valid_input = not(self.validate_input(cell, 1))
                else: #O
                    #print('Ходит игрок 2: ')
                    cell = input()
                    non_valid_input = not(self.validate_input(cell, 2))

            win = self.check_winner(self.maps)
            if win != "":
                game = False
            else:
                game = True
            p = not(p)               
        self.show_board()
        if count == 9:
            print("Ничья!")
        else:
            print("Победил ", win, '!', sep = '')

if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()