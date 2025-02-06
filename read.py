'''
Comenta aqui
'''
def read_and_sort_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		names = file.readlines()
	
	# Comenta aqui
	names = [name.strip() for name in names]
	names.sort()
	
	# Comenta aqui
	for name in names:
		print(name)
