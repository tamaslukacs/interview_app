#!/usr/bin/python
from pathlib import Path
from interview_app import config


def input_handler(dictionaryfile, startword, endword, resultfile):
    """
    By the time code executies until this point it is verified that
    -dictionaryfile can be read (not yet open, lazy=True)
    -startword and endword are provided
    -resultfile is writeable (already opened)

    Ensure the contents of the dictionaryfile is non zero
    load file contents into memory in appropriate data structure
    Normalise data (all lower case and remove duplicates)
    Remove non compliant words
    Ensure that both start and end words are present in dictionary file

    :param dictionaryfile: <unopened file 'r'> LazyFile
    :param startword: str
    :param endword: str
    :param resultfile: <opened file 'w'> LazyFile
    :return:
    """
    # choosing correct logic to parse file based on file suffix - an example to future upgrade the app with
    dictionaryfile_filetype = Path(dictionaryfile).suffix.replace(".", "")
    if dictionaryfile_filetype in config.behaviour.file_parser_with_newlines_filetypes:
        parser_choice = config.constants.FILE_PARSER_TXT_WITH_NEWLINES
        print("Parser will assume that the words are separated by newlines")

    # assume csv file is csv formatted!
    elif dictionaryfile_filetype in config.behaviour.file_parser_with_commas:
        parser_choice = config.constants.FILE_PARSER_CSV_WITH_COMMAS
    else:
        parser_choice = config.behaviour.default_file_parser

    # TODO: implement CSV parsing
    if parser_choice == config.constants.FILE_PARSER_CSV_WITH_COMMAS:
        raise NotImplementedError("CSV parsing is not yet implemented!")
    elif parser_choice == config.constants.FILE_PARSER_TXT_WITH_NEWLINES:
        try:
            with open(dictionaryfile, "r", encoding=config.behaviour.encoding) as f:
                contents = f.read().splitlines()
        except Exception as e:
            # catching exception should be generic just to be on the safe side when dealing with IO#
            # anything can happen, i.e. file removed meanwhile (unlikely)
            print(e)
            raise RuntimeError(f"File {dictionaryfile} cannot be open for reading?")
    else:
        raise ValueError(f"Undefined parser behaviour for {parser_choice}!")

    # store result in a normalised way all lower cased in a set data structure which removes duplicates by default
    # remove not compliant words too
    dictset = set()
    for word in contents:
        if len(word) != config.behaviour.word_length_check:
            continue
        dictset.add(word.lower())

    # no need to check for empty set as we check for start and end word existance anyway
    if startword.lower() not in dictset:
        raise ValueError(f"Start word '{startword}' provided by user does not exist in the dictionary file!")
    if endword.lower() not in dictset:
        raise ValueError(f"End word '{endword}' provided by user does not exist in the dictionary file!")

    # notify user
    print(f"Number of words valid for check: {len(dictset)}")

    return dictset
