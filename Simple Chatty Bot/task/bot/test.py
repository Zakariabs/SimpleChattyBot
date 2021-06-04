

def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('''Is Python case sensitive when dealing with identifiers?
    1. yes
    2. no
    3. machine dependent
    4. none of the mentioned
    ''')

    while True:
        answer = int(input())
        value = answer
        if value != 1:
            print('Please, try again.')
            continue
        else:
            print('Completed, have a nice day!')

test()