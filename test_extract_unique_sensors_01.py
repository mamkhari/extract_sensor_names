import unittest
import extract_unique_sensors_01


class TestExtractSensors(unittest.TestCase):
    """Test class for function test_read_sensors."""
    def test_read_sensors(self):
        """Test whether file_path is a regular file, a directory and that sensors_data
        is not empty."""
        file_name = 'SensorList.txt'
        url = 'http://monctl.devm.camlab.kat.ac.za/kat/doc/manuals/sensors/SensorList.txt'
        sensors_data = extract_unique_sensors_01.read_sensors(file_name, url)
        file_path = extract_unique_sensors_01.Path(file_name)
        self.assertTrue(file_path.is_file())
        self.assertTrue(file_path.parent.is_dir())
        self.assertIsNotNone(sensors_data)
