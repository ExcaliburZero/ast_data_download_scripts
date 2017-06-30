import os
import subprocess

def main():
    curve_directories = ["curves/"]

    [process_dir(d) for d in curve_directories]

def process_dir(directory):
    [process_file(directory, f) for f in os.listdir(directory)]

def process_file(directory, f):
    """
    Converts the .time light curve files into .csv files for easier parsing.

    1) Remove first 3 lines
    2) Remove # comment on header line
    3) Remove excess spacing
    4) Replace separtaing spaces with commas
    5) Remove extra comma at the start of each line
    6) Remove line ending commas on non-header lines

    process_lc_file = cat "$(1).time" | tail -n +4 | sed 's/\#/ /g' | tr -s ' ' | sed 's/ /,/g' | cut -c 2- | sed 's/,$$//g' > "$(1).csv"
    """
    f = os.path.splitext(f)[0]
    print(f)
    f = os.path.join(directory, f)

    command = "echo 'time,mag,magerror' > '%s.csv' && cat '%s.time' | tail -n +4 | sed 's/\#/ /g' | tr -s ' ' | sed 's/ /,/g' | cut -c 2- | sed 's/,$//g' >> '%s.csv'" % (f, f, f)

    subprocess.call(command, shell=True)

if __name__ == "__main__":
    main()
