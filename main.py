#GCSE Programming Project

import random

########################Used Globally########################

def enter_to_continue():
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('press enter to continue'))
    print('[' + '=' * 50 + ']')

    input()
    return

def blank_page():
    for i in range(0,100):
        print()
    return

def message(abc):
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format(abc))
    print('[' + '=' * 50 + ']')
    return

def welcome():
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('welcome'))
    print('[' + '=' * 50 + ']')
    print()
    return

def get_option():
    try:
        option = int(input('enter: '))
    except:
        message('invalid data type')
        start()
    return option

########################Used for Start Menu##################

def start_menu():
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('1 - login   '))
    print('[{:^50}]'.format('2 - register'))
    print('[{:^50}]'.format('3 - quit    '))
    print('[' + '=' * 50 + ']')
    print()
    return

def start():
    blank_page()
    welcome()
    start_menu()
    option = get_option()

    if option == 1:
        login()
    if option == 2:
        register()
    if option == 3:
        quit()
    else:
        message('invalid option')
        start()

########################Used for Login#######################

def login():
    blank_page()
    valid = False
    
    message('login')
    print()
    message('enter username and password')
    print()

    input_username = input('username: ')
    input_password = input('password: ')

    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            
            if input_username == new_line[0] and input_password == new_line[1]:
                valid = True
                break
    
    blank_page()
    if valid == True:
        message('successfully logged in')
        main()
    else:
        message('invalid username or password')
        start()

########################Used for Register####################      

def register():
    blank_page()

    message('register')
    print()
    message('enter username and password')
    print()

    input_username = input('username: ')
    input_password = input('password: ')
    print()

    message('confirm password')
    print()
    confirm_password = input('confirm password: ')

    if input_password != confirm_password:
        blank_page()
        message('passwords do not match')
        start()
    
    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            if new_line[0] == input_username:
                blank_page()
                message('username is taken')
                start()
    
    with open('users.txt', 'a') as users:
        users.write(input_username + ',' + input_password + '\n')

    message('registered')
    start()

########################Used for Main Menu###################

def main_menu():
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('1 - play game  '))
    print('[{:^50}]'.format('2 - rules      '))
    print('[{:^50}]'.format('3 - leaderboard'))
    print('[' + '=' * 50 + ']')
    print()
    return

def main():
    blank_page()
    welcome()
    main_menu()
    option = get_option()

    if option == 1:
        play()
    if option == 2:
        rules()
    if option == 3:
        leaderboard()
    else:
        message('invalid option')
        main()

########################Used for Rules#######################

def rules():
    blank_page()

    message('rules')

    print()
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('1 - you have 2 chances to guess  '))
    print('[{:^50}]'.format('2 - correct 1st time   = 3 points'))
    print('[{:^50}]'.format('3 - correct 2nd time   = 1 points'))
    print('[{:^50}]'.format('4 - incorrect 2nd time = lose    '))
    print('[' + '=' * 50 + ']')
    print()

    enter_to_continue()

########################Used for Leaderboard#################

def leaderboard():
    blank_page()
    message('leaderboard')

    print()
    print('[' + '=' * 51 + ']')
    print('[{:^25}|{:^25}]'.format('name', 'score'))
    print('[' + '=' * 51 + ']')
    
    empty_list = []
    with open('leaderboard.txt', 'r') as leaderboard:
        for each_line in leaderboard:
            new_line = each_line.strip('\n').split(',')
            empty_list.append(new_line)
    
    show = sorted(empty_list, key = lambda x:int(x[1]), reverse = True)

    count = 0

    for eachScore in show:
        print("[{:^25}|{:^25}]".format(eachScore[0], eachScore[1]))
        print("[" + "=" * 51 + "]")
        count = count + 1
        if count == 5:
            break

    print()
    enter_to_continue()

########################Used for Game########################

def get_number_of_songs():
    number_of_songs = 0
    with open('songs.txt', 'r') as songs:
        for each_line in songs:
            number_of_songs += 1
    return number_of_songs

def get_new_song(number_of_songs,already_selected):
    random_song = random.randint(0, number_of_songs - 1)
    while random_song in already_selected:
        random_song = random.randint(0, number_of_songs)

    with open('songs.txt', 'r') as songs:
        for each_line in songs:
            new_line = each_line.strip('\n').split(',')
            if int(new_line[0]) == random_song:
                current_artist = new_line[1]
                current_song = new_line[2]
                break
    return random_song,current_artist,current_song

def get_points():
    pass

def play():
    already_selected = []
    points = 0

    blank_page()
    message('starting game...')
    blank_page()

    number_of_songs = get_number_of_songs()

    random_song,current_artist,current_song = get_new_song(number_of_songs,already_selected)
    
    already_selected.append(random_song)
    
    points = get_points()
    
    print('[' + '=' * 51 + ']')
    print('[{:^25}|{:^25}]'.format(current_artist, current_song))
    print('[' + '=' * 51 + ']')

play()