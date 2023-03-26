import sys
class Keyfileempty(Exception):
    pass
class Inputfileempty(Exception):
    pass

try:
    operation = sys.argv[1]
    f3 = open(sys.argv[3], "r")
    f4 = open(sys.argv[2],"r")

    key_error = [i.strip("\n").split(",") for i in f4.readlines()]

    matrix_letter2 =[i.strip("\n") for i in f3.readlines()]
    matrix_letter = ""
    for i in matrix_letter2:
        matrix_letter += str(i)
    if len(sys.argv) < 5 or len(sys.argv) > 5:
        raise IndexError
    elif len(key_error) == 0 :
        raise Keyfileempty
    elif len(matrix_letter2) == 0:
        raise Inputfileempty

    if sys.argv[2] == "plain_input.txt":
        encoding_dictionary = {"A": 1, "a": 1, "B": 2, "b": 2, "C": 3, "c": 3, "D": 4, "d": 4, "E": 5, "e": 5, "F": 6,"f": 6, "G": 7, "g": 7, "H": 8, "h": 8, "I": 9, "i": 9, "J": 10, "j": 10, "K": 11, "k": 11,"L": 12, "l": 12, "M": 13, "m": 13, "N": 14, "n": 14, "O": 15, "o": 15, "P": 16, "p": 16,"Q": 17, "q": 17, "R": 18, "r": 18, "S": 19, "s": 19, "T": 20, "t": 20, "U": 21, "u": 21,"V": 22, "v": 22, "W": 23, "w": 23, "X": 24, "x": 24, "Y": 25, "y": 25, "Z": 26, "z": 26," ": 27}
        error_try = [encoding_dictionary[matrix_letter[a:a + 1]] for a in range(0, len(matrix_letter))]
    elif sys.argv[2] == "ciphertext.txt" :
        decoding_dictionary = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",12: "L", 13: "M", 14: "N", 15: "0", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: " ",0:"k"}
        error_try = [decoding_dictionary[matrix_letter[a:a + 1]] for a in range(0, len(matrix_letter))]

except IndexError:
    print("Parameter number error")
    exit()
except IOError:
    if operation != "dec" and operation != "enc":
        print(sys.argv[1])
        print("Undefined parameter error")
        exit()
    elif sys.argv[3] != "plain_input.txt" and sys.argv[3][-3:] == "txt" and sys.argv[3] != "ciphertext.txt":
        print("Input file not found error")
        exit()
    elif sys.argv[3][-3:] != "txt":
        print("The input file could not be read error")
        exit()
    elif sys.argv[32] != "key.txt" and sys.argv[3][-3:] == "txt":
        print("Key file not found error")
        exit()
    elif sys.argv[2][-3:] != "txt":
        print("Key file could not be read error")
        exit()
except Keyfileempty:
    print("Key file is empty error")
    exit()
except Inputfileempty:
    print("Input file is empty error")
    exit()
except KeyError:

    print("Invalid character in key file")
    exit()
except ValueError:
    print("Invalid character in input file")
    exit()


if sys.argv[3][-15:] == "plain_input.txt":
    f = open(sys.argv[3],"r")
    f2 = open(sys.argv[2],"r")
    f3 = open(sys.argv[4],"w")
    matrix_letter2 =[i.strip("\n") for i in f.readlines()]
    matrix_letter = ""
    for i in matrix_letter2:
        matrix_letter += str(i)


    key_matrix = [i.strip("\n").split(",") for i in f2.readlines()]

    matrix2 = []
    for i in range(len(key_matrix)):
        for x in range(len(key_matrix[0])):
            matrix2.append(int(key_matrix[i][x]))
    matrix1 = [matrix2[a:a+len(key_matrix)] for a in range(0, len(matrix2),len(key_matrix))]


    encoding_dictionary = {"A":1, "a":1 ,"B":2, "b":2 ,"C":3, "c":3 ,"D":4, "d":4 ,"E": 5, "e":5 ,"F":6, "f":6, "G":7, "g":7, "H":8, "h":8, "I":9, "i":9, "J":10, "j":10 ,"K":11, "k":11 ,"L":12, "l":12 ,"M":13,"m":13 ,"N":14, "n":14 ,"O":15, "o":15 ,"P":16, "p":16 ,"Q":17, "q":17 ,"R":18, "r":18 ,"S":19, "s":19 ,"T":20, "t":20 ,"U":21, "u":21 ,"V":22,"v":22 ,"W":23,"w":23 ,"X":24, "x":24 ,"Y":25, "y":25 ,"Z":26,"z":26 ," ":27}
    matrix_letter_list = [encoding_dictionary[matrix_letter[a:a+1]] for a in range(0, len(matrix_letter))]

    if len(matrix_letter_list) % len(matrix1) != 0 :
        matrix_letter_list.append(27)
    if len(matrix_letter_list) % len(matrix1) != 0:
        matrix_letter_list.append(27)
    matrix_number_list = [matrix_letter_list[a:a+len(matrix1[0])] for a in range(0, len(matrix_letter_list),len(matrix1[0]))]

    encoding = []

