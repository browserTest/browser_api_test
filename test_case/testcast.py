from test_case.basecase import BaseCase
import logging


class TestCase(BaseCase):

    def test_get_http(self):
        result = self.get_request_code('test_get_http')
        self.assertEqual(result[0], result[1])

    def test_get_https(self):
        result = self.get_request_code('test_get_https')
        self.assertEqual(result[0], result[1])

