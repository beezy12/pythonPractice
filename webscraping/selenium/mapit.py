#! python 3

# this programe allows the user to either enter an address at the command line,
# or just copy an address to the clipboard and then run this program to 
# have google maps open up and display the address on the map

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else: 
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/'+ address) 
