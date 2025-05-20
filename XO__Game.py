board = [1,2,3,4,5,6,7,8,9] # игровое поле
def game_board(): #Чертим игроовое поле
	print (('_' * 4 * 3 ))
	for i in range(3):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

def win(): # Проверка выигрышных ситуаций
	winner = False

	win_situations = (
		(0,1,2), (3,4,5), (6,7,8),
		(0,3,6), (1,4,7), (2,5,8),
		(0,4,8), (2,4,6)
	) #все возможные ситуации, в которых может выиграть "Х" или "0"

	for sit in win_situations:

		if (board[sit[0]] == board[sit[1]] and board[sit[1]] == board[sit[2]] and board[sit[1]] in ('X','0')):
			winner = board[sit[0]]

	return winner

def step_game(index, char):

	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False

	board[index-1] = char
	return True

def start_game():
	player = 'X' #Имя игрока, начинаем с "Х"
	step = 1

	game_board()


	while (step < 10) and (win() == False):
		index = input('Введите номер клетки для ' + player + ' ')

		if not (index in "123456789"): # Проверка, чтобы игроки вводили тольцо цифры
			print("Ошибка! Введите цифры пустых клеток доски!")
			continue

		if (step_game(int(index), player)):


			if (player == 'X'):
				player = 'O'
			else:
				player = 'X'

			game_board()

			step += 1
		else:
			print('Ошибка! Введите номер свободной клетки!')

	if (step == 10 and not win()):
		print('Ничья!')
	else:
		print('Поздравляем! Победил ' + win())

print('Игра началась!')
start_game()