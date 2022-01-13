import random
import numpy as np


###########################################################################################
# fonction qui gère boolean et matrix de jeux
def lvl(nbr_clm, nbr_row):  # global donne l'accès à la fonction pour modifier les valeurs
    global boolean, matrix  # de variables qui sont en dehors de la fonction
    boolean = np.zeros((nbr_row, nbr_clm))  # fonction qui crée une matrice remplie de zéros
    liste = [i for i in range(nbr_row * nbr_clm // 2)] * 2
    random.shuffle(liste)  # fonction qui met la liste au hasard
    matrix = convert_to_matrix(liste, nbr_clm)s


###########################################################################################
# fonction qui convertit la liste en matrice
def convert_to_matrix(liste, nbr_clm):
    matrix = []
    for i in range(0, len(liste), nbr_clm):
        matrix.append(liste[i:i + nbr_clm])
    return matrix


###########################################################################################
# fonction booléenne qui masque la matrice et décider quelle valeur il va afficher

def display_hidden_matrix(boolean, matrix):
    print()
    for i in range(len(boolean)):
        for j in range(len(boolean[i])):
            if boolean[i][j] == 0:
                print('■', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()
    print()


###########################################################################################
# c'est juste une fonction qui guide l'utilisateur pour saisire une entrée valide
def matrix_guide(nbr_clm):
    print('\n---here is your guiding matrix---\n')
    print(' ', end=' ')
    for i in range(1, nbr_clm + 1):
        print(i, end=' ')
    print()
    for i in range(1, nbr_clm + 2):
        print(i, end=' ')
        for j in range(nbr_clm):
            print('■', end=' ')
        print()
    print('============')


###########################################################################################
# fonction qui decide quand le jeu sera terminer
def continue_playing():
    for i in range(len(boolean)):
        for j in range(len(boolean[i])):
            if boolean[i][j] == 0:
                return True
    return False


###########################################################################################
# fonction qui décide si l'utilisateur veut rejouer ou passer au niveau suivant ou quiter le jeu
def play_again():
    global end, nbr_clm, nbr_row
    if end == True:
        play = input('❋ type play to start the game❋ : ').lower().strip()
        if play == 'play':
            lvl(nbr_clm, nbr_row)
            end = False
            return True
        if play != 'play':
            print('\n --please insert a valide input thanks-- ')
            return play_again()

    else:
        for i in range(len(boolean)):
            for j in range(len(boolean[i])):
                boolean[i][j] = 0
        print('➤ 1 = replay the same lvl\n➤ 2 = pass to the next lvl\n➤ 3 = quit the game')
        again = input('insert your choice: ')
        if again == '1':
            nbr_clm = 3
            nbr_row = 4
            lvl(nbr_clm, nbr_row)
            return True
        elif again == '2':
            nbr_clm += 1
            nbr_row += 1
            lvl(nbr_clm, nbr_row)
            return True
        elif again == '3':
            print('\n----thanks see you later :)----')
            return False

        ###############################################################################


boolean = []
matrix = []
nbr_clm = 3
nbr_row = 4
first = True
end = True
print('\n-✦-hello wellcome to the memory game-✦-\n')
while play_again():
    while continue_playing():
        display_hidden_matrix(boolean, matrix)
        try:
            x = int(input('enter x: ')) - 1
            if x < 0:
                print('\n---the input is out of matrix range try again---\n')
                matrix_guide(nbr_clm)
                continue
        except ValueError:
            print('\n---invalid input on x---')
            continue  # s'assurer que l'utilisateur insère des entrées valides
        try:
            y = int(input('enter y: ')) - 1
            if y < 0:
                print('\n---the input is out of matrix range try again---\n')
                matrix_guide(nbr_clm)
                continue
        except ValueError:
            print('\n---invalid input on y---')
            continue
        try:
            if boolean[x][y] == 1:
                print('\n-----this card is already open-----\n')
                continue
        except IndexError:
            print('\n---the input is out of matrix range try again---\n')
            matrix_guide(nbr_clm)
            continue

        ###################################################################

        boolean[x][y] = 1
        if first == True:
            oldx = x
            oldy = y
            first = False
        else:  # comparing the old input with the new ones
            display_hidden_matrix(boolean, matrix)
            first = True
            if matrix[oldx][oldy] == matrix[x][y]: print('\n----yay you got a match :)----')
            if matrix[oldx][oldy] != matrix[x][y]:
                boolean[oldx][oldy] = 0
                boolean[x][y] = 0
                print('\n-----not match :(-----\n')

    print('\n-----congratulations u won the game-----\n')