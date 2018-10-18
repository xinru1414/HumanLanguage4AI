import sys



def main():
	x = int(sys.argv[1])
	p = 0.5
	count = 0

	for i in range(x):
		p = 0.5 * p / (0.8 - 0.3 * p)
		

	print(p)

if __name__  == '__main__':
	main()
