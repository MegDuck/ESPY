
maxstack = 1024
    
class card:
	stack_sizes = []
	for i in range(1, maxstack + 1):
		if maxstack % i == 0:
			stack_sizes.append(i)
	
	
def generate_stack():
	stack = {}
	
	for i in range(1, card.stack_sizes[len(card.stack_sizes)//2] + 1):
		stack[i] = {}
		for j in range(1, maxstack // card.stack_sizes[len(card.stack_sizes)//2] + 1):
			stack[i][j] = 0
	return stack
	

def parse(code):
	for i in code:
		if i in ('>', '<', '^', 'v'):
			if i == '>':
			
				if root.tech['sb'] == True:
					root.line_pos += 2
					root.tech['sb'] = False
				else:
					root.line_pos += 1
			elif i == '<':
				if root.tech['sb'] == True:
					root.line_pos -= 2
					root.tech['sb'] = False
				else:
					root.line_pos -= 1
				if root.line_pos < 1:
					root.line_pos = 1
			elif i == '^':
				if root.tech['sb'] == True:
					root.line += 2
					root.tech['sb'] = False
				else:
					root.line += 1
			elif i == 'v':
				if root.tech['sb'] == True:
					root.line -= 2
					root.tech['sb'] = False
				else:
					root.line -= 1
		elif i in ('+', '-', '*', '%', '/'):
			if i == '+':
				root.value += 1
			elif i == '-':
				root.value -= 1
			elif root.value == '/':
				root.value /= root.stack[root.line-1][root.line_pos]
			elif root.value == '%':
				root.value %= root.stack[root.line-1][root.line_pos]
			elif root.value == '*':
				root.value *= root.stack[root.line-1][root.line_pos]
		elif i == '"':
			if root.tech['asc'] == False:
				root.tech['asc'] = True
			else:
				root.tech['asc'] = False
		elif i in ('?', '#', '_', '|', '@'):
			if i == '?':
				import random
				choice = random.choice(('>', '<', '^', 'v'))
				if choice == '>':
					root.line_pos += 1
				
				elif choice == '<':
					root.line_pos -= 1
					if root.line_pos < 1:
						root.line_pos = 1
				elif choice == '^':
					root.line += 1
				elif choice == 'v':
					root.line -= 1
					
			elif i == '#':
				root.tech['sb'] = True
			elif i == '@':
				import sys
				sys.exit(1)
			elif i == '_':
				if root.value == 0:
					root.line_pos += 1
				else:
					root.line_pos -= 1
			elif i == '|':
				if root.value == 0:
					root.line -= 1
				else:
					root.line += 1
		elif i in (':', '/', '$'):
			if i == ':':
				root.value += root.value
			elif i == '/':
				root.value, root.stack[root.line][root.line_pos - 1] = root.value, root.stack[root.line][root.line_pos - 1]
			elif i == '$':
				root.value = 0
				
		elif i in ('&', '~', '.', ','):
			if i == '&':
				inp = input()
				try:
					root.value = int(inp)
				except ValueError:
					None
			elif i == '~':
				inp = input()
				try:
					try:
						root.value = ord(inp)
					except IndexError:
						None
				except TypeError:
					None
			elif i == '.':
				try:
					print(int(root.value))
				except TypeError:
					None
				except ValueError:
					None
			elif i == ',':
				try:
					if root.value == '\\':
						print('\n')
					else: 
						from colorama import Fore, Style
						print(chr(root.value), end="")
				except TypeError:
					
					print(str(root.value), end="")
		elif i in ('!', '`'):
			if i == '!':
				if root.value != 0:
					root.value = 0
				else:
					root.value = 1
			elif i == '`':
				if root.value > root.stack[root.line - 1][root.line_pos]:
					root.value = 1
				else:
					root.value = 0
					
		elif i == 'd' and root.tech['asc'] == False:
			import datetime
			
			file = open('log.txt', 'a')
			file.write(f"\ncode: {text}\ndate: {datetime.datetime.today()}\n")
			
			file.close()
			print(f"pos: {root.line_pos}")
			print(f"line: {root.line}")	
			print(f"value is {root.value}")
		
		elif root.tech['asc'] == True:
			if i == '\\':
				root.value = '\\'
			else:
				root.value = i
			root.tech['asc'] = False
#			text = []
#			text.append(i)
#			ready_index = None
#			ready = False
#		
#			if i == '\\':
#				ready_index = text.index(i)
#				ready = True
#			
#			if ready == True:
#				try:
#					if text[ready_index + 1] == 'n':
#						root.value = '\n'
#						ready = False
#						ready_index = None
#				except IndexError:
#					break
#			root.value = str(i)
class root:
	tech = {'sb': False, 'asc': False}
	line=1; line_pos=1
	stack = generate_stack()
	
	value = stack[line][line_pos]
'''
> - right
< - left
^ - up
° - down
'''

				


text = input(': ')	
parse(text)