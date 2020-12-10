from test_utils.venv import run_in_virtualenv


def run_make(make_target):
    """Make sure the upgrade target works"""

    make_command = 'make {}'.format(make_target)
    run_in_virtualenv(make_command)
