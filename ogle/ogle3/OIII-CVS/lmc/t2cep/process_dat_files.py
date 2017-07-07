import pandas as pd
import subprocess

def main():
    dat_files = ["t2cep"]

    cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "period", "period_uncertainty", "time_max_bright", "I_amplitude", "R21", "phi21", "R31", "phi31"]

    column_sets = [cols, cols, cols]
 
    [dat_to_csv(dat, columns) for (dat, columns) in zip(dat_files, column_sets)]

def dat_to_csv(dat, columns):
    data = pd.read_fwf(dat + ".dat", header=None)

    if columns is not None:
        data.columns = columns
        
        data.to_csv(dat + ".csv", index=False)
    else:
        data.to_csv(dat + ".csv", index=False, header=False)

    remove_empty_cells(dat)

def remove_empty_cells(dat):
    """
    Remove all instances of "-"s indicating missing values, as csv files
    represent missing values as blank entries.
    """
    f = dat
    command = "cat '%s.csv' | sed 's/,-/,/g' > '%s_2.csv' && cat %s_2.csv > %s.csv && rm %s_2.csv" % (f, f, f, f, f)

    print(command)
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    main()
