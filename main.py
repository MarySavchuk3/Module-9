contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'User with this name is not available.'
        except ValueError:
            return 'Name and phone are not available.'
        except IndexError:
            return 'Name and phone are not available.'

    return inner


def hello(_):
    return 'How can I help you?'


@input_error
def add(contact):
    name, phone, *_ = contact
    contacts[name] = phone
    return f'Number {phone} with name {name} was added.'


@input_error
def change(contact):
    name, phone, *_ = contact
    for key in contacts:
        if key == name:
            contacts[key] = phone
            return f'Number {phone} with name {name} was changed.'
        else:
            return f'Number {phone} with name {name} does not exist.'


@input_error
def phone(contact):
    return f'{contact} number is {contacts[contact[0]]}.'


def show_all(_):
    if contacts:
        result = ''
        for name, phone in contacts.items():
            result += f'{name} : {phone} \n'
        return result
    else:
        return 'There are no contacts.'


def bye(_):
    return 'Good bye!'


def unknown_action(_):
    return 'This command is not available'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': bye,
    'exit': bye,
    'close': bye
}


def handler_input(input):
    input = input.lower().split(' ')
    command = input[0]
    if command in ('show', 'good'):
        command += ' ' + input[1]
    info = input[1:]
    try:
        handler = COMMANDS[command]
    except KeyError:
        handler = unknown_action
        if not command or command == '.':
            handler = bye
    return handler, info


def main():
    print('Please enter one of this commands: hello, add (name phone), change (name phone), phone (phone), show all.')
    print('Please enter input good bye, close, exit if you want to stop')
    while True:
        command = input('Enter command: ')
        handler, info = handler_input(command)
        try:
            result = handler(info)
            print(result)
            if result == 'Good bye!':
                exit()
        except KeyError:
            print('This command is not available')


main()
