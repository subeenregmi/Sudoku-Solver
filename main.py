def createSudokuBoard(filename):
	board = []
	file = None
	try: 
		file = open(filename, "r")
	except:
		print(f"File '{filename}' does not exist")
		return None
	
	for line in file:
		row = []
		for digit in line:
			if digit == '\n':
				continue
			row.append(int(digit))
		board.append(row)
			
	file.close()
	return board

def checkIfValid(board):
	for i in range(9):
		current_row = set({})
		current_col = set({})
		for j in range(9):
			if board[i][j] in current_row:
				return False
			else:
				if board[i][j] != 0:
					current_row.add(board[i][j])

			if board[j][i] in current_col:
				return False
			else:
				if board[j][i] != 0:
					current_col.add(board[j][i])
	
	for i in range(3):
		for j in range(3):
			current_box = set()
			for x in range(3):
				for y in range(3):	
					if board[i*3 + x][j*3 + y] == 0:
						continue
					if board[i*3 + x][j*3 + y] in current_box:
						return False
					current_box.add(board[i*3 + x][j*3 + y])

	return True 

def solveSudoku(board):
	if not checkIfValid(board):
		print("Invalid starting board")
		return

	solved = False
	index = 0
	zeros = []
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				zeros.append((i, j))

	while True:
		board[zeros[index][0]][zeros[index][1]]	+= 1
		
		if board[zeros[index][0]][zeros[index][1]] > 9:
			board[zeros[index][0]][zeros[index][1]] = 0
			index = index - 1
			continue

		if not checkIfValid(board):
			continue	

		else:
			index += 1
			if index == len(zeros):
				break
			
	return board

b = createSudokuBoard("hardest.txt")
x = solveSudoku(b)
print(x)
print(checkIfValid(x))