elif sys.argv[3][-14:] == "ciphertext.txt" :
    f = open(sys.argv[3],"r")
    f2 = open(sys.argv[2],"r")
    f3 = open(sys.argv[4],"w")
    matrix_letter2  = f.readline().split(",")

    matrix_number = []

    for i in matrix_letter2:
        matrix_number.append(int(i))


    decoding_dictionary = {1:"A" ,2:"B" ,3:"C" ,4:"D" ,5:"E" ,6:"F" ,7:"G" ,8:"H" ,9:"I" ,10:"J" ,11:"K" ,12:"L" ,13:"M" ,14:"N" ,15:"0" ,16:"P" ,17:"Q" ,18:"R" ,19:"S" ,20:"T" ,21:"U" ,22:"V" ,23:"W" ,24:"X" ,25:"Y" ,26:"Z" ,27:" " }
    key_matrix = [i.strip("\n").split(",") for i in f2.readlines()]
    matrix2 = []

    for i in range(len(key_matrix)):
        for x in range(len(key_matrix[0])):
            matrix2.append(int(key_matrix[i][x]))
    matrix1 = [matrix2[a:a+len(key_matrix)] for a in range(0, len(matrix2),len(key_matrix))]
    input_key = [matrix2[a:a + len(key_matrix)] for a in range(0, len(matrix2), len(key_matrix))]
    decoding= []



