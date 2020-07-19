#GCSE Programming Project

########################Used Globally########################

def blank_page():
    for i in range(0,100):
        print()
    return

def error(message):
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format(message))
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
        error('invalid data type')
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
        error('invalid option')
        start()

########################Used for Login#######################

def login():
    blank_page()
    valid = False
    
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('login'))
    print('[' + '=' * 50 + ']')
    print()
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('enter username and password'))
    print('[' + '=' * 50 + ']')
    print()

    input_username = input('username: ')
    input_password = input('password: ')

    with open('users.txt', 'r') as users:
        for each_line in users:
            new_line = each_line.strip('\n').split(',')
            username = new_line[0]
            password = new_line[1]
            
            if input_username == username and input_password == password:
                valid = True
                break
    
    blank_page()
    if valid == True:
        print('[' + '=' * 50 + ']')
        print('[{:^50}]'.format('successfully logged in'))
        print('[' + '=' * 50 + ']')
        main()
    else:
        print('[' + '=' * 50 + ']')
        print('[{:^50}]'.format('username or password is invalid'))
        print('[' + '=' * 50 + ']')
        start()
        
start()