from unittest import TestCase
from wavefront_pyformance.wavefront_reporter import WavefrontDirectReporter
import unittest
from pyformance import MetricsRegistry
from wavefront_dispatch import wrapper

@wrapper
def handler(ctx, payload):
    return True

class TestWrapper(TestCase):
    def test_wavefront_wrapper(self):
        #reg = MetricsRegistry()
        function_wrapper = wrapper(handler)
        assert(function_wrapper.__name__ == "wavefront_wrapper")

if __name__ == '__main__':
    # run 'python -m unittest discover' from toplevel to run tests
    unittest.main()
