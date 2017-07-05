import pandas as pd
import subprocess

def main():
    dat_files = ["RRab", "RRc", "RRd", "aRRd"]

    rrab_rrc_cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "period"
        , "period_uncertainty", "time_max_bright", "I_amplitude", "R21"
        , "phi21", "R31", "phi31"]

    rrd_arrd_cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "fo_period"
        , "fo_period_uncertainty", "fo_time_max_bright", "fo_I_amplitude"
        , "fo_R21", "fo_phi21", "fo_R31", "fo_phi31", "fm_period"
        , "fm_period_uncertainty", "fm_time_max_bright", "fo_I_amplitude"
        , "fo_R21", "fo_phi21", "fo_R31", "fo_phi31"]

    column_sets = [
          rrab_rrc_cols
        , rrab_rrc_cols
        , rrd_arrd_cols
        , rrd_arrd_cols
    ]
    [dat_to_csv(dat, columns) for (dat, columns) in zip(dat_files, column_sets)]

    combine_dat_files("RRab", "RRc", "RRd", "aRRd")

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

def combine_dat_files(rrab, rrc, rrd, arrd):
    rrab_dat = pd.read_csv(rrab + ".csv")
    rrc_dat = pd.read_csv(rrc + ".csv")
    rrd_dat = pd.read_csv(rrd + ".csv")
    arrd_dat = pd.read_csv(arrd + ".csv")

    rrab_dat = rrab_dat[["id", "period"]]
    rrab_dat["category"] = "RRab"

    rrc_dat = rrc_dat[["id", "period"]]
    rrc_dat["category"] = "RRc"

    rrd_dat = rrd_dat[["id", "fo_period"]]
    rrd_dat.columns = ["id", "period"]
    rrd_dat["category"] = "RRd"

    arrd_dat = arrd_dat[["id", "fo_period"]]
    arrd_dat.columns = ["id", "period"]
    arrd_dat["category"] = "aRRd"

    all_dat = pd.concat([rrab_dat, rrc_dat, rrd_dat, arrd_dat])
    all_dat.to_csv("all.csv", index=False)

if __name__ == "__main__":
    main()
