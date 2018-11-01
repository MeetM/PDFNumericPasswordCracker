from pikepdf import Pdf
import argparse

def crack_password(digits, filename):
    n = 1
    n_max = 9999999999999999999 % (10**digits)
    while n < n_max + 1:
        pn = str(n).zfill(digits)
        try:
            sample_pdf = Pdf.open(filename_or_stream = filename, password = pn)
            print("Password is " + pn)
            return True
        except:
            n += 1
            continue
    return False

# Parse Commandline Args
parser = argparse.ArgumentParser(description='Crack numeric passwords of PDFs')
parser.add_argument('filename', help="Full path of the PDF file")
parser.add_argument('-m', '--min-digits', help="Minimum digits in the password", type=int, default="1")
parser.add_argument('-n', '--max-digits', help="Maximum digits in the password", type=int, default="-1")
args = parser.parse_args()

# Check and fix min and max digit values
max_digits = args.max_digits
min_digits = args.min_digits
if max_digits < min_digits:
    max_digits = min_digits

# Iterate
digits = min_digits
found_password = False
print("Cracking. Please wait...")
while not found_password and digits <= max_digits:
    print("Trying to crack using " + str(digits) + " digit passwords")
    found_password = crack_password(digits, args.filename)
    digits += 1
if not found_password:
    print("Could not crack the password")