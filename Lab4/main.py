from test import stringcheck, grammarcheck

if __name__ == "__main__":

    c = int(input("Enter the number of LHS variables..\n"))

    for i in range(c):
        if grammarcheck(i):
            t = True
        else:
            t = False
            break

    if t:
        print("Grammar is accepted")
        if (stringcheck()):
            print("String is accepted")
        else:
            print("String is not accepted")

    else:
        print("Grammar is not accepted ")
