# ROOT
ROOT graphs and other functions.

dichroic_dark_box/
------------------
plot_wavelengths.py
- Dichroic filter characterization tests. Contains a hard-coded method for graphing percent reflectance, transmittance, and sum at various incidence angles and LEDs. This is a heat map version.

refl_graph.cpp
- Dichroic filter characterization tests. Contains a hard-coded method for graphing percent reflectance at various incidence angles and LEDs. 

sum_graph.cpp
- Dichroic filter characterization tests. Contains a hard-coded method for graphing the sum of percent transmittance and reflectance at various incidence angles and LEDs. 

trans_graph.cpp
- Dichroic filter characterization tests. Contains a hard-coded method for graphing percent transmittance at various incidence angles and LEDs. 

spectrometer/
-------------
air_per.txt
- Blank layout for hard-coded filter/sans filter data for tranmission percentages.

all_incidence.py
- Hard-coded filenames for all incidence angles to get specific wavelengths and their respective intensities in order to get the percent transmission.

per_trans.py
- Calculator for division, average, and double ratios in order to get transmission, reflection, and sum percentages.

singular_incidence.py
- Simple code with hard-coded filename to plot raw data with text indicating peak wavelength and intensity.
