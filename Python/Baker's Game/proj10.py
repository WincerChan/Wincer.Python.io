

import cards  # This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:

    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game

"""


def valid_fnd_move(src_card, dest_card):
    """
    Add your function header here.
    """
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    if not dest_card:
        if (dest_card == [] and src_card[:-1] == 'A'):
            pass
        else:
            raise RuntimeError("ERROR: the card is not Ace")
    if dest_card:
        if (src_card[-1] == dest_card[-1] and ranks.index(src_card[:-1]) - ranks.index(dest_card[:-1]) == 1):
            pass
        elif (ranks.index(src_card[:-1]) - ranks.index(dest_card[:-1]) == -12):
            pass
        else:
            raise RuntimeError("ERROR: the move is not valid")


def valid_tab_move(src_card, dest_card):
    """
    Add your function header here.
    """
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    if dest_card == [] or (ranks.index(dest_card[:-1]) - ranks.index(src_card[:-1]) == 1 and dest_card[-1] == src_card[-1]):
        pass
    elif ranks.index(dest_card[:-1]) - ranks.index(src_card[:-1]) != 1:
        raise RuntimeError("ERROR:wrong rank")
    elif dest_card[-1] == src_card[-1]:
        raise RuntimeError("ERROR:wrong suit")


def tableau_to_cell(tab, cell):
    """
    Add your function header here.
    """
    if not cell:
        cell.append(tab[-1])
        tab.pop(-1)
    else:
        raise RuntimeError("ERROR: invalid command because cell is not empty.")


def tableau_to_foundation(tab, fnd):
    """
    Add your function header here.
    """
    try:
        if not fnd:
            valid_fnd_move(tab[-1], fnd)
            fnd.append(tab.pop(-1))
        else:
            valid_fnd_move(tab[-1], fnd[-1])
            fnd.append(tab.pop(-1))
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))


def tableau_to_tableau(tab1, tab2):
    """
    Add your function header here.
    """
    try:
        if not tab2:
            valid_tab_move(tab[-1], tab2)
        else:
            valid_tab_move(tab1[-1], tab2[-1])
        tab2.append(tab1.pop(-1))
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))


def cell_to_foundation(cell, fnd):
    """
    Add your function header here.
    """
    try:
        if fnd:
            valid_fnd_move(cell[0], fnd[-1])
        else:
            valid_fnd_move(cell[0], fnd)
        fnd.append(cell[-1])
        cell.remove(cell[0])
        # cells.append([])
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))


def cell_to_tableau(cell, tab):
    """
    Add your function header here.
    """
    try:
        if tab:
            valid_tab_move(cell, tab[-1])
        else:
            valid_tab_move(cell, tab)
        tab.append(cell[0])
        cells.remove(cell)
        # cells.append([])
    except RuntimeError:
        pass


def is_winner(foundations):
    """
    Add your function header here.
    """
    for x in range(4):
        try:
            if foundations[x][-1][0] != ['K']:
                return False
            return True
        except:
            pass


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """

    # You must use this deck for the entire game.
    # We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck()
    stock.shuffle()
    # The game piles are here, you must use these.
    cells = [[], [], [], []]  # list of 4 lists
    foundations = [[], [], [], []]  # list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []]  # list of 8 lists
    hand = stock.__str__().replace(' ', '')
    hand = hand.split(',')
    """ YOUR SETUP CODE GOES HERE """
    stock.shuffle()
    for x in range(len(hand)):
        tableaus[int(x % 8)].append(hand[x])
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Add your function header here.
    """
    # Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("    --1----2----3----4--  --1----2----3----4--")
    print("      ", end="")
    for card1 in cells:
        if card1:
            print("{:4s} ".format(str(card1[-1])), end="")
        else:
            print("{:4s} ".format(str(card1)), end="")
    print("  ", end="")
    for card2 in foundations:
        if card2:
            print("{:4s} ".format(str(card2[-1])), end="")
        else:
            print("{:4s} ".format(str(card2)), end="")
    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))

    print()
    # Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    for x in range(8):
        print("       ", end="")
        try:
            print("{:4s} ".format(str(tableaus[0][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[1][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[2][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[3][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[4][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[5][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[6][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        try:
            print("{:4s} ".format(str(tableaus[7][x])), end="")
        except:
            print("{:4s} ".format(''), end="")
        print()

# HERE IS THE MAIN BODY OF OUR CODE
print(RULES)
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU)
command = input("prompt :> ").strip().lower()
while command != 'q':
    try:
        if len(command) != 1:
            command = command.split(' ')
            if command[0] == 'tc':
                tableau_to_cell(tabs[int(command[1]) - 1],
                                cells[int(command[2]) - 1])
            if command[0] == 'tf':
                tableau_to_foundation(
                    tabs[int(command[1]) - 1], fnds[int(command[2]) - 1])
            if command[0] == 'tt':
                tableau_to_tableau(
                    tabs[int(command[1]) - 1], tabs[int(command[2]) - 1])
            if command[0] == 'cf':
                cell_to_foundation(
                    cells[int(command[1]) - 1], fnds[int(command[2]) - 1])
            if command[0] == 'ct':
                cell_to_tableau(cells[int(command[1]) - 1],
                                tabs[int(command[2]) - 1])
        elif command == 'r':
            print(RULES)
            cells, fnds, tabs = setup_game()
            print(MENU)
        elif command == 'h':
            print(MENU)
    # Any RuntimeError you raise lands here
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))
    if is_winner(fnds):
        print('You won the game!')
    display_game(cells, fnds, tabs)
    print()
    command = input("prompt :> ").strip().lower()
