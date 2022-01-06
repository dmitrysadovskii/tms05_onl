def programme_ing(s):
    custom_string = ''
    for word in s.split():
        custom_string += word + 'ing '

    print(custom_string)


programme_ing('say hello everyone')
