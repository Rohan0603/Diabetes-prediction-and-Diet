import sys
from unittest.mock import MagicMock, patch

# Mock pandas and other dependencies that might be missing and are imported at module level
mock_pd = MagicMock()
sys.modules["pandas"] = mock_pd
sys.modules["streamlit"] = MagicMock()
sys.modules["PIL"] = MagicMock()
sys.modules["altair"] = MagicMock()

import unittest
# Now import the function to test
from Login_and_Registration import write_data

class TestLoginAndRegistration(unittest.TestCase):
    def test_write_data(self):
        # Create a sample DataFrame-like mock
        data = MagicMock()

        # Call the function under test
        write_data(data)

        # Verify that to_csv was called with the correct arguments on the data object
        data.to_csv.assert_called_once_with("data/user_data.csv", index=False)

if __name__ == "__main__":
    unittest.main()
