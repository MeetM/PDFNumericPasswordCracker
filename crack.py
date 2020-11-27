from pikepdf import Pdf
import argparse
import re

def crack_password(digits, filename, pattern):
    n = 1
    n_max = 9999999999999999999 % (10**digits)
    while n < n_max + 1:
        pn = str(n).zfill(digits)
        if pattern is None or pattern.match(pn):
            try:
                Pdf.open(filename_or_stream = filename, password = pn)
                print("Password is " + pn)
                return True
            except:
                # incorrect password
                pass
        n += 1
    return False

# Parse Commandline Args
parser = argparse.ArgumentParser(description='Crack numeric passwords of PDFs')
parser.add_argument('filename', help="Full path of the PDF file")
parser.add_argument('-m', '--min-digits', help="Minimum digits in the password", type=int, default="1")
parser.add_argument('-n', '--max-digits', help="Maximum digits in the password", type=int, default="-1")
parser.add_argument('-r', '--matching-regex', help="Skip passwords not matching regex", type=str, default=None)
args = parser.parse_args()

# Check and fix min and max digit values
max_digits = args.max_digits
min_digits = args.min_digits
if max_digits < min_digits:
    max_digits = min_digits

# Compile and print regex if provided
pattern = None
if args.matching_regex is not None:
    pattern = re.compile(args.matching_regex)
    print('Skipping passwords not matching:', args.matching_regex)

# Iterate
digits = min_digits
found_password = False
print("Cracking. Please wait...")
while not found_password and digits <= max_digits:
    print("Trying to crack using " + str(digits) + " digit passwords")
    found_password = crack_password(digits, args.filename, pattern)
    digits += 1
if not found_password:
    print("Could not crack the password")