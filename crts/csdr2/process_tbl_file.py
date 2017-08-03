import pandas as pd
import subprocess

def main():
    tbl_file = "CatalinaVars"
    
    tbl_to_csv(tbl_file)
    fix_var_type(tbl_file)

def tbl_to_csv(tbl_file):
    """
    1) Remove # symbols at the beginning of lines
    2) Remove extra spaces
    3) Replace spaces with commas
    4) Remove commas at beginning of lines
    5) Remove commas at end of lines
    6) Remove \\nodata entries
    """
    command = "cat %s.tbl | sed 's/^#//g' | tr -s ' ' | sed 's/ /,/g' | sed 's/^,//g' | sed 's/,$//g' | sed 's/\\\\\\\\nodata//g' > %s.csv" % (tbl_file, tbl_file)

    subprocess.call(command, shell=True)

VAR_TYPES = {
      1: "EW"
    , 2: "EA"
    , 3: "beta Lyrae"
    , 4: "RRab"
    , 5: "RRc"
    , 6: "RRd"
    , 7: "Blazkho"
    , 8: "RS CVn"
    , 9: "ACEP"
    , 10: "Cep-II"
    , 11: "HADS"
    , 12: "LADS"
    , 13: "LPV"
    , 14: "ELL"
    , 15: "Hump"
    , 16: "PCEB"
    , 17: "EA_UP"
}

def fix_var_type(tbl_file):
    data = pd.read_csv(tbl_file + ".csv")

    data["Var_Type"] = data["Var_Type"].map(lambda x: VAR_TYPES[x])

    data.to_csv(tbl_file + ".csv", index=False)

if __name__ == "__main__":
    main()
