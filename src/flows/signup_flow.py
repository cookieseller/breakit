# Example of a flow
from src.process.response_parsers.response_code_extractor import ResponseCodeExtractor
from src.process.step_validator.bad_request import BadRequestResponseGate
from src.process.step_validator.ok_response import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.process.response_parsers.json_variable_extractor import VariableExtractor
from src.request.header.common_header_mutator import CommonHeaderMutator

process = Process()
process.add_default_response_parser(ResponseCodeExtractor)

process.add_step(GetRequestStep('http://localhost:8080/', CommonHeaderMutator()))\
    .set_step_validator(OkResponseGate)
process.add_step(GetRequestStep('http://localhost:8080/start', CommonHeaderMutator()))\
    .set_step_validator(OkResponseGate)
process.add_step(GetRequestStep('http://localhost:8080/gettoken', CommonHeaderMutator()))\
    .add_response_parser(VariableExtractor)\
    .set_step_validator(OkResponseGate)
process.add_step(GetRequestStep('http://localhost:8080/validatetoken', CommonHeaderMutator()))\
    .set_step_validator(BadRequestResponseGate)
process.add_step(GetRequestStep('http://localhost:8080/end', CommonHeaderMutator()))\
    .set_step_validator(BadRequestResponseGate)

process.execute()
