from qiskit.providers import ProviderV1 as Provider
from qiskit.providers.providerutils import filter_backends

from .my_backend import MyBackend

class MyProvider(Provider):

    def __init__(self, token=None):
        super().__init__()
        self.token = token
        self.backends = [MyBackend(provider=self)]

    def backends(self. name=None, **kwargs):
        if name:
            backends = [
                backend for backend in backends if backend.name() == name]
        return filter_backends(backends, filters=filters, **kwargs)
