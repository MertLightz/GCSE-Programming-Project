#GCSE Programming Project

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

def start_menu():
    print('[' + '=' * 50 + ']')
    print('[{:^50}]'.format('1 - login   '))
    print('[{:^50}]'.format('2 - register'))
    print('[{:^50}]'.format('3 - quit    '))
    print('[' + '=' * 50 + ']')
    print()
    return

def get_option():
    try:
        option = int(input('enter: '))
    except:
        error('invalid data type')
        start()
    return option

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

start()