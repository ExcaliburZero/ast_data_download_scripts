"""
Separates the light curves for the CRTS release 2 into their own files.
"""
from __future__ import print_function
import os.path
import sys

def main():
    """
    Checks for proper command line arguments and then processes the file.
    """
    if (len(sys.argv) != 2):
        eprint("Need name of file to process.")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if (os.path.isfile(filename)):
            process_file(filename)
        else:
            eprint("The given file does not exist: " + filename)
            sys.exit(1)

def process_file(filename):
    """
    Separates the given data file into separate files for each light curve.
    """
    is_header = True
    header = "time,mag,magerr\n"
    os.makedirs("curves")
    with open(filename) as f:
        for line in f:
            if is_header:
                is_header = False
            else:
                star_id = line.split(",")[0]
                filename = create_filename(star_id)
                entry = create_entry(line)
                append_line(filename, header, entry)

def create_entry(line):
    parts = line.split(",")

    return "%s,%s,%s\n" % (parts[1], parts[2], parts[3])

def append_line(filename, header, content):
    """
    Appends the given content line to the end of the given file. Also adds the
    header line to the file if it has not yet been created.
    """
    if not os.path.isfile(filename):
        with open(filename, "a") as f:
            f.write(header)
            f.write(content)

    else:
        with open(filename, "a") as f:
            f.write(content)

def create_filename(star_id):
    """
    Creates the file name for the given star id. This is used to keep the
    naming consistent throughout and easier to change.
    """
    return "curves/" + star_id + ".csv"

def eprint(*args, **kwargs):
    """
    Prints the given message to stderr.
    """
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    main()
