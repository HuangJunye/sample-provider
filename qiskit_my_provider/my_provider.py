from qiskit.providers import ProviderV1 as Provider
from qiskit.providers.providerutils import filter_backends

from .my_backend import MyBackend

class MyProvider(Provider):

    def __init__(self, token=None):
        super().__init__()
        self.token = token
        self._backends = [MyBackend(provider=self)]

    def backends(self, name=None, filters=None, **kwargs):
        if name:
            backends = [
                backend for backend in backends if backend.name() == name]
        else:
            backends = self._backends
        return filter_backends(backends, filters=filters, **kwargs)
