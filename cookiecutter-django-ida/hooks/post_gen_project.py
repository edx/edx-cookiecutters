"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""
import os
import shutil

from cookiecutter.main import cookiecutter
from edx_lint.cmd.write import write_main

# cookiecutter can import a template from either github or from a location on local disk.
# If someone is debugging this repository locally, the below block is necessary to pull in
#   local versions of the templates
EDX_COOKIECUTTER_ROOTDIR = os.getenv('EDX_COOKIECUTTER_ROOTDIR') or 'https://github.com/edx/edx-cookiecutters.git'


def move(src, dest):
    """
    Use to move files or folders without replacement.
    """
    if os.path.isfile(dest):
        os.remove(src)
        return
    if os.path.isdir(src) and os.path.isdir(dest):
        dir_contents = os.listdir(src)
        for content in dir_contents:
            move(os.path.join(src, content), os.path.join(dest, content))
        os.rmdir(src)
    else:
        shutil.move(src, dest)


def remove(path):
    """
    Use to remove either a file or a whole directory.
    """
    full_path = os.path.join(os.getcwd(), path)
    if os.path.isfile(full_path):
        os.remove(full_path)
    elif os.path.isdir(full_path):
        shutil.rmtree(full_path)
    else:
        print(f"{full_path} not in cookiecutter output")


# Use Python template to get python files

# output location for python-template cookiecutter
python_placeholder_repo_name = "placeholder_repo_name_0"

extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["sub_dir_name"] = "{{cookiecutter.repo_name}}"
extra_context["project_name"] = "{{cookiecutter.project_name}}"
extra_context["project_short_description"] = "{{cookiecutter.project_short_description}}"
extra_context["version"] = "{{cookiecutter.version}}"
extra_context["author_name"] = "{{cookiecutter.author_name}}"
extra_context["author_email"] = "{{cookiecutter.author_email}}"
extra_context["open_source_license"] = "{{cookiecutter.open_source_license}}"

extra_context["placeholder_repo_name"] = python_placeholder_repo_name

cookiecutter(
    EDX_COOKIECUTTER_ROOTDIR,
    extra_context=extra_context,
    no_input=True,
    directory='python-template',
)

project_root_dir = os.getcwd()
python_template_cookiecutter_output_loc = os.path.join(project_root_dir, python_placeholder_repo_name)
files = os.listdir(python_template_cookiecutter_output_loc)

for f in files:
    move(os.path.join(python_template_cookiecutter_output_loc, f), os.path.join(project_root_dir, f))

os.rmdir(python_template_cookiecutter_output_loc)

# Removing unecessary files from python and django templates:
remove("setup.py")
remove("tox.ini")
remove("MANIFEST.in")

write_main(['pylintrc'])
