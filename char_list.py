#coding:UTF-8
char_list = []
def print_arg(arg):
	char_list.append(arg)
	print(char_list)
while True:
	x = input(u'ここに入力してみてね>>')
	print_arg(x)


