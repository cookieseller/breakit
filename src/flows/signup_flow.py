# Example of a flow
from src.response_parsers.bad_request import BadRequestResponseGate
from src.response_parsers.ok_response import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.response_parsers.variable_extractor import VariableExtractor

process = Process()
process.add_root_step(GetRequestStep('http://localhost:8080/')).add_response_handler(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/start')).add_response_handler(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/gettoken'))\
    .add_response_handler(OkResponseGate()) \
    .add_response_handler(VariableExtractor())
process.add_next_step(GetRequestStep('http://localhost:8080/validatetoken'))\
    .add_response_handler(BadRequestResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/end')).add_response_handler(BadRequestResponseGate())

process.execute()
