 #Right-Angled Triangle Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("* " * i)

#Inverted Right-Angled Triangle
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print("* " * i)


#Pyramid Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

#Pyramid Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

#Inverted Pyramid
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

#Number Triangle Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#

