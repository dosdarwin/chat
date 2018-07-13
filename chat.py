
def read_file():
	chat = []
    with open('C:/Users/Also_Lenovo/Desktop/coding/input.txt', 'r', encoding='utf-8-sig') as lines:
        for line in lines:  
            chat.append(line.strip())
    print(chat)
    return chat

def convert(chat):
    new = []
    person = None
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line)
    print (new)
    return new

def write_file(new):
	with open('C:/Users/Also_Lenovo/Desktop/coding/output.txt', 'w', encoding='utf-8-sig') as k:
		for line2 in new:
			k.write(line2 + "\n")

chat = read_file()
new = convert(chat)
write_file(new)
