# Example of a flow
from src.gate.bad_request_response_gate import BadRequestResponseGate
from src.gate.ok_response_gate import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep

process = Process()
process.add_root_step(GetRequestStep('http://localhost:8080/')).add_response_handler(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/start')).add_response_handler(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/gettoken')).add_response_handler(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/validatetoken'))\
    .add_response_handler(BadRequestResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/end')).add_response_handler(BadRequestResponseGate())

process.execute()
