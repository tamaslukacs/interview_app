from interview_app import config
from collections import deque
from typing import Dict


def find_shortest_path(dictset, startword, endword):
    """
    Algorithm to find shortest distance from two words thouh a set of words existing in dicset.
    Depth first search would be not optimal as we might be unlucky and go deep before we realise there is a shorter path.

    The following steps are taken:
    - start from startword
    - keep track of distance so that shortest path can be an exit flag
    - keep track of words already used from the dictset
    - work out list of words 1 distance away from current word
    - operate on that list to stay on same distance
    - check if endword is in the 1 distance away list, if so, exit alorithm, return visited_words
    - if endword not found, move to one of the 1 distance away word from current word, and repeat,
      but retain memory of visited nodes
    - we get the shortest path naturally as we go 1 depth at a time and exit as soon as we find one solution

    :param dictset:
    :param startword:
    :param endword:
    :return:
    """
    shortest_path = []
    # normalise start and endwords to match w dictset which was already normalised
    startword = startword.lower()
    endword = endword.lower()

    charset = config.behaviour.available_charset

    # container for relationship mapping between new word and where it came from
    child_parent_word_dict: Dict[str, str] = dict()
    # put start word in current depth
    current_depth_wordlist = [startword]
    # storage for next depth
    next_depth_wordlist = []
    # until there is any word in the current_node
    while len(current_depth_wordlist) > 0:
        # for each word in the current_depth_wordlist
        for current_word in current_depth_wordlist:
            # for each character of the word
            for charidx in range(len(current_word)):
                # for each possible characters
                for valid_char in charset:
                    new_word_list = list(current_word)
                    new_word_list[charidx] = valid_char
                    new_word = "".join(new_word_list)
                    # if the new_word is a valid one
                    if new_word in dictset:
                        # if it is not a previously visited word
                        if new_word not in child_parent_word_dict.keys():
                            # create dict entry with new word as key and parent as value
                            child_parent_word_dict.update({new_word: current_word})
                            # also add it to the next depth search
                            next_depth_wordlist.append(new_word)
                        # if the new word was already recorded, do nothing
                        else:
                            pass
                    if new_word == endword:
                        shortest_path = trace_back_path(child_parent_word_dict, startword, endword)
                        # return valid_path
                        break
        # copy word list to current level fron next
        current_depth_wordlist = []
        current_depth_wordlist = next_depth_wordlist[:]
        # clean next level
        next_depth_wordlist = []

    # no vaid path is found
    if len(shortest_path) == 0:
        # notify user
        print("No valid path was found from start to end word using the dictionary of words provided."
              " No result file will be generated.")
    else:
        print(
            f"The shortest distance between the start '{startword}' and end '{endword}' word is {len(shortest_path)} long.")
    return shortest_path


def trace_back_path(child_parent_word_dict, startword, endword):
    """
    Helper function to trtace back valid path though relationship mapping
    :param child_parent_word_dict:
    :param startword:
    :param endword:
    :return:
    """
    current_word = endword
    # use deque for path so that it is quick to append to the beginning of the list, no need to reverse later
    valid_path = deque([current_word.capitalize()])
    while current_word != startword:
        current_word = child_parent_word_dict[current_word]
        valid_path.appendleft(current_word.capitalize())

    return valid_path
