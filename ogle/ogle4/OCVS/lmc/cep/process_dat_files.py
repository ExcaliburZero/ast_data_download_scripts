import pandas as pd
import subprocess

def main():
    dat_files = ["cep1O", "cep1O2O", "cep1O2O3O", "cep1O3O", "cep2O", "cep2O3O", "cepF", "cepF1O", "cepF1O2O"]

    cepF_cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "period", "period_uncertainty", "time_max_bright", "I_amplitude", "R21", "phi21", "R31", "phi31"]

    cepF1O_cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "long_period", "long_period_uncertainty", "long_time_max_bright", "long_I_amplitude", "long_R21", "long_phi21", "long_R31", "long_phi31", "short_period", "short_period_uncertainty", "short_time_max_bright", "short_I_amplitude", "short_R21", "short_phi21", "short_R31", "short_phi31"]

    cepF1O2O_cols = ["id", "mean_I_magnitude", "mean_V_magnitude", "long_period", "long_period_uncertainty", "long_time_max_bright", "long_ I_amplitude", "long_R21", "long_phi21", "long_R31", "long_phi31", "mid_period", "mid_period_uncertainty", "mid_time_max_bright", "mid_I_amplitude", "mid_R21", "mid_phi21", "mid_R31", "mid_phi31", "short_period", "short_period_uncertainty", "short_time_max_bright", "short_I_amplitude", "short_R21", "short_phi21", "short_R31", "short_phi31"]

    column_sets = [
          cepF_cols
        , cepF1O_cols
        , cepF1O2O_cols
        , cepF1O_cols
        , cepF_cols
        , cepF1O_cols
        , cepF_cols
        , cepF1O_cols
        , cepF1O2O_cols
    ]

    fix_cep1O2O("cep1O2O")
    fix_cep1O2O("cepF1O")
 
    [dat_to_csv(dat, columns) for (dat, columns) in zip(dat_files, column_sets)]

    combine_dat_files(dat_files)

def fix_cep1O2O(dat):
    """
    Remove any extra spaces at column 102.
    """
    new_contents = []
    with open(dat + ".dat", "r") as f:
        line_size = None
        for line in f:
            if line_size is None:
                line_size = len(line)
                new_contents.append(line)
            else:
                if len(line) != line_size:
                    fixed_line = line[0:102] + line[103:]
                    new_contents.append(fixed_line)
                else:
                    new_contents.append(line)
    
    with open(dat + ".dat", "w") as f:
        f.write("\n".join(new_contents))

def dat_to_csv(dat, columns):
    data = pd.read_fwf(dat + ".dat", header=None)

    if columns is not None:
        try:
            data.columns = columns
        except ValueError:
            print(data.iloc[0])
            print(data.columns)
            print(columns)
            raise ValueError()
        
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
    cep1O_dat = pd.read_csv(dat_files[0] + ".csv")
    cep1O2O_dat = pd.read_csv(dat_files[1] + ".csv")
    cep1O2O3O_dat = pd.read_csv(dat_files[2] + ".csv")
    cep1O3O_dat = pd.read_csv(dat_files[3] + ".csv")
    cep2O_dat = pd.read_csv(dat_files[4] + ".csv")
    cep2O3O_dat = pd.read_csv(dat_files[5] + ".csv")
    cepF_dat = pd.read_csv(dat_files[6] + ".csv")
    cepF1O_dat = pd.read_csv(dat_files[7] + ".csv")
    cepF1O2O_dat = pd.read_csv(dat_files[8] + ".csv")

    cep1O_dat = cep1O_dat[["id", "period"]]
    cep1O_dat["category"] = "cep1O"

    cep1O2O_dat = cep1O2O_dat[["id", "long_period"]]
    cep1O2O_dat.columns = ["id", "period"]
    cep1O2O_dat["category"] = "cep1O2O"

    cep1O2O3O_dat = cep1O2O3O_dat[["id", "long_period"]]
    cep1O2O3O_dat.columns = ["id", "period"]
    cep1O2O3O_dat["category"] = "cep1O2O3O"

    cep1O3O_dat = cep1O3O_dat[["id", "long_period"]]
    cep1O3O_dat.columns = ["id", "period"]
    cep1O3O_dat["category"] = "cep1O3O"

    cep2O_dat = cep2O_dat[["id", "period"]]
    cep2O_dat["category"] = "cep2O"

    cep2O3O_dat = cep2O3O_dat[["id", "long_period"]]
    cep2O3O_dat.columns = ["id", "period"]
    cep2O3O_dat["category"] = "cep2O3O"

    cepF_dat = cepF_dat[["id", "period"]]
    cepF_dat["category"] = "cepF"

    cepF1O_dat = cepF1O_dat[["id", "long_period"]]
    cepF1O_dat.columns = ["id", "period"]
    cepF1O_dat["category"] = "cepF1O"

    cepF1O2O_dat = cepF1O2O_dat[["id", "long_period"]]
    cepF1O2O_dat.columns = ["id", "period"]
    cepF1O2O_dat["category"] = "cepF1O2O"

    all_dat = pd.concat([cep1O_dat, cep1O2O_dat, cep1O2O3O_dat, cep1O3O_dat, cep2O_dat, cep2O3O_dat, cepF_dat, cepF1O_dat, cepF1O2O_dat])

    all_dat.to_csv("all.csv", index=False)

if __name__ == "__main__":
    main()
