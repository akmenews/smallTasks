label = '''                  menu 
    1. show list
    2. add item
    3. remove item by position
    4. remove item by value
    5. save list
    0. exit
    '''

command = input('enter command number ')
data = []
file = open('readme.txt', 'r')
data = file.readlines()
file.close()
while command != '0':
    if command == '1':
        #data = file.readlines()
        print(data)
    elif command == '2':
        item = input('enter item ')
        if item:
            data.append(item)
    elif command == '3':
        #file = open('readme.txt', 'r')
        #data = file.readlines()
        print(data)
        position = input('enter remove position ')
        if position.isdigit():
            position = int(position) - 1
            #print(len(data))
            #print(data(position))
            if 0 < position < len(data):
                data.pop(position)
            else:
                print('wrong position ')
    if command == '4':
        value = input('enter value ')
        if value in data:
            data.remove(value)
            print('remove ', value)
        else:
            print(value, ' not found ')
    if command == '5':
        file = open('readme.txt', 'a')
        # print(data)
        for items in data:
            file.writelines(items)
        file.close()
    if command == '0':
        quit()

    else:
        command = input('enter command number ')



