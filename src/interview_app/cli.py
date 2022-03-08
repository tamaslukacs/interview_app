#!/usr/bin/python
import os

import click

from interview_app import config

CONTEXT_SETTINGS = {"help_option_names": ['-h', '--help'],
                    "ignore_unknown_options": True}


def abort_if_length_mismatch(ctx, param, value):
    """
    Used to do basic length check on start and end words
    :param ctx:
    :param param:
    :param value:
    :return:
    """
    if len(value) != config.behaviour.word_length_check:
        print(f"Expected character length for {param.name} is {config.behaviour.word_length_check},"
              f" but the provided word's length is {len(value)}!")
        ctx.abort()
    else:
        return value


@click.version_option(version=config.constants.APP_VER)
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-in", '--DictionaryFile',
              type=click.File(mode='r', encoding="utf-8", errors='strict', lazy=True, atomic=False), required=True,
              help="Filepath and name to dictionary file containing words")  # click.Path(exists=True))
@click.option("-start", '--StartWord', type=str, required=True, callback=abort_if_length_mismatch,
              help='Start word that is assumed to be found in the DictionaryFile file')
@click.option("-end", '--EndWord', type=str, required=True, callback=abort_if_length_mismatch,
              help='Word that is assumed to be found in the DictionaryFile file')
@click.option("-out", '--ResultFile',
              type=click.File(mode='w', encoding="utf-8", errors='strict', lazy=False, atomic=False),
              required=True, help='Filepath and name to the file that will contain the result')
def process_user_inputs(dictionaryfile, startword, endword, resultfile):
    """
    CLI UI for Interview APP

    - Enforces readable file path is provided for DictionaryFile\n
    - Ensures that both StartWord and EndWord are provided\n
    - Makes sure that the ResultFile is writable\n
    - Provides help and documentation for CLI usage\n
    - Ignores unknown parameters passed\n
    """
    # close result file as it was created for the sake of checking, writin will be sombody else's responsibility
    resultfile.close()

    if startword.upper() == endword.upper():
        # remove res file
        os.remove(resultfile.name)
        raise ValueError("It does not make sense to use this tool if the start and the end words are the same!")

    # notifying user
    print(f"The following user inputs were registered:\n"
          f"DictionaryFile: {dictionaryfile.name}\n"
          f"StartWord: {startword}\n"
          f"EndWord: {endword}\n"
          f"ResultFile: {resultfile.name}\n")

    # pass back pathfile not LazyFile
    return dictionaryfile.name, startword, endword, resultfile.name
