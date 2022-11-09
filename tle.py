import typing
from datetime import datetime

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

    @classmethod
    def parse(cls, name: str, tle1: str, tle2: str):

        # Parse tle1

        # Parse tle2

        pass


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
