import unittest

from qiskit_my_provider.my_provider import MyProvider


class TestProvider(unittest.TestCase):

    def test_provider_getbackend(self):
        """Test provider.get_backend works.
        """
        provider = MyProvider(token='42')

        for backend in provider.backends():
            self.assertEqual(backend, provider.get_backend(backend.name))


