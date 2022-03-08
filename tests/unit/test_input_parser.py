from click.testing import CliRunner
import pytest
import os

from interview_app.cli import process_user_inputs
from interview_app.input_parser import input_handler
from interview_app import config
from tutils import *
from fixtures import overwrite_default_parser_behaviour
#config.behaviour.default_file_parser

def test_valid_parsing_5match_5mismatch():
    res = input_handler(dictionaryfile=get_valid_5match_5mismatch_filepath(), startword="this", endword="that", resultfile="res.txt")
    assert len(res) == 5

def test_invalid_parsing_no_start_word():
    with pytest.raises(ValueError) as pytest_wrapped_e:
        res = input_handler(dictionaryfile=get_valid_5match_5mismatch_filepath(), startword="xxxx", endword="that", resultfile="res.txt")

def test_invalid_parsing_no_end_word():
    with pytest.raises(ValueError) as pytest_wrapped_e:
        res = input_handler(dictionaryfile=get_valid_5match_5mismatch_filepath(), startword="that", endword="xxxx", resultfile="res.txt")


def test_valid_parsing_5match_5mismatch_no_ext():
    res = input_handler(dictionaryfile=get_valid_5match_5mismatch_no_ext_filepath(), startword="this", endword="that", resultfile="res.txt")
    assert len(res) == 5

def test_unhandled_parser_in_config(overwrite_default_parser_behaviour):
    with pytest.raises(ValueError) as pytest_wrapped_e:
        res = input_handler(dictionaryfile=get_valid_5match_5mismatch_no_ext_filepath(), startword="this",
                            endword="that", resultfile="res.txt")

def test_csv_input():
    with pytest.raises(NotImplementedError) as pytest_wrapped_e:
        res = input_handler(dictionaryfile=get_invalid_csv_filepath(), startword="this", endword="that",
                        resultfile="res.txt")
    #assert NotImplementedError

def test_parsing_dll_file():
    with pytest.raises(RuntimeError) as pytest_wrapped_e:
        res = input_handler(dictionaryfile=get_invalid_random_dll_filepath(), startword="this", endword="that",
                        resultfile="res.txt")


@pytest.mark.xfail(reason="GUI is not implemented")
def test_input_handler_correct_inputs():
    assert 0 == 0