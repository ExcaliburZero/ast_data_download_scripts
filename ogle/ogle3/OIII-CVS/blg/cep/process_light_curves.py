import os
import subprocess

def main():
    curve_directories = ["curves/I/", "curves/V/"]

    [process_dir(d) for d in curve_directories]

def process_dir(directory):
    [process_file(directory, f) for f in sorted(os.listdir(directory))]

def process_file(directory, f):
    """
    1) Add the header
    2) Remove excess spacing
    3) Replace delimiting spaces with commas
    4) Remove any commas at the end of lines
    5) Remove any commas at beginning of lines
    """
    f = f[:-4]
    f = os.path.join(directory, f)

    print(f)

    command = "echo 'time,mag,magerror' > '%s.csv' && cat '%s.dat' | tr -s ' ' | sed 's/ /,/g' | sed 's/,$$//g' | sed 's/^,//g' >> '%s.csv'" % (f, f, f)

    subprocess.call(command, shell=True)

if __name__ == "__main__":
    main()
