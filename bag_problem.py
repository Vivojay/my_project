import sys

def bags(a, b):
    a = int(a)
    b = int(b)

    if a % b == 0:
        return int(a/b)
    else:
        return int(a/b)+1

if __name__ == '__main__':
    print(bags(sys.argv[1], sys.argv[2]))

