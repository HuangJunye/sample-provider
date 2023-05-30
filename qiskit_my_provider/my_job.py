from qiskit.providers import JobV1 as Job
from qiskit.providers import JobStatus
from qiskit.result import Result


class MyJob(Job):

    def __init__(self, backend, job_id, job_json, circuits):
        super().__init__(backend, job_id)
        self._backend = backend
        self._job_id = job_id
        self.job_json = job_json
        self.circuits = circuits

    def result(self, timeout=None, wait=5):
        result = self._wait_for_result(timeout, wait)
        results = [{
            'success': True,
            'shots': len(result['counts']),
            'data': result['counts']
        }]

        return Result.from_dict({
            'results': results,
            'backend_name': self._backend.name,
            'backend_version': self._backend.backend_version,
            'job_id': self._job_id,
            'success': True,
        })

    def status(self):
        result = get_job_status(self._job_id)
        if result['status'] == 'running':
            status = JobStatus.RUNNING
        elif result['status'] == 'complete':
            status = JobStatus.DONE
        else:
            status = JobStatus.ERROR
        return status
    
    def submit(self):
        raise NotImplementedError