get_data: download_files get_light_curves

download_files:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/README
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/RRab.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/RRc.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/RRd.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/aRRd.dat
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/ident.dat

get_light_curves: download_light_curves extract_light_curves process_light_curves

download_light_curves:
	wget ftp://ftp.astrouw.edu.pl/ogle/ogle4/OCVS/smc/rrlyr/phot.tar.gz

extract_light_curves:
	mkdir curves
	tar -zxvf "phot.tar.gz"
	mv phot/* curves/
	rm -d phot/

process_light_curves:
	python3 process_light_curves.py
