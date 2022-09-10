player1_characters = {
    "P1": False,                #False means character not available
    "P2": False,
    "P3": False,
    "P4": False,
    "P5": False,
    "H1": False
}

player2_characters = {
    "P1": False,
    "P2": False,
    "P3": False,
    "P4": False,
    "P5": False,
    "H1": False
}

commands = ["F", "H1:F"]

grid = {
    "11": "-", "12": "-", "13": "-", "14": "-", "15": "-",
    "21": "-", "22": "-", "23": "-", "24": "-", "25": "-",
    "31": "-", "32": "-", "33": "-", "34": "-", "35": "-",
    "41": "-", "42": "-", "43": "-", "44": "-", "45": "-",
    "51": "-", "52": "-", "53": "-", "54": "-", "55": "-"
}


def print_grid():
    print("Current Grid: ")
    print(f"{grid['51']} {grid['52']} {grid['53']} {grid['54']} {grid['55']}")
    print(f"{grid['41']} {grid['42']} {grid['43']} {grid['44']} {grid['45']}")
    print(f"{grid['31']} {grid['32']} {grid['33']} {grid['34']} {grid['35']}")
    print(f"{grid['21']} {grid['22']} {grid['23']} {grid['24']} {grid['25']}")
    print(f"{grid['11']} {grid['12']} {grid['13']} {grid['14']} {grid['15']}")


player1_characters_pos = dict()
player2_characters_pos = dict()


def characters_input():
    A = input("Player1 input: ")
    A_input = A.split(" ")
    for character in A_input:
        if player1_characters[character] or character not in player1_characters.keys():
            raise Exception(f"Invalid character input: {character}")
        if len(set(A_input)) != 5:
            raise Exception(f"Duplicate characters in input")

    B = input("Player2 input: ")
    B_input = B.split(" ")
    for character in B_input:
        if player2_characters[character] or character not in player2_characters.keys():
            raise Exception(f"Invalid character input: {character}")
        if len(set(A_input)) != 5:
            raise Exception(f"Duplicate characters in input")

    grid['11'] = "A-"+A_input[0]
    player1_characters[A_input[0]] = True
    player1_characters_pos[A_input[0]] = [1, 1]
    grid['12'] = "A-"+A_input[1]
    player1_characters[A_input[1]] = True
    player1_characters_pos[A_input[1]] = [1, 2]
    grid['13'] = "A-"+A_input[2]
    player1_characters[A_input[2]] = True
    player1_characters_pos[A_input[2]] = [1, 3]
    grid['14'] = "A-"+A_input[3]
    player1_characters[A_input[3]] = True
    player1_characters_pos[A_input[3]] = [1, 4]
    grid['15'] = "A-"+A_input[4]
    player1_characters[A_input[4]] = True
    player1_characters_pos[A_input[4]] = [1, 5]

    grid['51'] = "B-"+B_input[0]
    player2_characters[B_input[0]] = True
    player2_characters_pos[B_input[0]] = [5, 1]
    grid['52'] = "B-"+B_input[1]
    player2_characters[B_input[1]] = True
    player2_characters_pos[B_input[1]] = [5, 2]
    grid['53'] = "B-"+B_input[2]
    player2_characters[B_input[2]] = True
    player2_characters_pos[B_input[2]] = [5, 3]
    grid['54'] = "B-"+B_input[3]
    player2_characters[B_input[3]] = True
    player2_characters_pos[B_input[3]] = [5, 4]
    grid['55'] = "B-"+B_input[4]
    player2_characters[B_input[4]] = True
    player2_characters_pos[B_input[4]] = [5, 5]

    print_grid()


characters_input()


def valid_move(player, character, command):
    if command == 'F' and player == 'A' and player1_characters_pos.get(character)[0] == 5 and character in ['P1', 'P2', 'P3', 'P4', 'P5']:
        print("Invalid Move")
        return False
    elif command == 'F' and player == 'B' and player2_characters_pos.get(character)[0] == 1 and character in ['P1', 'P2', 'P3', 'P4', 'P5']:
        print("Invalid Move")
        return False
    else:
        return True


