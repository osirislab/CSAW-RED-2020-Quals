#!/usr/bin/env python3

import random
import sys
import time

#-----------------------------------------------------------------------------------------------------------------------------------
def create_board(width, height, padding):
	rows = (height * (padding + 8))
	cols = (width  * (padding + 17))
	board = [[' ' for i in range(cols)] for i in range(rows)]
	marker = [['.' for i in range(width)] for i in range(height)]
	return board, marker

#-----------------------------------------------------------------------------------------------------------------------------------
def draw_face(board, padding, face, x, y):
	for row in range(len(face)):
		chars = list(face[row])
		for col in range(len(chars)):
			x_off = x * (padding + 17)
			y_off = y * (padding + 8)
			board[y_off + row + 1][x_off + col + 1] = chars[col]

#-----------------------------------------------------------------------------------------------------------------------------------
def draw_squares(board, width, height, padding, corner_size, tl, tr, bl, br, t, b, l, r):
	if corner_size == 0:
		v0 = 0
		v1 = 0
		v2 = 0
		tl1 = l; tr1 = r
		tl2 = l; tr2 = r
		bl2 = l; br2 = r
		bl1 = l; br1 = r
	elif corner_size == 1:
		v0 = 1
		v1 = 0
		v2 = 0
		tl1 = tl; tr1 = tr
		tl2 = l;  tr2 = r
		bl2 = l;  br2 = r
		bl1 = bl; br1 = br
	else:
		v0 = 2
		v1 = 1
		v2 = 0
		tl1 = tl; tr1 = tr
		tl2 = tl; tr2 = tr
		bl2 = bl; br2 = br
		bl1 = bl; br1 = br

	for y in range(height):
		for x in range(width):
			x_off = x * (padding + 17)
			y_off = y * (padding + 8)

			board[y_off + 0][x_off + v0] = tl;  board[y_off + 0][x_off + 16 - v0] = tr
			board[y_off + 1][x_off + v1] = tl1; board[y_off + 1][x_off + 16 - v1] = tr1
			board[y_off + 2][x_off + v2] = tl2; board[y_off + 2][x_off + 16 - v2] = tr2
			board[y_off + 3][x_off + v2] = l;   board[y_off + 3][x_off + 16 - v2] = r
			board[y_off + 4][x_off + v2] = l;   board[y_off + 4][x_off + 16 - v2] = r
			board[y_off + 5][x_off + v2] = bl2; board[y_off + 5][x_off + 16 - v2] = br2
			board[y_off + 6][x_off + v1] = bl1; board[y_off + 6][x_off + 16 - v1] = br1
			board[y_off + 7][x_off + v0] = bl;  board[y_off + 7][x_off + 16 - v0] = br

			for i in range(15 - (corner_size * 2)):
				board[y_off + 0][x_off + 1 + corner_size + i] = t
				board[y_off + 7][x_off + 1 + corner_size + i] = b

	marker = [['.' for i in range(width)] for i in range(height)]
	return board, marker

#-----------------------------------------------------------------------------------------------------------------------------------
def print_board(board):
	for row in board:
		print(''.join(row))

#-----------------------------------------------------------------------------------------------------------------------------------
def main():
	mole = (
		r'      ___      ',
		r'    \"_ _"/    ',
		r'    | >-< |    ',
		r' ../ " O " \.. ',
		r' (((:-,_,-:))) ',
		r'               ',
	)

	smiley = (
		r'               ',
		r' \|/ ____ \|/  ',
		r'  @~/ ,. \~@   ',
		r' /_( \__/ )_\  ',
		r'    \__U_/     ',
		r'               ',
	)

	horizontals = (
		('-', '-'),
		('.', '.'),
		('+', '+'),
		('*', '*'),
		('#', '#'),
		('@', '@'),
		('=', '='),
		('^', 'V'),
	)
	verticals = (
		('|', '|'),
		('.', '.'),
		('+', '+'),
		('*', '*'),
		('#', '#'),
		('@', '@'),
		(':', ':'),
		('<', '>'),
		('[', ']'),
		('{', '}'),
		('(', ')'),
	)
	corners = (
		('*', '*',  '*',  '*'),
		('.', '.',  '.',  '.'),
		('o', 'o',  'o',  'o'),
		('O', 'O',  'O',  'O'),
		('@', '@',  '@',  '@'),
		('#', '#',  '#',  '#'),
		('+', '+',  '+',  '+'),
		('/', '\\', '\\', '/'),
	)

	level = 1
	score = 0
	hit = 0
	max_time = 10.25 - level

	while True:
		# Calculate level-based parameters
		corner_size = 0
		padding = 1
		faces = 0
		if level > 3:
			corner_size = random.randint(0, 1)
			padding = random.randint(1, 2)
			faces = random.randint(0, level-2)
		if level > 5:
			corner_size = random.randint(0, 2)
			padding = random.randint(1, 3)

		# Create the board
		width = random.randint(3, level + 2)
		height = random.randint(3, level + 2)
		board, marker = create_board(width, height, padding)

		# Draw smiley faces
		for _ in range(faces):
			smiley_x = random.randint(0, width-1)
			smiley_y = random.randint(0, height-1)
			draw_face(board, padding, smiley, smiley_x, smiley_y)
			marker[smiley_y][smiley_x] = 's'

		# Draw the mole
		mole_x = random.randint(0, width-1)
		mole_y = random.randint(0, height-1)
		draw_face(board, padding, mole, mole_x, mole_y)
		marker[mole_y][mole_x] = 'm'
		#print("1: marker = " + str(marker))

		# Draw the squares on the board
		horizontal = random.randint(0, min(level-1, len(horizontals)-1))
		vertical = random.randint(0, min(level-1, len(verticals)-1))
		corner = random.randint(0, min(level-1, len(corners)-1))
		draw_squares(board, width, height, padding, corner_size, *corners[corner] + horizontals[horizontal] + verticals[vertical])

		# Print the board
		print('Level: {0}   Score: {1}\n'.format(level, score))
		print_board(board)
		start = time.time()
		print('\nWhack (row col): ', end = '', flush=True)

		# Get the input from the player
		input = sys.stdin.readline().strip().split(' ')
		row = -1
		col = -1
		if len(input) == 2:
			try:
				row = int(input[0])
				col = int(input[1])
			except:
				pass

		# Check the input
		#print("User input: row = " + str(row) + ", col = " + str(col))
		#print("marker: " + str(marker))
		missed = True
		end = time.time()
		if ((end - start) > max_time):
			print('Too slow!')
		elif (row >= 0) and (row < height) and (col >= 0) and (col < width):
			if marker[row][col] == 'm':
				print('Whack!\n')
				score += 100
				missed = False
			elif marker[row][col] == 's':
				print('Ouch! :(')
				exit()
		if missed:
			print('Missed!')
			score -= 50
			if score < 0:
				score = 0
		else:
			hit += 1
			if (hit >= 10) and (level < 10):
				level += 1
				hit = 0
				max_time = 10.6 - level # was 10.25 - level, want to allow more time for slow internet connections

		# Check if the player has won
		if score > 10000:
			print('\n'
				'+---------------------+\n'
				'|                     |\n'
				'| YOU ARE A WINNER!!! |\n'
				'|                     |\n'
				'+---------------------+\n'
				'\n'
				'flag{Wh4t3v3r_d1d_th3_p00r_m0l3_d0_t0_y0u?}\n')
			exit()

#-----------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
