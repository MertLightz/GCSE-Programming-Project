#GCSE Programming Project
import time
import random
import requests
global input_username

########################Used Globally########################

def enter_to_continue():
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format('press enter to continue'))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)

    input()
    return

def blank_page():
    for i in range(0,100):
        print()
    return

def message(abc):
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format(abc))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    return

def welcome():
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format('welcome'))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    return

def get_option():
    try:
        option = int(input('enter: '))
    except:
        blank_page()
        message('invalid data type')
        print()
        enter_to_continue()
        start()
    return option

########################Used for Start Menu##################

def checks():
    for i in range(0,3):
        blank_page()
        if i == 0:
            file_name = 'users.txt'
        elif i == 1:
            file_name = 'leaderboard.txt'
        elif i == 2:
            file_name = 'songs.txt'
            
        message('checking for ' + file_name)
        time.sleep(1)
        blank_page()
    
        try:
            with open(file_name, 'r') as file:
                pass
        except:
            with open(file_name, 'w') as file:
                pass
            if i == 2:
                try:
                    url = 'https://raw.githubusercontent.com/MertLightz/GCSE-Programming-Project/master/songs.txt'
                    r = requests.get(url, allow_redirects = True)
                    open('songs.txt', 'wb').write(r.content)
                    message('downloading songs.txt from GitHub')
                    time.sleep(1)
                except:
                    message('unable to download songs.txt due to WiFi issues')
                    time.sleep(1)
            else:
                message('created ' + file_name)
                time.sleep(1)

def start_menu():
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format('1 - login   '))
    time.sleep(0.1)
    print('[{:^50}]'.format('2 - register'))
    time.sleep(0.1)
    print('[{:^50}]'.format('3 - quit    '))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print()
    time.sleep(0.1)
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
        blank_page()
        message('invalid option')
        print()
        enter_to_continue()
        start()

########################Used for Login#######################

def login():
    blank_page()
    with open('users.txt', 'r') as users:
        if users.readlines() == []:
            message('users.txt is empty')
            print()
            enter_to_continue()
            start()
            
    global input_username
    blank_page()
    valid = False
    
    message('login')
    print()
    message('enter username and password')
    print()

    input_username = input('username: ')
    time.sleep(0.1)
    input_password = input('password: ')
    time.sleep(0.1)

    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            
            if input_username == new_line[0] and input_password == new_line[1]:
                valid = True
                break
    
    blank_page()
    if valid == True:
        message('successfully logged in')
        print()
        enter_to_continue()
        main()
    else:
        message('invalid username or password')
        print()
        enter_to_continue()
        start()

########################Used for Register####################      

def register():
    blank_page()

    message('register')
    print()
    time.sleep(0.1)
    message('enter username and password')
    print()
    time.sleep(0.1)

    input_username = input('username: ')
    time.sleep(0.1)
    
    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            if new_line[0] == input_username:
                blank_page()
                message('username is taken')
                print()
                enter_to_continue()
                start()
                
    input_password = input('password: ')
    time.sleep(0.1)

    if input_password.strip(' ') == '':
        blank_page()
        message('password cannot be blank')
        print()
        enter_to_continue()
        start()
        
    print()
    time.sleep(0.1)

    message('confirm password')
    print()
    confirm_password = input('confirm password: ')

    if input_password != confirm_password:
        blank_page()
        message('passwords do not match')
        print()
        enter_to_continue()
        start()
    
    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            if new_line[0] == input_username:
                blank_page()
                message('username is taken')
                print()
                enter_to_continue()
                start()
    
    with open('users.txt', 'a') as users:
        users.write(input_username + ',' + input_password + '\n')

    blank_page()
    message('registered')
    print()
    enter_to_continue()
    start()

########################Used for Main Menu###################

def main_menu():
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format('1 - play game  '))
    time.sleep(0.1)
    print('[{:^50}]'.format('2 - rules      '))
    time.sleep(0.1)
    print('[{:^50}]'.format('3 - leaderboard'))
    time.sleep(0.1)
    print('[{:^50}]'.format('4 - quit       '))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    return

def main():
    blank_page()
    welcome()
    main_menu()
    option = get_option()

    if option == 1:
        play()
    elif option == 2:
        rules()
    elif option == 3:
        leaderboard()
    elif option == 4:
        quit()
    else:
        blank_page()
        message('invalid option')
        print()
        enter_to_continue()
        main()

########################Used for Rules#######################

