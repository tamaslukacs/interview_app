from interview_app import cli, input_parser, find_shortest_path_logic, output_writer, config
import pytest
from click.testing import CliRunner
import sys

# integ
@pytest.fixture
def mock_user_input(monkeypatch):
    def passthrough_process_user_inputs(dictionaryfile=1, startword=2, endword=3, resultfile=4):
        raise ImportError
        return sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8]

    monkeypatch.setattr(cli, 'process_user_inputs', passthrough_process_user_inputs)

# unit main
@pytest.fixture
def overwrite_entire_main_flow(monkeypatch):
    def fake_process_user_inputs():
        return None, None, None, None

    def fake_input_handler(inp, start, end, outp):
        return None

    def fake_find_shortest_path(dictset, startword, endword):
        return ["1"]

    def fake_write_to_text_with_newlines(answer_list, resultfile):
        pass

    monkeypatch.setattr(cli, 'process_user_inputs', fake_process_user_inputs)
    monkeypatch.setattr(input_parser, 'input_handler', fake_input_handler)
    monkeypatch.setattr(find_shortest_path_logic, 'find_shortest_path', fake_find_shortest_path)
    monkeypatch.setattr(output_writer, 'write_to_text_with_newlines', fake_write_to_text_with_newlines)


# unit cli
@pytest.fixture
def overwrite_file_parser_flow(monkeypatch):
    def fake_input_handler(dictionaryfile, startword, endword, resultfile):
        return dictionaryfile, startword, endword, resultfile

    monkeypatch.setattr(input_parser, 'input_handler', fake_input_handler)


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


# unit input_parser
@pytest.fixture
def overwrite_default_parser_behaviour(monkeypatch):
    monkeypatch.setattr(config.behaviour, 'default_file_parser', "xxx")
