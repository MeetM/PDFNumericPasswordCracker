# PDF Numeric Password Cracker
- Cracks PDFs with number password with optional fixed prefix
- Technique used - Brute Force

## Requirements
Requires Python 3.* and pikepdf
```sh
pip install pikepdf
``` 
## Usage
```sh
python crack.py PATH_TO_PDF_FILE [-m MIN_DIGITS] [-n MAX_DIGITS] [-r MATCHING_REGEX] [-p PREFIX]
``` 

Example 1 - If the password is between 3 to 5 digits long
```sh
python crack.py /home/elliot/Desktop/file.pdf -m 3 -n 5
```

Example 2 - Same as above, but tests passwords containing the digits 1-3 **only**
```sh
python crack.py /home/elliot/Desktop/file.pdf -m 3 -n 5 -r ^[1-3]+$
```

Example 3 - If the password is between 3 to 5 digits long but starts with 'abc'
```sh
python crack.py /home/elliot/Desktop/file.pdf -m 3 -n 5 -p abc
```

#### This is for educational purpose only, and may not work on all .pdf files.
