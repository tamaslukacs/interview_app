import os.path
# import portalocker
from interview_app.output_writer import write_to_text_with_newlines
import unittest
import os
import pytest
from tutils import get_file_contents_as_list


class TestOutputWriter(unittest.TestCase):

    def setUp(self):
        # store temporarily created result file in this variable
        self.filepath_created = None

    def tearDown(self):
        # cleanup result file after test has run
        if self.filepath_created is not None:
            try:
                os.remove(self.filepath_created)
            except Exception as e:
                print(e)

    def test_write_output_valid(self):
        answer_list = ["a", "b", "c"]
        resultfile = "res.txt"

        self.filepath_created = resultfile
        write_to_text_with_newlines(answer_list, resultfile)

        assert os.path.isfile(resultfile)
        assert get_file_contents_as_list(resultfile) == answer_list

    def test_write_output_invalid_file(self):
        answer_list = ["a", "b", "c"]
        resultfile = r"/*- \res.txt"
        self.filepath_created = resultfile
        with pytest.raises(RuntimeError) as _:
            # with portalocker.Lock(filename=resultfile, mode="w", flags=portalocker.LOCK_EX) as fh:
            # portalocker fails on ubuntu for some reason
            write_to_text_with_newlines(answer_list, resultfile)
