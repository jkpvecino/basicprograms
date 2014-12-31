
"""Manipulator is a Python calculator used to work with 2 dimensional vectors. It can be used to
calculate products between two vectors, sums of vectors, and scaled vectors through scaler
multiplication. Manipulator can also be used to graph vectors in two-dimensions on a standard
x1-x2 plane.

Instructions on how to use the program are included in-program. On default, Manipulator will
add vectors to one graphing matrix.

To test inputs, one may input the standard vector e1 by typing in 1 0 and pressing enter, and
vector e2 by typing in 0 1 and pressing enter. From here, one may use the functions listed under
the 'How-to' command to test the commands provided by manipulator.

All commands must be inputed as given by the program. Commands are case-sensitive and 
whitespace-sensitive."""

from functools import reduce
from operator import add
from operator import mul
import matplotlib.pyplot as plt

gmatrix = {}

###################
## vector basics ##
###################

def make_vector(x, y):
    return [x, y]

def xcoordinate(vector):
    return vector[0]

def ycoordinate(vector):
    return vector[1]

def inmatrix(lst):
	if len(lst) == 0:
		return False
	elif len(lst) == 1:
		return lst[0] in gmatrix
	else:
		return lst[len(lst) - 1] in gmatrix and inmatrix(lst[0:(len(lst)-1)])


######################
## vector functions ##
######################

def prod(vector1, vector2):
    try:
        assert type(vector1) is list and type(vector2) is list
        prod = []
        for index in range(len(vector1)):
            prod.append(vector1[index] * vector2[index])
        return reduce(add, prod)
    except AssertionError:
        return 'Inputs must be vectors'
    except IndexError:
        return 'Vectors must be in the same dimension'


def scale(vector, scaler):
    try:
        assert type(scaler) is int and type(vector) is list
        scaledvector = []
        for item in range(len(vector)):
            scaledvector.append(vector[item] * scaler)
        return scaledvector
    except AssertionError:
        return 'Wrong type of input on vector or scaler'

def addvector(vector1, vector2):
    try:
        assert len(vector1) == len(vector2)
        add_vector = []
        for index in range(len(vector2)):
            add_vector.append(vector1[index] + vector2[index])
        return add_vector
    except AssertionError:
        return 'Vectors must be in the same dimension.'
    except ValueError:
        return 'Vectors must contain real numbers.'

def addmultiple(lst):
    try:
        if len(lst) == 1:
            return lst[0]
        else:
            return reduce(addvector, lst)
    except IndexError:
        return 'There must be at least one vector as an input.'



##############
## graphing ##
##############

def graph(vector):
    graph1 = plt.plot([0, xcoordinate(vector)], [0, ycoordinate(vector)])

def wipe():
    gmatrix = {}

def graphmatrix():
    for vector in gmatrix:
        graph(gmatrix[vector])

def add_to_matrix(list_input, name):
    try:
        assert type(list_input) is list
        assert type(name) is str
        gmatrix[name] = list_input
    except AssertionError:
        return 'Names of vectors must be strings'

def scalegraph(vector, scaler):
    gmatrix[vector] = scale(gmatrix[vector], scaler)

def scalemultiple(lst, scaler):
    for vector in lst:
        gmatrix[vector] = scale(gmatrix[vector], scaler)

def scalewholegraph(scaler):
    for vector in gmatrix:
        gmatrix[vector] = scale(gmatrix[vector], scaler)



###############
## interface ##
###############

print("")
print("Welcome to Manipulator.")
print("This is a 2D vector manipulator. Vectors in dimensions greater than two")
print("will not work.")
print("")

choice = 'How-to'

while choice != False:
    if choice == "How-to":
        print ("The following commands are available. Each command must be written correctly,")
        print ("otherwise the command will be invalid.")
        print (" ")
        print ("How-to - this will replay this message and list commands")
        print ("To create vectors, input two coordinates, x-coordinate first,")
        print ("then the y-coordinate.")
        print ("Matrix - this will show the current matrix of vectors")
        print ("Wipe - this will delete the current matrix of vectors")
        print ("Delete <insert vector name> - this will delete the chosen vector from the matrix")
        print ("Graph - this will graph the current matrix of vectors")
        print ("Vector operations - this will open the menu for vector operations")
        print ("exit - this will close the program")

    elif choice == 'Matrix':
        print(gmatrix)

    elif choice == 'Wipe':
        gmatrix = {}

    elif choice.replace(" ", "").replace("-", "").isdigit() == True:
        veclist = list(map(int, choice.split()))
        vector = make_vector(veclist[0], veclist[1])
        name = input("Please name this vector. ")
        add_to_matrix(vector, name)

    elif choice[0:6] == 'Delete':
        trash = gmatrix.pop(choice[7::])

    elif choice == 'Graph':
        graphmatrix()
        plt.axis([-10, 10, -10, 10])
        plt.grid()
        plt.show()

    elif choice == 'Vector operations':
        print (" ")
        print ("The following operations are available:")
        print (" ")
        print ("Vector addition")
        print ("Vector multplication")
        print ("Vector scaling")
        print ("Matrix scaling")
        print ("Which operation would you like to use?")

        choice2 = input()
        
        while choice2 != False:
            if choice2 == "Vector addition":
                sumlist, vectors = [], []
                while not inmatrix(vectors):
                	vectors = input("List each vector by name. ").split()
                for vector in vectors:
                    sumlist.append(gmatrix[vector])
                result = addmultiple(sumlist)
                name = input("Please name this vector. ")
                add_to_matrix(result, name)
                print (result)
            
            elif choice2 == "Vector multiplication":
                vectors = input("List each vector by name. ").split()
                print (prod(gmatrix[vectors[0]], gmatrix[vectors[1]]))

            elif choice2 == "Vector scaling":
                factor = 'a'
                vectors = input("List each vector you would like to scale by name. ").split()
                while factor.replace(" ","").replace(".","").replace("-","").isdigit() == False:
                    print("Please pick a scaler you would like to use. ")
                    factor = input()
                    result = scalemultiple(vectors, int(factor))
                print (gmatrix)

            elif choice2 == 'Matrix scaling':
                factor = 'a'
                while factor.replace(" ","").replace(".","").replace("-","").isdigit() == False:
                    print("Please pick a scaler you would like to use. ")
                    factor = input()
                scalewholegraph(int(factor))
                print (gmatrix)

            print("Would you like to do more operations? (Yes or No)")
            cont = input()
            if cont == 'No':
                choice2 = False
            elif cont == 'Yes':
                choice2 = input()
    
    elif choice == 'exit':
        exit()
    
    else:
        print("Invalid command.")

    choice = input()































































