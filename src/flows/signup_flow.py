# Example of a flow
from src.process.response_parsers.response_code_extractor import ResponseCodeExtractor
from src.process.step_validator.bad_request import BadRequestResponseGate
from src.process.step_validator.ok_response import OkResponseGate
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.process.response_parsers.json_variable_extractor import VariableExtractor
from src.process.variable_storage.persisted_environment import PersistedEnvironment
from src.request.header.common_user_agent_mutator import CommonUserAgentMutator
from src.request.header.multi_header_mutator import MultiHeaderMutator

process = Process()

with PersistedEnvironment('env') as env:
    process.add_default_response_parser(ResponseCodeExtractor(env))
    # Add request body mutator
    process.add_step(GetRequestStep('http://localhost:8080/', CommonUserAgentMutator()))\
        .set_step_validator(OkResponseGate(env))
    process.add_step(GetRequestStep('http://localhost:8080/start', CommonUserAgentMutator()))\
        .set_step_validator(OkResponseGate(env))
    process.add_step(GetRequestStep('http://localhost:8080/gettoken', CommonUserAgentMutator()))\
        .add_response_parser(VariableExtractor(env))\
        .set_step_validator(OkResponseGate(env))
    process.add_step(GetRequestStep('http://localhost:8080/validatetoken', MultiHeaderMutator([CommonUserAgentMutator()])))\
        .set_step_validator(BadRequestResponseGate(env))
    process.add_step(GetRequestStep('http://localhost:8080/end', CommonUserAgentMutator()))\
        .set_step_validator(BadRequestResponseGate(env))

    process.execute()
