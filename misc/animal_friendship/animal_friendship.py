#!/usr/bin/python3
def main():
    print("*** Animal Friendship ***\n")
    print("To get the flag, answer this question:\n")
    print("What sort of creature is Domo's friend? ",end='')
    try:
        answer = input()
    except:
        print("Error during receiving input. Program will exit.")
        exit(0)
    acceptable_answers = {"chipmunk","Chipmunk","CHIPMUNK"}
    mostly_acceptable_answers = {"gopher","Gopher","GOPHER","gerbil","Gerbil","GERBIL", "squirrel", "SQUIRREL", "Squirrel", "Dormouse", "dormouse", "DORMOUSE", "MOUSE", "mouse", "Mouse", "rodent", "Rodent", "RODENT"}
    if answer in acceptable_answers:
        print("\nYep, that's it!")
    elif answer in mostly_acceptable_answers:
        print("\nClose enough! We think it's a chipmunk, but guessing the animal isn't part of the challenge.")
    else:
        print("\nNope!")
        exit(0)
    print("\nflag{m4k1n9_f0r3n51c5_53c0nd_n47ur3}")

main()