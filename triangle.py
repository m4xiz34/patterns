print("This is a program that prints triangles using stars (*).")

n = int(input("Enter the amount of rows you want: "))

for i in range (n):
    for j in range (i+1):
        print("*  ", end=" ")
    print()
