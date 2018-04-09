
#! python3

# this program simulates a password storage app
# enter account name at the command line for the password you want
# takes a command line argument for the account name
# and copies the password to the clipboard using pyperclip

import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('just copied your ' + account + ' to the clipboard')
else:
    print('there is no account named ' + account)
