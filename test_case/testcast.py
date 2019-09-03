from test_case.basecase import BaseCase
import logging


class TestCase(BaseCase):

    # def test_get_http(self):
    #     result = self.get_request_code('test_get_http')
    #     self.assertEqual(result[0], result[1])
    #
    # def test_get_https(self):
    #     result = self.get_request_code('test_get_https')
    #     self.assertEqual(result[0], result[1])

    """test003——LYX"""
    def test_get_test003(self):
        result = self.get_request_code('test003')
        self.assertEqual(result[0],result[1])

    """test011——LYX"""
    def test_get_test011a(self):
        result = self.get_request_code('test011a')
        self.assertEqual(result[0],result[1])

    """test011b——LYX"""
    def test_get_test011b(self):
        result = self.get_request_value('test011b')
        self.assertEqual(result[0],result[1])

    """test011c——LYX"""
    def test_get_test011c(self):
        result = self.get_request_DB('test011c')
        self.assertEqual(result[0],result[1])
