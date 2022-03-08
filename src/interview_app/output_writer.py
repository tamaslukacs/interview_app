from interview_app import config


def write_to_text_with_newlines(answer_list, resultfile):
    try:
        with open(resultfile, "w", encoding=config.behaviour.encoding) as f:
            f.write('\n'.join(answer_list))
    except Exception as e:
        # catch any unexpected exception, file opening and writing was apready checked before, but
        # file could be open by other application meanwhile
        print(e)
        # report the solution to the user in order to reduce frustration for the user by not getting the answer in a file
        print(f"Result for shortest path:\n{answer_list}")
        raise RuntimeError(f"Cannot write to result file '{resultfile}'! Maybe open by other application?")
