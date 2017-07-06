get_data: get_catalog get_light_curves

get_catalog: download_catalog process_catalog

download_catalog:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/README
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/Miras.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/OSARGs.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/SRVs.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/ident.dat

process_catalog:
	python3 process_dat_files.py

get_light_curves: download_light_curves extract_light_curves process_light_curves

download_light_curves:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle3/OIII-CVS/lmc/lpv/phot.tar.gz

extract_light_curves:
	mkdir curves
	tar -zxvf "phot.tar.gz"
	mv phot/* curves/
	rm -d phot/

process_light_curves:
	python3 process_light_curves.py
