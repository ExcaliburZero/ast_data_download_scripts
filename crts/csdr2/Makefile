get_data: get_catalog get_light_curves

get_catalog: download_catalog process_catalog

download_catalog:
	wget http://nesssi.cacr.caltech.edu/DataRelease/CatalinaVars.tbl

process_catalog:
	python3 process_tbl_file.py

get_light_curves: download_light_curves extract_light_curves process_light_curves

download_light_curves:
	wget http://nesssi.cacr.caltech.edu/DataRelease/AllVar.phot.gz

extract_light_curves:
	gunzip AllVar.phot.gz

process_light_curves:
	python3 separate_curves.py AllVar.phot
