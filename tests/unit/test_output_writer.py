import os.path
import portalocker
from interview_app.output_writer import write_to_text_with_newlines
import unittest
from interview_app import config
import os
import pytest
from tutils import get_file_contents_as_list

class TestOutputWriter(unittest.TestCase):

    def setUp(self):
        #store temporarily created result file in this variable
        self.filepath_created = None

    def tearDown(self):
        #cleanup result file after test has run
        if self.filepath_created is not None:
            try:
                os.remove(self.filepath_created)
            except Exception as e:
                print(e)

    def test_write_output_valid(self):
        answer_list = ["a", "b", "c"]
        resultfile = "res.txt"

        self.filepath_created = resultfile
        write_to_text_with_newlines(answer_list,resultfile )

        assert os.path.isfile(resultfile)
        assert get_file_contents_as_list(resultfile) == answer_list

    def test_write_output_invalid_file(self):
        answer_list = ["a", "b", "c"]
        resultfile = "res.txt"
        self.filepath_created = resultfile
        with pytest.raises(RuntimeError) as pytest_wrapped_e:
            with portalocker.Lock(resultfile, 'w', timeout=10) as fh:
                write_to_text_with_newlines(answer_list,resultfile)


