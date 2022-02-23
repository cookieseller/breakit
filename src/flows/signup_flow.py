# Example of a flow
from src.process.step_validator.bad_request import BadRequestResponseGate
from src.process.step_validator.ok_response import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.process.response_parsers.variable_extractor import VariableExtractor

process = Process()
process.add_root_step(GetRequestStep('http://localhost:8080/')).add_step_validator(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/start')).add_step_validator(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/gettoken'))\
    .add_response_parser(VariableExtractor())\
    .add_step_validator(OkResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/validatetoken'))\
    .add_step_validator(BadRequestResponseGate())
process.add_next_step(GetRequestStep('http://localhost:8080/end')).add_step_validator(BadRequestResponseGate())

process.execute()
