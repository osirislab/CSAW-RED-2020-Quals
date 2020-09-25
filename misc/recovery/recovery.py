#!/usr/bin/python3
def main():
    print("*** Recovery ***\n")
    print("To get the flag, answer this question:\n")
    print("What is Alice's email address? ",end='')
    try:
        answer = input()
    except:
        print("Error during receiving input. Program will exit.")
        exit(0)
    acceptable_answers = {"alice_test@hotmail.com"}
    if answer in acceptable_answers:
        print("\nYep, that's it!")
    else:
        print("\nNope!")
        exit(0)
    print("\nflag{W1r3sh4rk,TCPfl0w,gr3p,57r1n95--7h3y'r3_4ll_f0r3n51c5_700l5}")

main()