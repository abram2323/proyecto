'''
carga el fichero y enseña el contenido
'''
def read_and_sort_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		names = file.readlines()
	
	# Coge el fichero y guarda el contenido en la variable "names"
	names = [name.strip() for name in names]
	names.sort()
	
	# Es un bucle que muestra por pantalla los nombres
	for name in names:
		print(name)
