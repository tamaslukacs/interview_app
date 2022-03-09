from interview_app import find_shortest_path_logic


def test_find_shortest_path_no_solution():
    dictset = ("aaaa", "bbbb")
    startword = "aaaa"
    endword = "bbbb"
    res = find_shortest_path_logic.find_shortest_path(dictset, startword, endword)
    assert res == []


def test_find_shortest_path_solution_length_2():
    dictset = ("aaaa", "aaab")
    startword = "aaaa"
    endword = "aaab"
    res = find_shortest_path_logic.find_shortest_path(dictset, startword, endword)
    assert len(res) == 2


def test_find_shortest_path_solution_length_3():
    dictset = ("aaaa", "aaab", "aabb")
    startword = "aaaa"
    endword = "aabb"
    res = find_shortest_path_logic.find_shortest_path(dictset, startword, endword)
    assert len(res) == 3
