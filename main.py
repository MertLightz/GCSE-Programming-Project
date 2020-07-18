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