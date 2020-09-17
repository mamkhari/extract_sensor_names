import logging
import unittest
from pathlib import Path
from urllib.request import urlopen

from mock import MagicMock, Mock, mock_open, patch

from extract_unique_sensors_01 import (extract_all_sensors, read_sensors,
                                       splitting_extracted_sensors)


class TestExtractSensors(unittest.TestCase):
    """Test class for function test_read_sensors."""

    def test_read_sensors_from_file_success(self):
        file_name = "some_non_existant_file.txt"
        url = ""
        read_data = "sensorA, sensorB"
        with patch.object(Path, "exists") as path_exists:
            path_exists.return_value = True
            with patch(
                "builtins.open", mock_open(read_data=read_data), create=True
            ) as mock_file:
                with patch.object(logging, "debug") as mocked_logger:
                    DUT = read_sensors(file_name, url)

        path_exists.assert_called()
        mock_file.assert_called()
        mocked_logger.assert_called_with(
            "Accessing sensor data from the file_name: %r.", file_name
        )
        self.assertEqual([read_data], DUT)

    def test_read_sensors_from_url(self):
        pass

    def _test_read_sensors(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            url = "http://lebogang.com"
            mock_urlopen.return_value.status_code = 200
            self.assertTrue(url)

        with patch("urllib.request.urlopen") as mock_urlopen:
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

        with self.assertLogs("test_logger", level="DEBUG") as cm:
            logging.getLogger("test_logger.file_name").debug("file_name exist")
            logging.getLogger("test_logger.url").debug("URL exist")
            logging.getLogger("test_logger").error("file_name or url type does exist")
            self.assertEqual(
                cm.output,
                [
                    "DEBUG:test_logger.file_name:file_name exist",
                    "DEBUG:test_logger.url:URL exist",
                    "ERROR:test_logger:file_name or url type does exist",
                ],
            )

    def test_extract_all_sensors(self):
        sensor_name = "kat"
        sensors_data = [
            "kat.sensor.name_1",
            "not.kat.sensor.name_1",
            "kat.sensor.name_2",
            "kat.sensor.name_3",
            "ket.name.sensor_2",
        ]
        expected_candidate_lines = [
            "kat.sensor.name_1",
            "kat.sensor.name_2",
            "kat.sensor.name_3",
        ]
        candidate_line = extract_all_sensors(sensors_data, sensor_name)
        self.assertListEqual(candidate_line, expected_candidate_lines)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(sensor_name, int)
            self.assertIsInstance(sensors_data, list)

    def test_splitting_extracted_sensors(self):
        sensor_name = "kat"
        candidate_sensors = [
            "kat.sensor.name_1",
            "kat.sensor.name_2",
            "kat.sensor.name_3",
        ]
        expected_candidate_sensors = ["name_1", "name_2", "name_3"]
        sensor = splitting_extracted_sensors(candidate_sensors, sensor_name)
        self.assertListEqual(sensor, expected_candidate_sensors)
