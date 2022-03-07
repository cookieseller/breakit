from unittest import TestCase
from unittest.mock import Mock

from src.process.process import Process
from src.process.step.get_request_step import GetRequestStep


class TestProcess(TestCase):
    def test_execute(self):
        process = Process()

        step1 = Mock()
        step1.execute()
        step1.execute.assert_called()

        step2 = Mock()
        step2.execute()
        step2.execute.assert_called()

        process.add_step(step1())
        process.add_step(step2())
        process.execute()

    def test_execute_nested(self):
        process = Process()

        step1 = Mock()
        step1.get_identifier.return_value = 'step1'
        step2 = Mock()
        step2.get_identifier.return_value = 'step2'
        step3 = Mock()
        step3.get_identifier.return_value = 'step3'

        process.add_step(step1)
        process.add_step(step2)
        process.add_step_after(step3, step1)
        process.execute()

        step1.execute.assert_called_once()
        step2.execute.assert_called_once()
        step3.execute.assert_called_once()

    def test_execute_nested_differing_paths(self):
        process = Process()

        step1 = Mock()
        step1.get_identifier.return_value = 'step1'
        step2 = Mock()
        step2.get_identifier.return_value = 'step2'

        step3 = Mock()
        class_mock = Mock()
        step_validator = Mock()
        class_mock.return_value = step_validator
        step_validator.is_valid.return_value = False
        step3.get_identifier.return_value = 'step3'

        step4 = Mock()

        step5 = Mock()
        step5.get_identifier.return_value = 'step5'

        process.add_step(step1)
        process.add_step(step2)
        process.add_step_after(step3, step2).set_step_validator(class_mock)
        process.add_step(step4)
        process.add_step_after(step5, step2)
        process.execute()

        step1.execute.assert_called_once()
        step2.execute.assert_called_once()
        step3.execute.assert_called_once()
        step4.execute.assert_not_called()
        step5.execute.assert_called_once()

    def test_add_default_response_parser(self):
        first_default_response_parser = Mock()
        second_default_response_parser = Mock()
        process = Process()
        process.add_default_response_parser(first_default_response_parser)
        process.add_default_response_parser(second_default_response_parser)

        process_step = process.add_step(GetRequestStep('localhost'))
        response_parsers = process_step.get_response_parsers()
        self.assertEqual(2, len(response_parsers))
        self.assertEqual(response_parsers[0], first_default_response_parser)
        self.assertEqual(response_parsers[1], second_default_response_parser)