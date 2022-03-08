import string


class constants:
    APP_VER = "0.1.0"
    UI_CLI = "CLI"
    UI_GUI = "GUI"  # possible future feature
    FILE_PARSER_TXT_WITH_NEWLINES = "FILE_PARSER_TXT_WITH_NEWLINES"
    FILE_PARSER_CSV_WITH_COMMAS = "FILE_PARSER_CSV_WITH_COMMAS"  # possible future feature


class behaviour:
    word_length_check = 4  # can expand on this in the future
    encoding = "utf-8"  # encoding expected during file readings and writings

    # get all avaiable printablecharacters, convert them to lower case, then remove duplica
    available_charset = set(list(string.printable.lower()))  # charset used during searching

    default_user_interface = constants.UI_CLI  # default user interface choice
    default_file_parser = constants.FILE_PARSER_TXT_WITH_NEWLINES  # default file parser choice if suffix does not give it away
    file_parser_with_newlines_filetypes = ["txt",
                                           "cfg"]  # file parser maping for file extensions where newline separates files
    file_parser_with_commas = ["csv"]  # file parser maping for file extensions where commas separates files
