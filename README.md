# Orbit Visualizer

## Getting Started

The conda environment can be recreated with the following command:

```bash
conda env create -f environment.yml
```

To update conda libraries installed into the `environment.yml` file, use the following command.

```bash
conda env export --from-history > environment.yml
```

## Theory

Orbital mechanics, or astrodynamics, is concerned with the motion of rockets and spacecraft.

The motions are computed from **Newton's laws of universal gravitation** and **Newton's law of motion**, which explains **Kepler's laws of planetary motion**.

### Orbital Elements

Orbital elements are parameters required to uniquely identify a specific orbit.

The traditional orbital elements are the 6 **Keplerian elements**.

| S/N | Keplerian Elements                      | Purpose                                                                                                                               |
| --- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Eccentricity (`e`)                      | Describe shape of orbit, how flattened wrt circle.                                                                                    |
| 2   | Semi-major axis (`a`)                   | Describe the size of the orbit.                                                                                                       |
|     | Apogee                                  | The point on the satellite orbit that is farthest distance from center of Earth.                                                      |
|     | Perigee                                 | The point on orbit nearest to the center of Earth.                                                                                    |
| 3   | Inclination (`i`)                       | The angle that orbital plane of satellite makes with the Earth's equatorial plane.                                                    |
| 4   | Right ascension of ascending node (`Ω`) | The angle measured from vernal equinox (Y) towards line joining the ascending and descending nodes in direction of rotation of Earth. |
|     | Descending node (N1)                    | The point where satellite passes from the northern to southern hemisphere.                                                            |
|     | Ascending Node (N2)                     | The point where satellite passes from the southern  to  northern hemisphere.                                                          |
|     | Equinoxes                               | The inclination of the equatorial plane of Earth with respect to the line joining the center of the Earth and the sun.                |
|     | Vernal equinox (Y)                      | The direction of line of equinoxes with respect to the direction of the sun on 21 March.                                              |
| 5   | Argument of the perigee (`ω`)           | Defines the location of the major axis of the satellite orbit.                                                                        |
| 6   | True Anomaly                            | Indicate the position of the satellite in its orbit.                                                                                  |

TODO: To understand each parameter and the purpose

Argument of the perigee
The angle between the line joining the perigee and the center of the Earth and the line of nodes, from the ascending node to the descending node in the same direction as the satellite orbit.

True Anomaly (θ or ν)
The angle formed by the line joining the perigee and the center of the Earth with the line joining the satellite and the center of the Earth, in the same direction of the satellite rotation.

### Two Line Elements (TLE)

TLE is acdata format used to convey sets of orbital elements that describe the orbits of Earth-orbiting satellites.

![TLE](https://th.bing.com/th/id/R.5edfe99a12df6e20a941cb7f177ad940?rik=9j6Xjc8aLf74dA&riu=http%3a%2f%2fwww.lesa.biz%2f_%2frsrc%2f1587441572390%2fspace-technology%2fsatellite%2forbital-elements%2fTLE.JPG&ehk=rERUVNWd%2buxNePdRagkLDcqtFJSGI5bWuTpPlgiEy6M%3d&risl=&pid=ImgRaw&r=0)

We can make use of the 6 Keplerian elements to recreate the orbit of a Satellite.
