# Super_Sonic

> Category: misc  
> Suggested Points: 75

# Description
> A basic stegonography challenge. Goal is to find the flag.

# Deployment
> Release super_sonic.zip

# Flag
> flag{py1h0n_1s_c00l}

# Solution
> 1. Open the audio file in a forensic audio visualizer. There are many open source tools that can be used for this.  
> 2. Any internet search would help extracting a text from the audio file
> 3. Once the text is extracted, it's used as a passphrase for a basic stegonography on the image: Car.jpeg
> 4. Again, any open source tool would help extracting a file from an image file, when asked for a passphrase enter the passphrase received from the audio file
