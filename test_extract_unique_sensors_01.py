import unittest
import logging
from mock import MagicMock
from mock import patch
from urllib.request import urlopen
from extract_unique_sensors_01 import read_sensors
from extract_unique_sensors_01 import extract_all_sensors
from extract_unique_sensors_01 import splitting_extracted_sensors


class TestExtractSensors(unittest.TestCase):
    """Test class for function test_read_sensors."""

    def test_read_sensors(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            url = "http://lebogang.com"
            mock_urlopen.return_value.status_code = 200
            self.assertTrue(url)

        with patch('urllib.request.urlopen') as mock_urlopen:
            non_existing_url = "http://google.com/fakeurl"
            mock_urlopen.return_value.status_code = 404
            self.assertTrue(non_existing_url)

        file_name = 1
        mock_path = MagicMock()
        mock_path.Path(file_name).exists().return_value = True
        self.assertTrue(file_name)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(file_name, str)
            self.assertIsInstance(url, str)

        with self.assertLogs('test_logger', level='DEBUG') as cm:
            logging.getLogger('test_logger.file_name').debug("file_name exist")
            logging.getLogger('test_logger.url').debug("URL exist")
            logging.getLogger('test_logger').error("file_name or url type does exist")
            self.assertEqual(
            cm.output, [
                'DEBUG:test_logger.file_name:file_name exist',
                'DEBUG:test_logger.url:URL exist',
                'ERROR:test_logger:file_name or url type does exist']
            )

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
