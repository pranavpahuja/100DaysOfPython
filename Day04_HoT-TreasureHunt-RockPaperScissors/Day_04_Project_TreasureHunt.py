row1 = ["▓▓","▓▓","▓▓"]
row2 = ["▓▓","▓▓","▓▓"]
row3 = ["▓▓","▓▓","▓▓"]

map = [row1, row2, row3]

rc = input("Enter the row and column where you want to hide the treasure: (use RC format, e.g. 23 for R=2 and C=3):> ")

row = rc[0]
column = rc[1]
print(row + " " + column)

map[int(row)-1][int(column)-1] = 'X'

print(row1)
print(row2)
print(row3)