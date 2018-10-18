import math
import matplotlib.pyplot as plt


def main():
	f1 = [418.5, 813.8, 447.9, 801.0, 616.3, 654.0]
	f2 = [2474.1, 1740.0, 845.3, 1544.2, 1077, 1381.4]
	n = ['ni','na','nu','er','bo','e']

	plt.scatter(f1, f2)
	plt.xlim(0, math.ceil(max(f1))+100)
	plt.ylim(0, math.ceil(max(f2))+100)
	plt.xlabel('F1 Formant')
	plt.ylabel('F2 Formant')
	plt.title('Formant Chart')

	for i, text in enumerate(n):
		plt.annotate(text, (f1[i], f2[i]))

	plt.show()

if __name__  == '__main__':
	main()
