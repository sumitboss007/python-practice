def main():
    x = int(input("What's x ? "))
    if is_odd(x):
        print('ODD')
    else:
        print('EVEN')
        
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
main()