from urllib.request import urlopen

sensors_data = urlopen('http://monctl.mkat-rts.karoo.kat.ac.za/kat/doc/manuals/sensors/SensorList.txt')
lines = sensors_data.readlines()

candidate_lines = []
for line in lines:
    line = line.decode()
    if line.startswith('kat.sensors'):
        for sensor in line.split():
            candidate_lines.append(sensor)

# extract sensor names

sensor_names = []
for sensor_name in candidate_lines:
    # typical line : gvygvtvyvtvyvtv
    # kat.sensors.anc_api_version   kat.sensors.anc_ganglia_api_version   kat.sensors.anc_ganglia_kat_monctl_system_os_name
    sensor_name = sensor_name.split('.')[-1].strip("\n")
    sensor_names.append(sensor_name)
print(sorted(sensor_names))










