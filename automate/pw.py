#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'email_password',
        'blog': 'blog_password',
        'luggage': 12345}

# Handling Command Line Arguments.

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line argument is the account name.

# Copy the right password.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
