from skyfield.api import load, wgs84

stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

for sat in satellites:
    raan_rad = sat.model.nodeo
    eccentricity_rad = sat.model.ecco
    aug_of_perigee_rad = sat.model.argpo
