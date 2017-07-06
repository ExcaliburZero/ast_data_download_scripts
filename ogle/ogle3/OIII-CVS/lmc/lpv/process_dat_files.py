import pandas as pd
import subprocess

def main():
    dat_files = ["Miras", "SRVs", "OSARGs"]

    cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "primary_period", "primary_I_amplitude", "secondary_period", "secondary_I_amplitude", "tertiary_period", "tertiary_I_amplitude"]

    column_sets = [cols, cols, cols]
 
    [dat_to_csv(dat, columns) for (dat, columns) in zip(dat_files, column_sets)]

    combine_dat_files(dat_files)

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

def combine_dat_files(dat_files):
    miras_dat = pd.read_csv(dat_files[0] + ".csv")
    srvs_dat = pd.read_csv(dat_files[1] + ".csv")
    osargs_dat = pd.read_csv(dat_files[2] + ".csv")

    miras_dat = miras_dat[["id", "primary_period"]]
    miras_dat.columns = ["id", "period"]
    miras_dat["category"] = "MIRA"

    srvs_dat = srvs_dat[["id", "primary_period"]]
    srvs_dat.columns = ["id", "period"]
    srvs_dat["category"] = "SRV"

    osargs_dat = osargs_dat[["id", "primary_period"]]
    osargs_dat.columns = ["id", "period"]
    osargs_dat["category"] = "OSARG"

    all_dat = pd.concat([miras_dat, srvs_dat, osargs_dat])

    all_dat.to_csv("all.csv", index=False)

if __name__ == "__main__":
    main()
