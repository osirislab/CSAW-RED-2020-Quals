#!/usr/bin/python3
def main():
    print("*** otherplane ***\n")
    print("To get the flag, answer this question:\n")
    print("Who did the admin contact? ",end='')
    try:
        answer = input()
    except:
        print("Error during receiving input. Program will exit.")
        exit(0)
    acceptable_answers = {"galactic octopus","Galactic Octopus","Galactic octopus", "galactic_octopus", "GALACTIC OCTOPUS", "galacticoctopus","GALACTICOCTOPUS"}
    answer = answer.replace("\"","")
    answer = answer.replace("\'","")
    if answer in acceptable_answers:
        print("\nYep, that's it! Although in retrospect it's probably the octopus that cast the \"Contact Other Plane\" spell.")
    else:
        print("\nNope!")
        exit(0)
    print("\nflag{m0r3_l1k3_c0n74c7_9l455_pl4n3}")

main()