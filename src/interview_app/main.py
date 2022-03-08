#!/usr/bin/python
from interview_app import config
from interview_app import input_parser
from interview_app import find_shortest_path_logic
from interview_app import output_writer


def main(ui=config.behaviour.default_user_interface):
    """
    Entry point for Interview App

    :param ui: choice of UI to use by user, default is commond-line "CLI"
    :return:
    """
    import sys
    if ui.upper() == config.constants.UI_CLI:
        from interview_app.cli import process_user_inputs
    elif ui.upper() == config.constants.UI_GUI:
        raise NotImplementedError(f"UI Feature {config.constants.UI_GUI} not yet implemented!")
    else:
        raise ValueError(f"Unsupported User Interface option '{ui}'!")

    # process user inputs
    dictionaryfile, startword, endword, resultfile = process_user_inputs()

    # parse, clean and normalise dictionary of words
    dictset = input_parser.input_handler(dictionaryfile, startword, endword, resultfile)

    # find out if there is a a path from start to end word and stop at the shortest one
    answer_list = find_shortest_path_logic.find_shortest_path(dictset, startword, endword)

    # if there was an answer found, write it using output handler
    if len(answer_list) > 0:
        output_writer.write_to_text_with_newlines(answer_list, resultfile)

    sys.exit(0)


if __name__ == '__main__':  # pragma: no cover
    main()
