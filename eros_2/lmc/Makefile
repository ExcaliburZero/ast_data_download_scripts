get_data: get_catalog get_light_curves

get_catalog: download_cat cat_to_csv

download_cat:
	wget http://stardb.yonsei.ac.kr/EPOCH/download_files/VariablesInEROS_for_StarDB.cat

# Converts the .cat data file into a .csv format for easier parsing.
#
# 1) Remove spaces
# 2) Remove header and footer lines
# 3) Replace vertical slashe separators with commas
# 4) Remove statring character for each line
# 5) Remove ending character for each line
cat_to_csv:
	cat VariablesInEROS_for_StarDB.cat | sed 's/ //g' | sed -e '1d;3d;150119d;' | sed 's/|/,/g' | cut -c 2- | sed 's/.$$//g' > VariablesInEROS_for_StarDB.csv

get_curve = wget "http://stardb.yonsei.ac.kr/EPOCH/LCs/$(1).tar.gz"

get_light_curves: download_light_curves extract_light_curves process_light_curves

download_light_curves:
	$(call get_curve,1_10)
	$(call get_curve,11_20)
	$(call get_curve,21_30)
	$(call get_curve,31_40)
	$(call get_curve,41_50)
	$(call get_curve,51_60)
	$(call get_curve,61_70)
	$(call get_curve,71_80)
	$(call get_curve,81_88)

extract = tar -zxvf "$(1).tar.gz" && mv "$(2)"/* curves/ && rm -d "$(2)"

extract_light_curves:
	mkdir curves
	$(call extract,1_10,1_11)
	$(call extract,11_20,11_21)
	$(call extract,21_30,21_31)
	$(call extract,31_40,31_41)
	$(call extract,41_50,41_51)
	$(call extract,51_60,51_61)
	$(call extract,61_70,61_71)
	$(call extract,71_80,71_81)
	$(call extract,81_88,81_89)

process_light_curves:
	python3 process_light_curves.py
