from read import read_and_sort_file

def main():
	nombre = input("¿Cómo te llamas?: ")
	print(f"¡Hola, {nombre}, te presento a tus compañeros de clase!")
	file_path = 'nombres.txt'
	read_and_sort_file(file_path)


if __name__ == "__main__":
	main()