"""
    Functions to help test cookiecutters
"""

import os
from contextlib import contextmanager


@contextmanager
def inside_dir(dirpath):
    """
    Change into a directory and change back at the end of the with-statement.

    Args:
        dirpath (str): the path of the directory to change into.

    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Bake a cookiecutter, and switch into the resulting directory.

    Args:
        cookies (pytest_cookies.Cookies): the cookie to be baked.

    """
    result = cookies.bake(*args, **kwargs)
    if result.exception:
        raise result.exception
    with inside_dir(str(result.project)):
        yield
