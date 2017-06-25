
# pyperclip takes things off the clipboard
import webbrowser, sys, pyperclip

#webbrowser.open('https://www.rotogrinders.com')

sys.argv

#the first command line arg is always the name of the file, so...
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)
