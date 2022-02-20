# breakit

This project is trying to implement a WebAPI tester, working with Request mutation to try and reach specified Responses and go through predefined Processes

To make it work, define your own process flow within the flows directory and implement the different paths by defining nodes and their expected responses.

Process steps will be executed depth first, meaning that you can defined different flows
based on the previous response parser. 