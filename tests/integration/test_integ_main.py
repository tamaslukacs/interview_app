import sys
from interview_app.main import main
from interview_app import cli
import unittest
import pytest
import os
from fixtures import mock_user_input
from tutils import get_example_input_filepath,get_file_contents_as_list
from _pytest.monkeypatch import MonkeyPatch


def passthrough_process_user_inputs(dictionaryfile=1, startword=2, endword=3, resultfile=4):
    return sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8]




class TestOutputWriter(unittest.TestCase):

    def setUp(self):
        #store temporarily created result file in this variable
        self.filepath_created = None
        self.monkeypatch = MonkeyPatch()

    def tearDown(self):
        #cleanup result file after test has run
        if self.filepath_created is not None:
            try:
                os.remove(self.filepath_created)
            except Exception as e:
                print(e)

    def test_integ_exists_solution(self):
        args = ["--DictionaryFile",
                get_example_input_filepath(),
                "--StartWord",
                "Spin",
                "--EndWord",
                "Spot",
                "--ResultFile",
                "res.txt"]
        solultion = ["Spin", "Spit", "Spot"]
        self.filepath_created = args[-1]
        sys.argv[1:] = args
        self.monkeypatch.setattr(cli, 'process_user_inputs', passthrough_process_user_inputs)
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            main()
        assert os.path.isfile(args[-1])
        assert get_file_contents_as_list(args[-1]) == solultion

    def test_integ_no_solution(self):
        args = ["--DictionaryFile",
                get_example_input_filepath(),
                "--StartWord",
                "ANSI",
                "--EndWord",
                "yang",
                "--ResultFile",
                "res.txt"]
        solultion = ["Spin", "Spit", "Spot"]
        self.filepath_created = args[-1]
        sys.argv[1:] = args
        self.monkeypatch.setattr(cli, 'process_user_inputs', passthrough_process_user_inputs)
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            main()
        assert not os.path.isfile(args[-1])
        #assert get_file_contents_as_list(args[-1]) == solultion