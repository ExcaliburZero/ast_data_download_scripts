get_data: get_data_files get_light_curves

get_data_files: download_data_files process_data_files

download_data_files:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/README
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/RRab.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/RRc.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/RRd.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/aRRd.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/ident.dat

process_data_files:
	python3 process_dat_files.py

get_light_curves: download_light_curves extract_light_curves process_light_curves

download_light_curves:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/rrlyr/phot.tar.gz

extract_light_curves:
	mkdir curves
	tar -zxvf "phot.tar.gz"
	mv phot/* curves/
	rm -d phot/

process_light_curves:
	python3 process_light_curves.py
