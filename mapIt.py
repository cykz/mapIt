#!/usr/bin/env python3

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:]) #get address from command line

else:
  address = pyperclip.paste() #get address from clipboard

webbrowser.open('https://www.google.com/maps/place/' + address)
