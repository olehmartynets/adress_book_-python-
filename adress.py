import pickle

def open_file():
    try:
        with open('data3.pickle', 'rb') as f:
            data_new = pickle.load(f)
            return data_new
    except:
        return False

file_not_empty = bool(open_file())

def write_file(file):
    adress_array = []
    if file_not_empty:
        adress_array = open_file()
        adress_array.append(file)
    else:
        adress_array.append(file)
    with open('data3.pickle', 'wb') as f:
        pickle.dump(adress_array, f)

def add_new_adress():
    adress_obj = {}
    name = input('enter name : ')
    city = input('enter city : ')
    adress_obj[name] = city
    write_file(adress_obj)

def show_adress(adress):
    for file in adress:
        print(file)

def find_adress(key):
    data = open_file()
    if file_not_empty:
        all_adress = []
        for obj in data:
            if key in obj.keys():
               all_adress.append(key + ' - ' + obj[key])
        if len(all_adress):
            for el in all_adress:
                print(el)
        else:
            print('we do not have adress for ' + key)

    else:
        print('book is empty')

def remove_adress(adress):
    if file_not_empty:
        data = open_file()
        for i in range(len(data)):
            if adress in data[i].keys():
                del data[i]
                with open('data3.pickle', 'wb') as f:
                    pickle.dump(data, f)
                print(adress + 'was removed')
                break
            else:
                print(adress + 'not in book')
    else:
        print('we do not souch adress')

def main(action):
    if action == '2':
        key = input('enter name : ')
        find_adress(key)

    elif action == '3':
        name = input('enter name for remove adress : ')
        remove_adress(name)
    elif action == '4':
        if file_not_empty:
            show_adress(open_file())
        else:
            print(' adress book is empty')

    elif action == '3':
        print('remove adress')

    else:
        add_new_adress()

while True:
    print(
        '''
     Please choose one variant:

     Add adress - 1
     find aress - 2
     remove adress - 3
     show all adress - 4
     exit - exit
     another symbol will be - add adress
        '''
    )
    action = input('enter your variant : ')
    if action == 'exit':
        print('exit')
        break
    main(action)

