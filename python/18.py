from common import *

Triangle = textToList("0067_triangle.txt")  

for i in range(len(Triangle)-2, -1, -1):

    for j in range(0, len(Triangle[i])):

        if Triangle[i+1][j] > Triangle[i+1][j+1]:

            Triangle[i][j] += Triangle[i+1][j]

        else:

            Triangle[i][j] += Triangle[i+1][j+1]

print(Triangle[0][0])
