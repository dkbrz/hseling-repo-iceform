import unittest

import hseling_api_iceform


class HSELing_API_IceformTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_iceform.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to hseling_api_Iceform', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
