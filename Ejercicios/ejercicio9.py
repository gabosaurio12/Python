def digito(c):
	if ord(c) > 47 and ord(c) < 58:
		return True
	else:
		return False

def main():
	car = input('Caracter ')
	print(digito(car))

if __name__ == '__main__':
	main()
