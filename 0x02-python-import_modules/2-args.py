#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    i = 1
    args = len(argv) - 1

    print(f"{args} {'argument' if args == 1 else 'arguments'}", end="")
    print(f"{'.' if args == 0 else ':'}")
    while (i <= args):
        print(f"{i}: {argv[i]}")
        i += 1
