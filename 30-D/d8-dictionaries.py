phonebook = {}


def getInput():
    user_input = input().split()
    phonebook[user_input[0]] = user_input[1]


def query():
    query_input = input()
    if query_input in phonebook:
        print("{name}={number}".format(
            name=query_input, number=phonebook[query_input]))
    else:
        print("Not found")


if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        getInput()
    while True:
        try:
            query()
        except EOFError:
            break
