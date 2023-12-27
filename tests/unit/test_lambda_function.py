import unittest
import importlib
import logging
import jsonpickle
import json
from lambdas.lambda_function import sum, lambda_handler


logger = logging.getLogger()

class TestFunction(unittest.TestCase):

  def test_sum(self):
    test_input = [2,4,6,8]
    expected_result = 20
    actual_result = sum(test_input)
    self.assertEqual(expected_result, actual_result)

  def test_lambda_handler(self):
    #xray_recorder.begin_segment('test_function')
    file = open('event.json', 'rb')
    expected_result = 15
    try:
      ba = bytearray(file.read())
      test_event = jsonpickle.decode(ba)
      logger.warning('## EVENT')
      logger.warning(jsonpickle.encode(test_event))
      test_context = {'requestid' : '1234'}
      actual_result = lambda_handler(test_event, test_context)
      print(str(actual_result))
      self.assertEqual(actual_result, expected_result)
    finally:
      file.close()
    file.close()
    #xray_recorder.end_segment()

if __name__ == '__main__':
    unittest.main()