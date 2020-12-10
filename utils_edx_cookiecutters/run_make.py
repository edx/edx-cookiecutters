"""
Utility tool to run make targets in current directory
"""

from test_utils.venv import run_in_virtualenv


def run_make(make_target):
    """Used to run any make target in current directory"""

    make_command = 'make {}'.format(make_target)
    run_in_virtualenv(make_command)
