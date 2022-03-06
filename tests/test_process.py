from unittest import TestCase

from src.process.process import Process
from src.process.step.step import Step


class TestProcess(TestCase):
    def test_execute(self):
        process = Process()
        process.add_step(self.TestStep())
        process.execute()

    class TestStep(Step):
        def execute(self):
            pass

        def get_identifier(self) -> str:
            pass

