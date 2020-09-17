# Alert

> Category: misc  
> Suggested Points: 75

# Description
> A simple image steganography challenge. Goal is to display the full image to find the hidden flag.

# Deployment
> Release alert.png

# Flag
> flag{sT@y_s@F3}

# Solution
> Use a hex editor to modify the image's height. Change "01 18" to "02 58", which is the same value as width.  
> Run "pngcheck -vf alert.png"  
> There is a error message: "CRC error in chunk IHDR (computed be6698dc, expected 80d6882d)"  
> Open the hex editor again and change "80d6882d" to "be6698dc"  
> Open the PNG and find the flag  
