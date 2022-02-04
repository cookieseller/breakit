# Example of a flow
#data = create_data()
#gate(response(signup(data))
from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep
from src.response.ok_response import OkResponse

process = Process()
process.add_step(GetRequestStep(), OkResponse())


