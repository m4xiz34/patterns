print("This is a program that prints triangles using stars (*).")

n = int(input("Enter the amount of rows you want: "))
p = 1

for i in range (n):
    for j in range (i+1):
        print(p, end=" ")
        p = p + 1
        
    print()
