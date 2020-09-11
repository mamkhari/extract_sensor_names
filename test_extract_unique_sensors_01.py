import unittest
import logging
from mock import MagicMock
from mock import patch
from extract_unique_sensors_01 import extract_all_sensors
from extract_unique_sensors_01 import splitting_extracted_sensors


class TestExtractSensors(unittest.TestCase):
    """Test class for function test_read_sensors."""

    def test_read_sensors(self):
        with patch('requests.get') as mock_request:
            url = "http://lebogang.com"
            mock_request.return_value.status_code = 200
            self.assertTrue(url)

        with patch('requests.get') as mock_request:
            non_existing_url = "http://google.com/fakeurl"
            mock_request.return_value.status_code = 404
            self.assertTrue(non_existing_url)

        file_name = 1
        mock_path = MagicMock()
        mock_path.Path(file_name).exists().return_value = True
        self.assertTrue(file_name)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(file_name, str)
            self.assertIsInstance(url, str)

        def my_logs(self):
            with self.assertLogs('file_name, url', level='DEBUG') as cm:
                logging.debug("Uknown file_name")
                logging.debug("Unknown url")
                self.assertEqual(
                cm.output, ['BEBUG:file_name:Unknownfile_name', 'url:Unknown url'])

    def test_extract_all_sensors(self):
        sensor_name = "kat"
        sensors_data = [
            "kat.sensor.name_1", "not.kat.sensor.name_1", "kat.sensor.name_2",
            "kat.sensor.name_3", "ket.name.sensor_2"
        ]
        expected_candidate_lines = ['kat.sensor.name_1', 'kat.sensor.name_2',
                                    'kat.sensor.name_3']
        candidate_line = extract_all_sensors(sensors_data, sensor_name)
        self.assertListEqual(candidate_line, expected_candidate_lines)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(sensor_name, int)
            self.assertIsInstance(sensors_data, list)

    def test_splitting_extracted_sensors(self):
        sensor_name = "kat"
        candidate_sensors = [
            'kat.sensor.name_1', 'kat.sensor.name_2', 'kat.sensor.name_3'
        ]
        expected_candidate_sensors = ['name_1', 'name_2', 'name_3']
        sensor = splitting_extracted_sensors(candidate_sensors, sensor_name)
        self.assertListEqual(sensor, expected_candidate_sensors)
