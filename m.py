def matrix (matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print (matrix[i][j])
	for y in matrix:
		print (y)
		#print("\n")
#def main ():
m=int( input("enter first matrix rows"))
n= int( input("enter first matrix columns"))
p=int( input("enter second matrix rows"))
q=int( input("enter second matrix columns"))
if (n != p):
	print ("matrix mul not exist")
	exit();
array1= [[0 for j in range (0,n)] for i in range (0,m)]
array2= [[0 for j in range (0,q)] for i in range (0,p)]
result= [[0 for j in range (0,q)] for i in range (0,m)]
print ("enter first matrix elements:")
for i in range (0,m):
	for j in range (0,n):
		array1[i][j]=int (input("enter element"))
print ("enter second matrix elements:")
for i in range (0,p):
	for j in range (0,q):
		array2[i][j]=int (input("enter element"))
print("first matrix")
matrix(array1)
print ("second matrix")
matrix(array2)

for i in range(0,m):
	for j in range (0,q):
		for k in range(0,n):
			result[i][j] +=array1[i][k] * array2[k][j]

print ("mul of two matrices:")
matrix(result)