def rules():
    blank_page()

    message('rules')

    print()
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print('[{:^50}]'.format('1 - you have 2 chances to guess  '))
    time.sleep(0.1)
    print('[{:^50}]'.format('2 - correct 1st time   = 3 points'))
    time.sleep(0.1)
    print('[{:^50}]'.format('3 - correct 2nd time   = 1 points'))
    time.sleep(0.1)
    print('[{:^50}]'.format('4 - incorrect 2nd time = lose    '))
    time.sleep(0.1)
    print('[' + '=' * 50 + ']')
    time.sleep(0.1)
    print()
    time.sleep(0.1)

    enter_to_continue()
    main()

########################Used for Leaderboard#################

def leaderboard():
    blank_page()
    with open('leaderboard.txt', 'r') as leaderboard:
        if leaderboard.readlines() == []:
            message('leaderboard.txt is empty')
            print()
            enter_to_continue()
            main()
            
    message('leaderboard')

    print()
    time.sleep(0.1)
    print('[' + '=' * 51 + ']')
    time.sleep(0.1)
    print('[{:^25}|{:^25}]'.format('name', 'score'))
    time.sleep(0.1)
    print('[' + '=' * 51 + ']')
    time.sleep(0.1)
    
    empty_list = []
    with open('leaderboard.txt', 'r') as leaderboard:
        for each_line in leaderboard:
            new_line = each_line.strip('\n').split(',')
            empty_list.append(new_line)
    
    show = sorted(empty_list, key = lambda x:int(x[1]), reverse = True)

    count = 0

    for eachScore in show:
        print("[{:^25}|{:^25}]".format(eachScore[0], eachScore[1]))
        time.sleep(0.1)
        print("[" + "=" * 51 + "]")
        time.sleep(0.1)
        count = count + 1
        if count == 5:
            break

    print()
    enter_to_continue()
    main()

########################Used for Game########################

def add_to_leaderboard(input_username, points):
    with open('leaderboard.txt', 'a') as leaderboard:
        leaderboard.write(input_username + ',' + str(points) + '\n')

def get_number_of_songs():
    number_of_songs = 0
    with open('songs.txt', 'r') as songs:
        for each_line in songs:
            number_of_songs += 1
    return number_of_songs

def get_new_song(number_of_songs,already_selected):
    random_song = random.randint(0, number_of_songs - 1)
    while random_song in already_selected:
        random_song = random.randint(0, number_of_songs - 1)

    with open('songs.txt', 'r') as songs:
        for each_line in songs:
            new_line = each_line.strip('\n').split(',')
            if int(new_line[0]) == random_song:
                break
    already_selected.append(random_song)
    return new_line[1],new_line[2],new_line[3]

def play():
    blank_page()
    with open('songs.txt', 'r') as songs:
        if songs.readlines() == []:
            message('songs.txt is empty')
            print()
            enter_to_continue()
            main()
    already_selected = []
    points = 0

    blank_page()
    message('starting game...')
    blank_page()

    number_of_songs = get_number_of_songs()

    new_song = True
    check = False
    while check == False:
        if number_of_songs == len(already_selected):
          blank_page()
          message('you have beaten the game')
          print()
          break
            
        if new_song == True:
            current_artist,current_song,hidden_song = get_new_song(number_of_songs,already_selected)

        for i in range(0,2):
            blank_page()
            
            print('[' + '=' * 51 + ']')
            time.sleep(0.1)
            print('[{:^25}|{:^25}]'.format('points', points))
            time.sleep(0.1)
            print('[' + '=' * 51 + ']')
            time.sleep(0.1)
            print()
            time.sleep(0.1)
            
            print('[' + '=' * 51 + ']')
            time.sleep(0.1)
            print('[{:^25}|{:^25}]'.format(current_artist, hidden_song))
            time.sleep(0.1)
            print('[' + '=' * 51 + ']')
            time.sleep(0.1)
            print()
            time.sleep(0.1)

            player_answer = input('Song Name: ').lower().replace(' ', '')
            blank_page()
            current_song = current_song.lower().replace(' ', '')
            
            if player_answer == current_song and i == 0:
                message('correct, you gained 3 points')
                print()
                enter_to_continue()
                points += 3
                i = 0
                break
            
            elif player_answer == current_song and i == 1:
                message('correct, you gained 1 points')
                print()
                enter_to_continue()
                points += 1
                i = 0
                new_song = True
                
            elif player_answer != current_song and i == 1:
                message('incorrect, you have lost')
                print()
                check = True
                
            else:
                message('incorrect')
                print()
                enter_to_continue()
                new_song = False

    message('adding to leaderboard')
    print()
    add_to_leaderboard(input_username, points)
    enter_to_continue()
    main()

checks()
start()
