from urllib.request import urlopen

sensors_data = urlopen('http://monctl.mkat-rts.karoo.kat.ac.za/kat/doc/manuals/sensors/SensorList.txt')
lines = sensors_data.readlines()

candidate_lines = []
for line in lines:
    line = line.decode()
    if line.startswith('kat.sensors'):
        for candidate_line in line.split():
            candidate_lines.append(candidate_line)

# Loop over candidate_lines and extract sensor names
sensor_names = []
for sensor in candidate_lines:
    # Typical output from "sensor" variable:
    # kat.sensors.anc_api_version   kat.sensors.anc_ganglia_api_version   kat.sensors.anc_ganglia_kat_monctl_system_os_name
    sensor = sensor.split('.')[-1]  
    sensor = sensor.strip("\n")  
    sensor_names.append(sensor)
print(sorted(sensor_names))
