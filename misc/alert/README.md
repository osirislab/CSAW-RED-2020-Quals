# Alert

> Category: misc  
> Suggested Points: 150

# Description
> A simple image steganography challenge. Goal is to display the full image to find the hidden flag.

# Deployment
> Release alert.png

# Flag
> flag{sT@y_s@F3}

# Solution
> \* A brief explanation of PNG file structure: https://stackoverflow.com/a/30551737  
> 1. Use a hex editor to modify the image's height. In the IHDR chunk, we can see that the current height of the image is "01 18" and the width is "02 58". Since this image is square, we need to change the height to "02 58".  
> 2. Run "pngcheck -vf alert.png".  
> 3. There is an error message: "CRC error in chunk IHDR (computed be6698dc, expected 80d6882d)".  
> 4. Open the hex editor again. In the IHDR chunk, find the number "80d6882d" and change it to "be6698dc".  
> 5. Open the PNG and find the flag.  
