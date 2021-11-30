
keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "?"]]

word = input()

index_row = 0
index_col = 0
index2_row = 0
index2_col = 0

for alp in word:
    for i, row in enumerate(keyboard):
        for j, col in enumerate(row):
            if alp == col:
                index2_row = (index_row + i) - index2_row
                index2_col = (index_col - j) - index2_col
                #print("index_row", index_row,"index2_row", index2_row, "i=", i)
                #print("index_col", index_col,"index2_col", index2_col,"j=", j)
                if index2_row >= 0:
                    if index2_col >= 0:
                        print(abs(index2_row)*'_', end="")
                        print(abs(index2_col)*'<', end="")
                        print("@", end="")
                    elif index2_col <= 0:
                        print(abs(index2_row)*'_', end="")
                        print(abs(index2_col)*'>', end="")
                        print("@", end="")
                elif index2_row <= 0:
                    if index2_col >= 0:
                        print(abs(index2_row)*'^', end="")
                        print(abs(index2_col)*'<', end="")
                        print("@", end="")
                    elif index2_col <= 0:
                        print(abs(index2_row)*'^', end="")
                        print(abs(index2_col)*'>', end="")
                        print("@", end="")
                index2_row = i
                index2_col = -j
                
                
            


