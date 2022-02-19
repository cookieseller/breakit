# Example of a flow
from src.gate.bad_request_response_gate import BadRequestResponseGate
from src.gate.ok_response_gate import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep

process = Process()
process.add_root_step(GetRequestStep('http://localhost:8080/')).add_expected_response(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/start')).add_expected_response(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/gettoken')).add_expected_response(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/validatetoken')).add_expected_response(BadRequestResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/end')).add_expected_response(BadRequestResponseGate())

process.execute()
