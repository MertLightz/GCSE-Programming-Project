#GCSE Programming Project

########################Used Globally########################

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

########################Used for Start Menu##################

def get_option():
    try:
        option = int(input('enter: '))
    except:
        message('invalid data type')
        start()
    return option

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
    
start()