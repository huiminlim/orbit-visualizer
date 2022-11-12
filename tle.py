from __future__ import annotations

from datetime import datetime
from enum import IntEnum

import requests


class TLE:
    def __init__(
            self,
            name: str,
            sat_num: str,
            classification: dict,
            intl_designator: str,
            timestamp: datetime,
            first_deriv_mean_motion: float,
            second_deriv_mean_motion: float,
            drag_term: float,
            ephermeris_type: int,
            element_num: int,
            inclination: float,
            right_ascesion_ascending_node: float,
            eccentricity: int,
            arg_of_perigee: float,
            mean_anomaly: float,
            mean_motion: float,
            revolution_at_epoch: int,
            checksum: int) -> None:
        self.name = name
        self.sat_num = sat_num
        self.classification = classification
        self.intl_designator = intl_designator
        self.timestamp = timestamp
        self.first_deriv_mean_motion = first_deriv_mean_motion
        self.second_deriv_mean_motion = second_deriv_mean_motion
        self.drag_term = drag_term
        self.ephermeris_type = ephermeris_type
        self.element_num = element_num
        self.checksum = checksum
        self.inclination = inclination
        self.right_ascesion_ascending_node = right_ascesion_ascending_node
        self.eccentricity = eccentricity
        self.arg_of_perigee = arg_of_perigee
        self.mean_anomaly = mean_anomaly
        self.mean_motion = mean_motion
        self.revolution_at_epoch = revolution_at_epoch

    # Index position of the tokens in TLE1
    class TLE1_Index(IntEnum):
        LINE = 0
        SATELLITE_CATALOG_NUM = 1
        INTL_DESIGNATOR = 2
        EPOCH_JULIAN_YEAR_DAY_FRACTION = 3
        FIRST_DERIV_MEAN_MOTION = 4
        SECOND_DERIV_MEAN_MOTION = 5
        DRAG_TERM = 6
        EPHEMERIS_TYPE = 7
        ELEMENT_NUM_CHECKSUM = 8

    # Index position of the tokens in TLE2
    class TLE2_Index(IntEnum):
        LINE = 0
        SATELLITE_CATALOG_NUM = 1
        INCLINATION = 2
        RIGHT_ASCENSION_ASCENDING_NODE = 3
        ECCENTRICITY = 4
        ARGUMENT_OF_PERIGEE = 5
        MEAN_ANOMALY = 6
        MEAN_MOTION = 7
        REVOLUTION_NUM_CHECKSUM = 8

    @classmethod
    def parse(cls, name: str, tle1: str, tle2: str):

        # Tokenize tle1
        tle1_tokens = tle1.split()
        sat_num = tle1_tokens[TLE.TLE1_Index.SATELLITE_CATALOG_NUM]
        intl_designator = tle1_tokens[TLE.TLE1_Index.INTL_DESIGNATOR]
        julian_year_day_fraction = tle1_tokens[TLE.TLE1_Index.EPOCH_JULIAN_YEAR_DAY_FRACTION]
        first_deriv_mean_motion = tle1_tokens[TLE.TLE1_Index.FIRST_DERIV_MEAN_MOTION]
        second_deriv_mean_motion = tle1_tokens[TLE.TLE1_Index.SECOND_DERIV_MEAN_MOTION]
        drag_term = tle1_tokens[TLE.TLE1_Index.DRAG_TERM]
        ephermeris_type = tle1_tokens[TLE.TLE1_Index.EPHEMERIS_TYPE]
        element_num = tle1_tokens[TLE.TLE1_Index.ELEMENT_NUM_CHECKSUM][:-1]
        checksum1 = tle1_tokens[TLE.TLE1_Index.ELEMENT_NUM_CHECKSUM][-1]
        print(
            sat_num,
            intl_designator,
            julian_year_day_fraction,
            first_deriv_mean_motion,
            second_deriv_mean_motion,
            drag_term,
            ephermeris_type,
            element_num,
            checksum1)

        # Parse tle2
        tle2_tokens = tle2.split()
        inclination = tle2_tokens[TLE.TLE2_Index.INCLINATION]
        right_ascension_ascending_node = tle2_tokens[TLE.TLE2_Index.RIGHT_ASCENSION_ASCENDING_NODE]
        eccentricity = tle2_tokens[TLE.TLE2_Index.ECCENTRICITY]
        arg_of_perigee = tle2_tokens[TLE.TLE2_Index.ARGUMENT_OF_PERIGEE]
        mean_anomaly = tle2_tokens[TLE.TLE2_Index.MEAN_ANOMALY]
        mean_motion = tle2_tokens[TLE.TLE2_Index.MEAN_MOTION]
        revo_num = tle2_tokens[TLE.TLE2_Index.REVOLUTION_NUM_CHECKSUM][:-1]
        checksum2 = tle2_tokens[TLE.TLE2_Index.REVOLUTION_NUM_CHECKSUM][-1]
        print(
            inclination,
            right_ascension_ascending_node,
            eccentricity,
            arg_of_perigee,
            mean_anomaly,
            mean_motion,
            revo_num,
            checksum2)

        # return cls(name,sat_num, intl_designator )


if __name__ == "__main__":
    r = requests.get("https://api.endurancein.space/tle")

    # Exit if HTTP request failed
    if r.status_code != 200:
        print("TLE request failed... Exiting...")
        exit(1)

    name = r.json()["name"]
    tle1 = r.json()["tle1"]
    tle2 = r.json()["tle2"]
    print(f"{name}")
    print(f"\t{tle1}")
    print(f"\t{tle2}")

    tle = TLE.parse(name, tle1, tle2)
