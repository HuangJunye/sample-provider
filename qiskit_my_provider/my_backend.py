from qiskit.providers import BackendV2 as Backend
from qiskit.providers import Options
from qiskit.transpiler import Target
from qiskit.circuit import Parameter, Measure
from qiskit.circuit.library import PhaseGate, SXGate, UGate, CXGate, IGate

from .my_job import MyJob

class MyBackend(Backend):

    def __init__(self):
        super().__init__()

        # Create Target
        self._target = Target('Target for My Backend')

        # Define support instructions

        # Set option validators
        self.options.set_validator('shots', (1, 4096))
        self.options.set_validator('memory', bool)

    @property
    def target(self):
        return self._target
    
    @property
    def max_circuits(self):
        return 1024
    
    @classmethod
    def _default_options(cls):
        Options(shots=1024, memory=False)

    def run(self, circuits, **kwargs):

        options = {
            'shots': kwargs.get('shots', self.options.shot),
            'memory': kwargs.get('memory', self.options.memory),
        }
        job_json = convert_to_wire_format(circuit, options)
        job_handle = submit_to_backend(job_json)

        return MyJob(self, job_handle, job_json, circuits)