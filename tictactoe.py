class TicTacToe:
    def __init__(self):
        self.plateau = {
            "A" : ["▢", "▢", "▢"],
            "B" : ["▢", "▢", "▢"],
            "C" : ["▢", "▢", "▢"]
        }

    def display_board(self):
            print("----PLATEAU-----")
            print(self.plateau["A"])
            print(self.plateau["B"])
            print(self.plateau["C"])

    def put_symbol(self, square, symbol):
        ligne, colonne = square

        if ligne not in ["A", "B", "C"] or colonne not in [0, 1, 2]:
            raise SquareNotFoundError(square)

        if self.plateau[ligne][colonne] != "▢":
            raise SquareNotEmptyError(square)

        self.plateau[ligne][colonne] = symbol

    def game_finished(self):
        for ligne, colonne in self.plateau.items():
            if self.plateau[ligne][0] == self.plateau[ligne][1] == self.plateau[ligne][2] != "▢":
                return True
        for i in range(3):
            if self.plateau["A"][i] == self.plateau["B"][i] == self.plateau["C"][i] != "▢":
                return True
        if self.plateau["A"][0] == self.plateau["B"][1] == self.plateau["C"][2] != "▢":
            return True
        if self.plateau["A"][2] == self.plateau["B"][1] == self.plateau["C"][0] != "▢":
                return True
        for ligne in self.plateau:
            if "▢" in self.plateau[ligne]:
                return False

        return False

class SquareNotEmptyError(Exception):
    def __init__(self, square):
        self.square = square

    def __str__(self):
        ligne, colonne = self.square
        return f"La case {ligne}{colonne + 1} est déjà occupée"

class SquareNotFoundError(Exception):
    def __init__(self, square):
        self.square = square

    def __str__(self):
        ligne, colonne = self.square
        return f"La case choisie n'existe pas : {ligne}{colonne + 1}"
    

partie = TicTacToe()
partie.display_board()

while partie.game_finished() == False:

    while True:
        x_horizontal = input("[Joueur X] Choisissez une case :\nHorizontal (A,B,C): ")
        x_vertical = int(input("Vertical (1,2,3): "))

        try:
            partie.put_symbol((x_horizontal, x_vertical - 1), "X")
            break
        except SquareNotFoundError as e:
            print(e)
        except SquareNotEmptyError as e:
            print(e)

    partie.display_board()

    while True:
        o_horizontal = input("[Joueur O] Choisissez une case :\nHorizontal (A,B,C): ")
        o_vertical = int(input("Vertical (1,2,3): "))

        try:
            partie.put_symbol((o_horizontal, o_vertical - 1), "O")
            break
        except SquareNotFoundError as e:
            print(e)
        except SquareNotEmptyError as e:
            print(e)

    partie.display_board()

print("\n")
print("GAME OVER")