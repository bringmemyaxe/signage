#                                  IDEAS
# the list with ideas is just a list where you can add some ideas like
# in a to-do list if you're afraid of forgetting something important
#
#                                  PIECES
# the diagram contains pieces which might be connected like in causality:
# the cause and consequence relationship; or like
# the goal and problems relationship or anything else
#
#                                  ROOT-PIECE
# a root-piece is a piece which isn't a dependency of other ones so far
#
#                                  DEPENDENCY-PIECE
# a dependency-piece is a piece which is going to be added as already
# connected to an existing one
import string
import itertools
import os

digits_and_letters = list(string.digits + string.ascii_uppercase)
digits_and_letters.remove('O')
address_list = [tup[0] + tup[1] for tup in itertools.product(digits_and_letters, digits_and_letters)]
hider_path = 'dependencies/hider.X'
while True:
    mode = input('''
0 - add an idea
1 - show the list of ideas
2 - delete an idea
3 - add a root-piece
4 - add a dependency-piece
5 - show the list of unhidden pieces
6 - hide a piece from the list
7 - connect two pieces
8 - show the list of all pieces
9 - prioritise pieces
e - exit
choose mode: ''')
    if mode == '0':
        idea = input('''add an idea:
''')
        for address in address_list:
            path = 'ideas/ide' + address + '.J'
            if os.path.exists(path):
                pass
            else:
                try:
                    with open(path, 'a', encoding='UTF-8') as new_file:
                        new_file.write(idea)
                        print('saved at ide' + address)
                        break
                except FileNotFoundError:
                    os.makedirs('ideas/')
                    with open(path, 'a', encoding='UTF-8') as new_file:
                        new_file.write(idea)
                        print('saved at ide' + address)
                        break
    elif mode == '1':
        for address in address_list:
            path = 'ideas/ide' + address + '.J'
            try:
                with open(path, encoding='UTF-8') as showing:
                    print('')
                    print('ide' + address + '.J:')
                    print(showing.read())
            except FileNotFoundError:
                pass
    elif mode == '2':
        address = input('''input an address for deleting: ''')
        path = 'ideas/ide' + address + '.J'
        if os.path.exists(path):
            os.remove(path)
            print('successfully deleted')
        else:
            print('wrong address')
    elif mode == '3':
        piece = input('''add a root-piece:
''')
        for address in address_list:
            path_for_Q = 'dependencies/Q/' + address + '.Q'
            if os.path.exists(path_for_Q):
                pass
            else:
                try:
                    with open(path_for_Q, 'w', encoding='UTF-8') as new_file:
                        new_file.write(piece)
                except FileNotFoundError:
                    os.makedirs('dependencies/Q/')
                    with open(path_for_Q, 'w', encoding='UTF-8') as new_file:
                        new_file.write(piece)
                    path_for_X = 'dependencies/X/' + address + '.X'
                    try:
                        open(path_for_X, 'w', encoding='UTF-8')
                    except FileNotFoundError:
                        os.makedirs('dependencies/X/')
                        open(path_for_X, 'w', encoding='UTF-8')
                    print('> successfully created at ' + address + ' <')
                    break
    elif mode == '4':
        root_address = input('''input an address for linking: ''')
        root_path = 'dependencies/X/' + root_address + '.X'
        if os.path.exists(root_path):
            for dependency_address in address_list:
                dependency_path = 'dependencies/Q/' + dependency_address + '.Q'
                if os.path.exists(dependency_path):
                    pass
                else:
                    with open(root_path, 'a', encoding='UTF-8') as connector:
                        connector.write(dependency_address + '\n')
                    print('successfully linked')
                    print('>> saved at:', dependency_address, '<')
                    piece = input('''add a dependency-piece:
''')
                    with open(dependency_path, 'a', encoding='UTF-8') as new_file:
                        new_file.write(piece)
                    dependency_path = 'dependencies/X/' + dependency_address + '.X'
                    open(dependency_path, 'w', encoding='UTF-8')
                    print('successfully saved')
                    break
        else:
            print('wrong address')
    elif mode == '5':
        with open(hider_path, encoding='UTF-8') as hider_open:
            hidden_pieces = hider_open.read().splitlines()
        for address in address_list:
            path = 'dependencies/Q/' + address + '.Q'
            try:
                with open(path, encoding='UTF-8') as showing:
                    if address in hidden_pieces:
                        pass
                    else:
                        print('')
                        print(address + '.Q:')
                        print(showing.read())
            except FileNotFoundError:
                pass
    elif mode == '6':
        address = input('''input an address for hiding: ''')
        path = 'dependencies/Q/' + address + '.Q'
        if os.path.exists(path):
            with open(hider_path, 'a', encoding='UTF-8') as hider:
                hider.write(address + '\n')
            print('successfully hidden')
        else:
            print('wrong address')
    elif mode == '7':
        root_address = input('''input an address for a root-piece: ''')
        root_path = 'dependencies/X/' + root_address + '.X'
        if os.path.exists(root_path):
            dependency_address = input('''input an address for a dependency-piece: ''')
            dependency_path = 'dependencies/Q/' + dependency_address + '.Q'
            if os.path.exists(dependency_path):
                with open(root_path, 'a', encoding='UTF-8') as connector:
                    connector.write(dependency_address + '\n')
                print('successfully linked')
            else:
                print('wrong address')
        else:
            print('wrong address')
    elif mode == '8':
        for address in address_list:
            path = 'dependencies/Q/' + address + '.Q'
            try:
                with open(path, encoding='UTF-8') as showing:
                    print('')
                    print(address + '.Q:')
                    print(showing.read())
            except FileNotFoundError:
                pass
    elif mode == '9':
        counted_list = {}
        value_to_add_to = []
        # not finished
        for address in address_list:
            # not finished
            try:
                # not finished
                value_to_add_to_depth = 0
                if address not in counted_list:
                    counted_list[address] = 1
                else:
                    value_to_add_to[value_to_add_to_depth] = counted_list.get(address)
                    value_to_add_to[value_to_add_to_depth] += 1
                    counted_list[address] = value_to_add_to[value_to_add_to_depth]
                # not finished
        # not finished
        for address, priority in counted_list.items():
            # not finished
            print('the address', address, 'has priority', priority)
    elif mode == 'e':
        break
    else:
        print('wrong mode')
