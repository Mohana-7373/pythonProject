file = open('dummy.txt', 'r')
print(file.readline())
print(file.readline())
file.close()

with open('.\dummy.txt', 'r')as file:
    print(file.read())
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.tell())

with open('dummy.txt', 'r')as file:
    for line in file:
        print(line,end='')
with open('dummy.txt', 'r') as file:
    file_content = file.read(10)
    print(file_content,end='')

    file_content=file.readline()
    print(file_content,end='')
    print(file.tell())

with open('dummy.txt', 'r') as file:
    size_to_read = 20

