import pytest
import os

from interview_app.cli import process_user_inputs
from interview_app import input_parser
from tutils import get_example_input_filepath
from fixtures import overwrite_file_parser_flow, runner

@pytest.mark.parametrize("args, expected",
                         [(["--DictionaryFile", get_example_input_filepath(), "--StartWord", "AAAA", "--EndWord", "BBBB", "--ResultFile", "res.txt"],
                           [get_example_input_filepath(),"AAAA","BBBB", "res.txt"]),
                          (["-in", get_example_input_filepath(), "-start", 1111, "-end", "GGGG", "-out", "out.cfg"],
                           [get_example_input_filepath(), 1111, "GGGG", "out.cfg"])])
def test_process_user_inputs_valid_inputs(overwrite_file_parser_flow, runner, args, expected):
    result = runner.invoke(process_user_inputs, args)
    print(result.output)
    res = result.output.split("\n")[1:]
    assert result.exit_code == 0
    assert res[0].split(" ")[1] == str(expected[0])
    assert res[1].split(" ")[1] == str(expected[1])
    assert res[2].split(" ")[1] == str(expected[2])
    assert res[3].split(" ")[1] == str(expected[3])

@pytest.mark.parametrize("args",
[(["-in", get_example_input_filepath(), "-start", "CCCC", "-end", "CCCC", "-out", "out.cfg"]),
 (["-in", get_example_input_filepath(), "-start", "dddd", "-end", "dddd", "-out", "out.cfg"])])
def test_process_user_inputs_same_start_and_end_word(overwrite_file_parser_flow,runner,args):
    result = runner.invoke(process_user_inputs, args)
    assert result.exit_code == 1
    assert ValueError == type(result.exception)

@pytest.mark.parametrize("args",
[(["-in", get_example_input_filepath(), "-start", "CCC", "-end", "SSS", "-out", "out.cfg"]),
 (["-in", get_example_input_filepath(), "-start", "ddddd", "-end", "fffff", "-out", "out.cfg"]),
 (["-in", get_example_input_filepath(), "-start", "", "-end", "ffff", "-out", "out.cfg"])])
def test_process_user_inputs_invalid_length_params(overwrite_file_parser_flow,runner, args):
    result = runner.invoke(process_user_inputs,args)
    assert result.exit_code == 1
    assert "Aborted!" in result.output
    assert SystemExit == type(result.exception)
    assert not os.path.isfile(args[7])


@pytest.mark.parametrize("args",
[(["-in", "not_real_file.txt", "-start", 1111, "-end", "SSSS", "-out", "out.cfg"]),
 (["-in", get_example_input_filepath(), "-start", "dddd", "-end", "ffff", "-out", r"out ./\&=-cfg"]),
 #(["-in", get_example_input_filepath(), "-start", "", "-end", "ffff", "-out", "out.cfg"])
])
def test_process_user_inputs_invalid_files(overwrite_file_parser_flow,runner, args):
    result = runner.invoke(process_user_inputs,args)
    print(result.output)
    assert result.exit_code == 2
    assert "Error: " in result.output
    assert SystemExit == type(result.exception)