
keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "?"]]

word = input()

index_row = 0
index_col = 0

for alp in word:
    index2_row = 0
    index2_col = 0
    for i, row in enumerate(keyboard):
        for j, col in enumerate(row):
            if alp == col:
                index_row = index_row - i
                index_col = index_col + j
                print(index_row, index_col)
                if index_row < 0:
                    if index_col < 0:
                        print(i*'_', j*'<')
                    elif index_col > 0:
                        print(i*'_', j*'>')
                elif index_row > 0:
                    if index_col < 0:
                        print(i*'^', j*'<')
                    elif index_col > 0:
                        print(i*'^', j*'>')
    
            


