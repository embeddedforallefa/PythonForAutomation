import sys

while True:
    print("Type exit ti exit.")
    response = input()
    if response == 'exit':
        sys.exit()
        print("you typed" + response + ".")
