from urllib.request import urlopen
from pathlib import Path

file_name = "SensorList.txt"
url = "http://monctl.devm.camlab.kat.ac.za/kat/doc/manuals/sensors/SensorList.txt"                                                                          
kat_sensor = "kat.sensor"

def read_sensors(file_name, url):
    """This function opens, reads and extracts the contents of the file_name.

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
    try:
        assert isinstance(file_name, str)
        assert isinstance(url, str)       
    except AssertionError:        
        print('filename or url is not a string.')
        return                                   
    sensors_data = []
    if file_name and Path(file_name).exists():
        file_path = Path(file_name)           
        with open(file_path) as lines:
            sensors_data = lines.readlines()
    elif url:                               
        try: 
            sensors_url = urlopen(url)
            sensors_data = sensors_url.readlines()
        except Exception:                         
            print("Failed to retrieve sensor data")
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
    assert isinstance(sensors_data, list), "Expected a list"
    candidate_lines = []
    for sensor_data in sensors_data:
        if sensor_data.startswith(sensor_name):
            for candidate_line in sensor_data.split():
                candidate_lines.append(candidate_line)
    return candidate_lines

# Loop over candidate_lines and extract sensor names
def splitting_list(sensors_list):
    """Splits the candidate_lines by dot and append that to sensors_list. It also removes the 
    empty lines.
    """
    sensors_list = []
    candidate_lines = sensors_list
    sensors_list = extract_all_sensors(sensors_data)
    unique_sensors = splitting_list(sensors_list)
    for sensor in candidate_lines:
    # Typical output from "sensor" variable:
    # kat.sensors.anc_api_version   kat.sensors.anc_ganglia_api_version   kat.sensors.anc_ganglia_kat_monctl_system_os_name
        sensor = sensor.split('.')[-1]  
        sensor = sensor.strip("\n") 
        sensors_list.append(sensor)
    return sensors_list 
