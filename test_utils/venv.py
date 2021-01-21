"""
Utilities for managing virtualenvs in tests.
"""

import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def run_in_virtualenv(shell_script):
    """
    Set up virtualenv in current directory and run provided shell script
    with virtualenv active. Virtualenv is deleted after script runs.
    """
    with TemporaryDirectory() as parent_dir:
        venv_path = str(Path(parent_dir) / 'venv')
        try:
            subprocess.check_call(['virtualenv', '-p', sys.executable, '--clear', venv_path])
            # TODO: Remove the following line when both the latest versions of pip and pip-tools work fine together
            subprocess.check_call(f'. {venv_path}/bin/activate; pip install pip==20.0.2', env={}, shell=True)
            subprocess.check_call(f'. {venv_path}/bin/activate; {shell_script}', env={}, shell=True)
        finally:
            if shutil.rmtree.avoids_symlink_attacks:
                shutil.rmtree(venv_path, ignore_errors=True)