def twoxtwo_matrix():
    for i in range(len(matrix1)):
        for x in range(0,len(matrix_number_list)):
            encoding.append(matrix_number_list[x][0] * matrix1[i][0] + matrix_number_list[x][1]*matrix1[i][1])



    print_encoding = []

    for i in range(0,len(encoding)):
        if i < len(encoding)//2:
            print_encoding.append(encoding[i])
            print_encoding.append(encoding[i+len(encoding)//2])

    for i in range(len(print_encoding)):
        if i < len(print_encoding)-1:
            f3.write("{},".format(print_encoding[i]))
        elif i == len(print_encoding)-1:
            f3.write("{}".format(print_encoding[i]))

def threexthree_matrix():
    for i in range(len(matrix1)):
        for x in range(len(matrix_number_list)):
            encoding.append(matrix_number_list[x][0] * matrix1[i][0] + matrix_number_list[x][1] * matrix1[i][1]+ matrix_number_list[x][2]*matrix1[i][2])
    print_encoding = []
    for i in range(0, len(encoding)):
        if i < len(encoding) // 3:
            print_encoding.append(encoding[i])
            print_encoding.append(encoding[i + len(encoding) // 3])
            print_encoding.append(encoding[i + (len(encoding) // 3)*2])
    for i in range(len(print_encoding)):
        if i < len(print_encoding)-1:
            f3.write("{},".format(print_encoding[i]))
        elif i == len(print_encoding)-1:
            f3.write("{}".format(print_encoding[i]))

def twoxtwo_inverse():


    determ = matrix1[0][0] * matrix1[1][1] - matrix1[0][1]*matrix1[1][0]

    print_decoding =[]
    matrix4 = [[0,0],[0,0]]
    matrix4[0][0] += matrix1[1][1]
    matrix4[0][1] += -matrix1[0][1]
    matrix4[1][0] += -matrix1[1][0]
    matrix4[1][1] += matrix1[0][0]
    for i in range(len(matrix4)):
        for x in range(len(matrix4[i])):
            matrix4[i][x] = round(matrix4[i][x]/determ)



    matrix_number2 = [matrix_number[a:a + 2] for a in range(0, len(matrix_number), 2)]

    for b in range(len(matrix4)):
        for a in range(len(matrix_number2)):
            decoding.append(matrix_number2[a][0] * matrix4[b][0] + matrix_number2[a][1] * matrix4[b][1])

    for i in range(0,len(decoding)):
        if i < len(decoding)//2:
            print_decoding.append(decoding[i])
            print_decoding.append(decoding[i+len(decoding)//2])
    matrix_letter_list2 = []
    for i in range(len(print_decoding)):
        matrix_letter_list2.append(decoding_dictionary[print_decoding[i]])

    for i in range(len(matrix_letter_list2)):
        if i < len(matrix_letter_list2)-1:
            f3.write("{}".format(matrix_letter_list2[i]))
        elif i == len(matrix_letter_list2)-1:
            f3.write("{}".format(matrix_letter_list2[i]))



    return matrix1


matrix3 =[[0,0,0],[0,0,0],[0,0,0]]
def minor():
    global matrix1
    matrix3[0][0] += matrix1[1][1]*matrix1[2][2] - matrix1[1][2]*matrix1[2][1]
    matrix3[0][1] += matrix1[1][0]*matrix1[2][2] - matrix1[1][2]*matrix1[2][0]
    matrix3[0][2] += matrix1[1][0]*matrix1[2][1] - matrix1[1][1]*matrix1[2][0]
    matrix3[1][0] += matrix1[0][1]*matrix1[2][2] - matrix1[0][2]*matrix1[2][1]
    matrix3[1][1] += matrix1[0][0]*matrix1[2][2] - matrix1[0][2]*matrix1[2][0]
    matrix3[1][2] += matrix1[0][0]*matrix1[2][1] - matrix1[0][1]*matrix1[2][0]
    matrix3[2][0] += matrix1[0][1]*matrix1[1][2] - matrix1[0][2]*matrix1[1][1]
    matrix3[2][1] += matrix1[0][0]*matrix1[1][2] - matrix1[0][2]*matrix1[1][0]
    matrix3[2][2] += matrix1[0][0]*matrix1[1][1] - matrix1[0][1]*matrix1[1][0]

    matrix1 = matrix3
    cofactors()


def cofactors():
    for i in range(len(matrix1)):
        if i % 2 == 0:

            for x in range(len(matrix1[i])):
                if x % 2 == 1:
                    matrix1[i][x] = -matrix1[i][x]

                else:
                    continue
        elif i % 2 == 1:
            for x in range(len(matrix1[i])):
                if x % 2 == 0:
                    matrix1[1][x] = -matrix1[1][x]

    adjugate(matrix1)

def adjugate(y):
    transpose = list(map(list,zip(*y)))
    determinant(transpose)


def determinant(x):
    determin = matrix1[0][0] * input_key[0][0] + matrix1[0][1] * input_key[0][1] + matrix1[0][2] * input_key[0][2]

    for i in range(len(x)):
        for k in range(len(x[i])):
            x[i][k] = round(x[i][k]/ determin)

    three_print(x)
def threexthree_inverse():
    print_decoding =[]
    minor()
def three_print(a):
    print_decoding = []

    matrix_number_print = [matrix_number[a:a+3] for a in range(0, len(matrix_number),3)]


    for i in range(len(a)):
        for x in range(len(matrix_number_print)):

            decoding.append(matrix_number_print[x][0] * a[i][0] + matrix_number_print[x][1] * a[i][1] + matrix_number_print[x][2] * a[i][2])

    for i in range(0, len(decoding)):
        if i < len(decoding) // 3:
            print_decoding.append(decoding[i])
            print_decoding.append(decoding[i + len(decoding) // 3])
            print_decoding.append(decoding[i + (len(decoding) // 3)*2])

    matrix_letter_list2 = []
    for i in range(len(print_decoding)):
        matrix_letter_list2.append(decoding_dictionary[print_decoding[i]])
    for i in range(len(matrix_letter_list2)):
        if i < len(matrix_letter_list2)-1:
            f3.write("{}".format(matrix_letter_list2[i]))
        elif i == len(matrix_letter_list2)-1:
            f3.write("{}".format(matrix_letter_list2[i]))



def encode():
    if len(matrix1) == 3:
        threexthree_matrix()
    elif len(matrix1) == 2:
        twoxtwo_matrix()
def decode():
    if len(matrix1) == 3:
        threexthree_inverse()
    if len(matrix1) == 2:
        twoxtwo_inverse()

if operation == "enc":
    encode()
elif operation == "dec":
    decode()
