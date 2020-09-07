import unittest
from extract_unique_sensors_01 import extract_all_sensors
from extract_unique_sensors_01 import splitting_extracted_sensors


class TestExtractSensors(unittest.TestCase):
    """Test class for function test_read_sensors."""

    def test_extract_all_sensors(self):
        sensor_name = "kat"
        sensors_data = [
            "kat.sensor.name_1", "not.kat.sensor.name_1", "kat.sensor.name_2",
            "kat.sensor.name_3", "ket.name.sensor_2"
        ]
        expected_candidate_lines = ['kat.sensor.name_1', 'kat.sensor.name_2',
                                    'kat.sensor.name_3']
        self.assertIsInstance(sensor_name, str)
        self.assertIsInstance(sensors_data, list)
        candidate_line = extract_all_sensors(sensors_data, sensor_name)
        self.assertListEqual(candidate_line, expected_candidate_lines)

    def test_splitting_extracted_sensors(self):
        sensor_name = "kat"
        candidate_sensors = [
            'kat.sensor.name_1', 'kat.sensor.name_2', 'kat.sensor.name_3'
        ]
        expected_candidate_sensors = ['name_1', 'name_2', 'name_3']
        sensor = splitting_extracted_sensors(candidate_sensors, sensor_name)
        self.assertListEqual(sensor, expected_candidate_sensors)
