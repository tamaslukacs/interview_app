from interview_app.main import main
from interview_app.config import constants
import pytest
from fixtures import overwrite_entire_main_flow  # noqa: F401; pylint: disable=unused-variable


def test_main_ui_choice_blank(overwrite_entire_main_flow):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    print(pytest_wrapped_e)


@pytest.mark.parametrize("ui_choice, expected",
                         [("CLI", SystemExit),
                          ("Cli", SystemExit),
                          (constants.UI_CLI, SystemExit)])
def test_main_ui_choice_cli(overwrite_entire_main_flow, ui_choice, expected):
    with pytest.raises(expected) as pytest_wrapped_e:
        main(ui_choice)
    assert pytest_wrapped_e.type == expected
    # print(pytest_wrapped_e)


def test_main_unsupported_ui_choice():
    with pytest.raises(ValueError):
        main("VR")


@pytest.mark.xfail(reason="GUI is not implemented")
def test_main_not_implemented_ui():
    with pytest.raises(SystemExit):
        main(constants.UI_GUI)
