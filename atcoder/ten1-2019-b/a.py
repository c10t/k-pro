
def main():
    a, b, c = map(int, input().split())
    if a < c:
        print('Yes' if a < c < b else 'No')
    else:
        print('Yes' if b < c < a else 'No')


main()
