def main():
	width, height = float(input()), float(input())

	print(f'Площадь: {width * height}\n'
		f'Периметр: {(width + height) * 2}')

if __name__ == "__main__":
	main()