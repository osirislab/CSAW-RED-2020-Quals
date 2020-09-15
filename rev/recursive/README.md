# Recursive
- Category: rev 
- Suggested Points: 
- Distribute:

# Description
Reversing challenge testing the player's understand of how recursive functions and passing by reference in C programs. Players also have to keep track of a number of variables used multiple times throughout the program.

# Deployment
n/a (I think)

# Flag
flag{r3Curs1Ve_Rev3rSe}

# Solution

## 5 variables used through main
- a: used to store the returned value from the recursive function f
- b: counter to capture the number of times f is called
- c: size of the buffer to read in the flag
- d: size of the buffer to read in the user input
- e: stores the int conversion of the user input string

## Steps
1. User is prompted to enter a number between 1 and 99999
2. If valid, sent into the recursive function f, which divides the user input by 2 until it can't anymore. b is passed in by reference to capture the number oof times divided.
3. Program tests if the the number of times divided is 7 and the returned value + the number of divisions = the difference in the size of the buffer. If so, the flag is printed.

## Answer
If c-d = 18 and b = 7 then a = c - b is 11. 2^7 * 11 = 1408.

# Potential Breakage
