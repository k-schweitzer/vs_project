"""this module is wrapper for running calculation of matrixes,
you should tun it with file specified
"""

# import file with methodss for matri operation
from __cramerLib__ import convertToMatrixAndVector
from __cramerLib__ import replaceWithRightSides
from __cramerLib__ import determinantCalculation
# import sys for handling of arguments
import sys


"""This method calcualtes teterminant of matrix,

 determinantCalculation(). For example,

>>> determinantCalculation([1, 1, 1, 1, 1, 1, 1, 1, 1])
1
"""


def main():
    """ main of the script,

        this method is run automatically after script is opened
    """

    if(len(sys.argv) != 2):
        if(len(sys.argv) < 2):
            print("too few argumetns specified")
            sys.exit(1)
        else:
            print("too many arguments specified")
            sys.exit(1)

    if(sys.argv[1] == 'help'):
        print("-Welcome to 3x3 matrix variables calculation script\n script returns value of variables x y z of matrix epanded by vector of right sides containing results of equations")
        print("-Script is run by running python __cramerCalcMain__.py with specification of file containing matrix to be solved with space used as delimiter between columns.")
        print("-Matrix must be of 3x3 with column with results of equations, tus in format:")
        print("\t k1x l1y m1z R1")
        print("\t k2x l2y m2z R2")
        print("\t k3x l3y m3z R3")

        sys.exit(0)

    # open file
    try:
        FILE = open(sys.argv[1])
    except IOError:
        print("File "+sys.argv[1]+' not found on this machine')
        sys.exit(1)

    lines = []
    # convert file to array of strings where string is one line.
    for line in FILE:
        lines.append(line)

    # variables used in code to
    matrix = []
    vector = []

    # run conversion of file to matrix
    if convertToMatrixAndVector(lines, matrix, vector) != 1:
        sys.exit(1)

    # determinant of matrix without altered columns
    determinantOfMatrix = determinantCalculation(matrix)

    if determinantOfMatrix == 0:
        print("determinant of matrix is ZERO! Can't calcualte value of variables")
        sys.exit(1)

    # array of results
    results = {}

    # calculation of
    results["x"] = determinantCalculation(replaceWithRightSides(matrix, vector, 0))/determinantOfMatrix
    results["y"] = determinantCalculation(replaceWithRightSides(matrix, vector, 1))/determinantOfMatrix
    results["z"] = determinantCalculation(replaceWithRightSides(matrix, vector, 2))/determinantOfMatrix

    # print results of calculation
    print("Results form matrix:")
    print(str(matrix[0])+"\t"+str(matrix[1])+"\t"+str(matrix[2]))
    print(str(matrix[3])+"\t"+str(matrix[4])+"\t"+str(matrix[5]))
    print(str(matrix[6])+"\t"+str(matrix[7])+"\t"+str(matrix[8]))
    print("And vector: "+str(vector[0])+" "+str(vector[1])+" "+str(vector[2]))
    print("Are:")
    print("x: "+str(results["x"]))
    print("y: "+str(results["y"]))
    print("z: "+str(results["z"]))
    sys.exit(0)


main()
