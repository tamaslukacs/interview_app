import os
from interview_app import config


def get_example_input_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", 'words-english.txt')
    return example_input


def get_invalid_empty_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", 'empty.txt')
    return example_input


def get_invalid_random_dll_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", 'random_dll_file')
    return example_input


def get_invalid_csv_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", 'commas.csv')
    return example_input


def get_valid_5match_5mismatch_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", "small_5_valid_5_invalid.txt")
    return example_input


def get_valid_5match_5mismatch_no_ext_filepath():
    resdir = os.getcwd()
    # print(resdir)
    example_input = os.path.join(resdir, "tests", "resources", "small_5_valid_5_invalid_no_ext")
    return example_input


def get_file_contents_as_list(filepath):
    try:
        with open(filepath, "r", encoding=config.behaviour.encoding) as f:
            contents = f.read().splitlines()
    except Exception as e:
        raise e

    return contents
