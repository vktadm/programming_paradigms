PARAMETR = True

if PARAMETR:
	def get_rect(a, b):
		return f'Периметр: {2 * (a + b)}'
else:
	def get_rect(a, b):
		return f'Площадь: {a * b}'

print(get_rect(5, 6))