def move(player, character, command):
    if command == 'F' and player == 'A' and character in ['P1', 'P2', 'P3', 'P4', 'P5']:
        char_pos = player1_characters_pos.get(character)
        key1 = str(char_pos[0]) + str(char_pos[1])
        key2 = str(char_pos[0]+1)+str(char_pos[1])
        player1_characters_pos[character] = [char_pos[0]+1, char_pos[1]]
        grid[key1] = '-'
        grid[key2] = 'A-'+character
        if grid[key2][0] == 'A':
            print("Friend troop already present")
        elif grid[key2][0] == 'B':
            player1_characters_pos[grid[key2][2:]] = None
            player1_characters[grid[key2][2:]] = False
            grid[key2] = 'A-'+character
        else:
            grid[key2] = 'A-' + character
    elif command == 'F' and player == 'B' and character in ['P1', 'P2', 'P3', 'P4', 'P5']:
        char_pos = player2_characters_pos.get(character)
        key1 = str(char_pos[0]) + str(char_pos[1])
        key2 = str(char_pos[0]-1)+str(char_pos[1])
        player2_characters_pos[character] = [char_pos[0] - 1, char_pos[1]]
        grid[key1] = '-'
        if grid[key2][0] == 'B':
            print("Friend troop already present")
        elif grid[key2][0] == 'A':
            player1_characters_pos[grid[key2][2:]] = None
            player1_characters[grid[key2][2:]] = False
            grid[key2] = 'B-'+character
        else:
            grid[key2] = 'B-' + character
    elif command == 'F' and player == 'A' and character == 'H1':
        char_pos = player1_characters_pos.get(character)
        key1 = str(char_pos[0]) + str(char_pos[1])
        key2 = str(char_pos[0]+2)+str(char_pos[1])
        player1_characters_pos[character] = [char_pos[0]+2, char_pos[1]]
        grid[key1] = '-'
        if grid[key2][0] == 'A':
            print("Friend troop already present")
        elif grid[key2][0] == 'B':
            del player1_characters_pos[grid[key2][2:]]
            player1_characters[grid[key2][2:]] = False
            grid[key2] = 'A-'+character
        else:
            grid[key2] = 'A-' + character
    elif command == 'F' and player == 'B' and character == 'H1':
        char_pos = player2_characters_pos.get(character)
        key1 = str(char_pos[0]) + str(char_pos[1])
        key2 = str(char_pos[0]-2)+str(char_pos[1])
        player2_characters_pos[character] = [char_pos[0]-2, char_pos[1]]
        grid[key1] = '-'
        if grid[key2][0] == 'B':
            print("Friend troop already present")
        elif grid[key2][0] == 'A':
            del player1_characters_pos[grid[key2][2:]]
            player1_characters[grid[key2][2:]] = False
            grid[key2] = 'B-'+character
        else:
            grid[key2] = 'B-' + character


def check_winner():
    countA = 0
    countB = 0

    for key in player1_characters_pos.keys():
        if player1_characters_pos[key]:
            countA += 1
    for key in player2_characters_pos.keys():
        if player2_characters_pos[key]:
            countB += 1

    if countA == 0:
        print("Player B wins")
        return True
    elif countB == 0:
        print("Player A wins")
        return True
    else:
        return False


while not check_winner():
    A_move = input("Player A's move: ").split(":")
    if player1_characters[A_move[0]]:
        command = A_move[1]
        if command in commands and valid_move(player='A', character=A_move[0], command=command):
            move(player='A', character=A_move[0], command=command)
            print_grid()
    else:
        print("Invalid character")

    B_move = input("Player B's move: ").split(":")
    if player2_characters[B_move[0]]:
        command = B_move[1]
        if command in commands and valid_move(player='B', character=B_move[0], command=command):
            move(player='B', character=B_move[0], command=command)
            print_grid()
    else:
        print("Invalid character")