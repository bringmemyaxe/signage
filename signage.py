import os
r = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
full_r = []
for one in r:
    for two in r:
        appender = one + two
        full_r.append(appender)
while True:
    mode = input('''
0 - add an idea
1 - create a thing
2 - create a thing connected to an existing one (without showing the list)
3 - mark a thing as fully planned (hiding this thing from the list)
4 - show unhidden things
5 - show the list
6 - connector
7 - show the ideas
8 - delete an idea
9 - prioritise things
e - exit
choose mode: ''')
    if mode == '0':
        mode0_idea = input('''add an idea:
''')
        for mode0_address in full_r:
            mode0_path = 'ideas/ide' + mode0_address + '.J'
            if os.path.exists(mode0_path):
                pass
            else:
                try:
                    with open(mode0_path, 'a', encoding='UTF-8') as mode0_adder:
                        mode0_adder.write(mode0_idea)
                        print('saved at ' + 'ide' + mode0_address)
                        break
                except FileNotFoundError:
                    os.makedirs('ideas/')
                    with open(mode0_path, 'a', encoding='UTF-8') as mode0_adder:
                        mode0_adder.write(mode0_idea)
                        print('saved at ' + 'ide' + mode0_address)
                        break
    elif mode == '1':
        mode1_temp = input('''create a core for dependencies:
''')
        for address in full_r:
            mode1_path_Q = 'dependencies/Q/' + address + '.Q'
            if os.path.exists(mode1_path_Q):
                pass
            else:
                try:
                    with open(mode1_path_Q, 'a', encoding='UTF-8') as mode1_description:
                        mode1_description.write(mode1_temp)
                except FileNotFoundError:
                    os.makedirs('dependencies/Q/')
                    with open(mode1_path_Q, 'a', encoding='UTF-8') as mode1_description:
                        mode1_description.write(mode1_temp)
                mode1_path_X = 'dependencies/X/' + address + '.X'
                try:
                    open(mode1_path_X, 'w', encoding='UTF-8')
                except FileNotFoundError:
                    os.makedirs('dependencies/X/')
                    open(mode1_path_X, 'w', encoding='UTF-8')
                print('>', 'successfully created at', address, '<')
                break
    elif mode == '2':
        mode2_link = input('''input an address for linking: ''')
        mode2_linked_address = 'dependencies/X/' + mode2_link + '.X'
        if os.path.exists(mode2_linked_address):
            for mode2_new_link in full_r:
                mode2_new_path_Q = 'dependencies/Q/' + mode2_new_link + '.Q'
                if os.path.exists(mode2_new_path_Q):
                    pass
                else:
                    with open(mode2_linked_address, 'a', encoding='UTF-8') as mode2_linking:
                        mode2_linking.write(mode2_new_link + '\n')
                    print('>', 'successfully linked', '<')
                    print('>>', 'the address for a new thing is:', mode2_new_link, '<<')
                    mode2_temp = input('''create a dependency:
''')
                    with open(mode2_new_path_Q, 'a', encoding='UTF-8') as mode2_new_description:
                        mode2_new_description.write(mode2_temp)
                    mode2_new_path_X = 'dependencies/X/' + mode2_new_link + '.X'
                    open(mode2_new_path_X, 'w', encoding='UTF-8')
                    print('successfully saved')
                    break
        else:
            print('wrong address')
    elif mode == '3':
        mode3_address = input('''input an address for hiding: ''')
        mode3_path_check = 'dependencies/Q/' + mode3_address + '.Q'
        if os.path.exists(mode3_path_check):
            with open('dependencies/hider.X', 'a', encoding='UTF-8') as hider:
                hider.write(mode3_address + '\n')
            print('address', mode3_address, 'was successfully marked as hidden')
        else:
            print('wrong address')
    elif mode == '4':
        with open('dependencies/hider.X', encoding='UTF-8') as mode4_checker:
            mode4_hidden_things = (mode4_checker.read().splitlines())
        for mode4_brute in full_r:
            mode4_path = 'dependencies/Q/' + mode4_brute + '.Q'
            try:
                with open(mode4_path, encoding='UTF-8') as mode4_showing:
                    if mode4_brute in mode4_hidden_things:
                        pass
                    else:
                        print('')
                        print(mode4_brute + '.Q' + ':')
                        print(mode4_showing.read())
            except FileNotFoundError:
                pass
    elif mode == '5':
        for mode5_brute in full_r:
            mode5_path = 'dependencies/Q/' + mode5_brute + '.Q'
            try:
                with open(mode5_path, encoding='UTF-8') as mode5_showing:
                    print('')
                    print(mode5_brute + '.Q' + ':')
                    print(mode5_showing.read())
            except FileNotFoundError:
                pass
    elif mode == '6':
        mode6_first = input('''input an address for a thing: ''')
        mode6_first_path = 'dependencies/X/' + mode6_first + '.X'
        if os.path.exists(mode6_first_path):
            mode6_second = input('''input an address for the second thing that you need for the first one: ''')
            mode6_second_path = 'dependencies/Q/' + mode6_second + '.Q'
            if os.path.exists(mode6_second_path):
                with open(mode6_first_path, 'a', encoding='UTF-8') as mode6_linking:
                    mode6_linking.write(mode6_second + '\n')
                print('successfully linked')
            else:
                print('wrong address')
        else:
            print('wrong address')
    elif mode == '7':
        for mode7_brute in full_r:
            mode7_path = 'ideas/ide' + mode7_brute + '.J'
            try:
                with open(mode7_path, encoding='UTF-8') as mode7_showing:
                    print('')
                    print('ide' + mode7_brute + '.J' + ':')
                    print(mode7_showing.read())
            except FileNotFoundError:
                pass
    elif mode == '8':
        mode8_link = input('''input an address for deleting: ''')
        mode8_path = 'ideas/ide' + mode8_link + '.J'
        if os.path.exists(mode8_path):
            os.remove(mode8_path)
            print('successfully deleted')
        else:
            print('wrong address')
    elif mode == '9':
        path = []
        file = []
        contents = []
        count = {}
        adding = []
        element = []
        for i in range(1, 1001):
            path.append(list())
            file.append(list())
            contents.append(list())
            adding.append(list())
            element.append(list())
        for fir in r:
            for sec in r:
                brute_force = fir + sec
                path_index = 0
                path[path_index] = 'dependencies/X/' + brute_force + '.X'
                file_index = 0
                contents_index = 0
                current_chain = []
                try:
                    with open(path[path_index], encoding='UTF-8') as file[file_index]:
                        contents[contents_index] = (file[file_index].read().splitlines())
                    current_chain.append(brute_force)
                    print(current_chain)
                    adding_index = 0
                    if brute_force not in count:
                        count[brute_force] = 1
                    else:
                        adding[adding_index] = count.get(brute_force)
                        adding[adding_index] += 1
                        count[brute_force] = adding[adding_index]
                    if len(contents[contents_index]) == 0:
                        pass
                    else:
                        element_index = -1
                        def recursio(element_index, path_index, file_index, adding_index, contents_index):
                            element_index += 1
                            path_index += 1
                            file_index += 1
                            adding_index += 1
                            for element[element_index] in contents[contents_index]:
                                try:
                                    while 1:
                                        path[path_index] = 'dependencies/X/' + element[element_index] + '.X'
                                        contents_index += 1
                                        with open(path[path_index], encoding='UTF-8') as file[file_index]:
                                            contents[contents_index] = (file[file_index].read().splitlines())
                                        if element[element_index] in current_chain:
                                            contents_index -= 1
                                            break
                                        else:
                                            current_chain.append(element[element_index])
                                            print(current_chain)
                                            if element[element_index] not in count:
                                                count[element[element_index]] = 1
                                            else:
                                                adding[adding_index] = count.get(element[element_index])
                                                adding[adding_index] += 1
                                                count[element[element_index]] = adding[adding_index]
                                            if len(contents[contents_index]) == 0:
                                                contents_index -= 1
                                            else:
                                                recursio(element_index, path_index, file_index, adding_index,
                                                         contents_index)
                                            current_chain.remove(element[element_index])
                                            break
                                except FileNotFoundError:
                                    while 1:
                                        print("EVERYTHING WENT WRONG")
                            adding_index -= 1
                            file_index -= 1
                            path_index -= 1
                            element_index -= 1
                        recursio(element_index, path_index, file_index, adding_index, contents_index)
                except FileNotFoundError:
                    pass
        print(count)
        k = 1
        for k in range(1, 100001):
            for xx, yy in count.items():
                if yy == k:
                    print(xx, yy)
    elif mode == 'e':
        break
    else:
        print('wrong input')
