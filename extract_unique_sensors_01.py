import sys
import argparse
import logging

from urllib.request import urlopen
from pathlib import Path


def create_parser():
    """Creates a parser for command line arguments.

    Returns
    -------
    args: Namespace
        Namespace containing the arguments to the command.
    """

    parser = argparse.ArgumentParser(description='Extract unique sensors')
    parser.add_argument('--file_name', help='File to extract unique sensors from.')
    parser.add_argument(
        '--url',
        help='A reference to SensorList.txt that specifies its location on a computer'
        'network.'
    )
    parser.add_argument('--kat_sensor', required=True, help='Name of unique sensor')
    parser.add_argument('-v', metavar='verbosity', type=int, default=2, help='Logging'
                        'verbosity: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug')

    args = parser.parse_args()
    return args


def read_sensors(file_name, url):
    """This function opens, reads and extracts the contents of the file_name.If the file_name
    does not exist,with try will attempt to read the file_name from the url expecting it
    to be there. If not, catch exception and perform a fallback.

    Params
    ------
    file_name: str
        The actual name of the file.
    url: str
        The location of SensorList.txt on the internet.

    Returns
    -------
    sensors_data: list
        list of sensors.
    """
    assert isinstance(file_name, str), "Expected a string."
    assert isinstance(url, str), "Expected a string."
    sensors_data = []
    if file_name and Path(file_name).exists():
        file_path = Path(file_name)
        logging.debug("Accesing sensor data from the file_name: %r.", file_name)
        with open(file_path) as lines:
            sensors_data = lines.readlines()
    elif url:
        try:
            sensors_url = urlopen(url)
            sensors_data = sensors_url.readlines()
            logging.debug("Accessing sensor data from the url:  %r.", url")

        except Exception:
            logging.exception(
                "Failed to retrieve sensor data. Unknown URL type or filename."
            )

    return sensors_data


def extract_all_sensors(sensors_data, sensor_name):
    """Filters the sensors by extracting the name of sensors only.

    Params
    ------
    sensors_data: list
        list of all sensors.
    sensor_name: str
        name of sensor

    Returns
    -------
    candidate_lines: list
        list of sensor names.
    """
    assert isinstance(sensor_name, str), "Expected a string."
    assert isinstance(sensors_data, list), "Expected a list."
    candidate_lines = []
    for sensor_data in sensors_data:
        if sensor_data.startswith(sensor_name):
            for candidate_line in sensor_data.split():
                candidate_lines.append(candidate_line)
    return candidate_lines


# Loop over candidate_lines and extract sensor names
def splitting_extracted_sensors(candidate_sensors, sensor_name):
    """Splits candidate_sensors by dot, removes the empty lines and append results to the
    sensors_list.

    Params
    ------
    candidate_sensors: list
        list of extracted sensors
    sensor_name: str
        name of sensor

    Returns
    -------
    sensors_list: list
        list of unique sensors
    """
    sensors_list = []
    for sensor in sorted(candidate_sensors):
        # Typical output from "sensor" variable:
        # kat.sensors.anc_api_version   kat.sensors.anc_ganglia_api_version
        # kat.sensors.anc_ganglia_kat_monctl_system_os_name
        sensor_ = sensor.split('.')[-1]
        sensor_ = sensor_.strip("\n")
        sensors_list.append(sensor_)
    return sensors_list


def main(args):
    verbose = {
        0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO,
        4: logging.DEBUG}
    logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    sensors_data = read_sensors(args.file_name, args.url)
    extracted_sensors = extract_all_sensors(sensors_data, args.kat_sensor)
    unique_sensors_names = splitting_extracted_sensors(extracted_sensors, args.kat_sensor)
    return unique_sensors_names


if __name__ == "__main__":
    args = create_parser()
    main(args)
