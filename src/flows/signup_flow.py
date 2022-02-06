# Example of a flow
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.response.ok_response import OkResponse

process = Process()
process.add_root_step(GetRequestStep('http://localhost:8080/'), OkResponse())
process.add_next_step(GetRequestStep('http://localhost:8080/toggle'), OkResponse())

process.execute()
