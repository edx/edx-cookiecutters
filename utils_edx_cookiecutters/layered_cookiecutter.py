"""
    Helps create a cookiecutter using layered approach
"""
from os import getenv
from pathlib import Path
from shutil import move as shutil_move
from shutil import rmtree as shutil_rmtree

from cookiecutter.main import cookiecutter
from edx_lint.cmd.write import write_main


class LayeredCookiecutter():
    """
    Class to help facilitate usage of the layered cookiecutter approach
    """

    # cookiecutter can import a template from either github or from a location on local disk.
    # If someone is debugging this repository locally, the below block is necessary to pull in
    #   local versions of the templates
    EDX_COOKIECUTTER_ROOTDIR = Path(
        getenv('EDX_COOKIECUTTER_ROOTDIR') or 'https://github.com/edx/edx-cookiecutters.git'
        )

    def __init__(self, project_rootdir, edx_cookiecutter_rootdir=None):
        if edx_cookiecutter_rootdir is not None:
            self.EDX_COOKIECUTTER_ROOTDIR = Path(edx_cookiecutter_rootdir)
        self.templates = []
        self.project_rootdir = Path(project_rootdir)

    def move(self, src, dest):
        """
        Use to move files or folders without replacement.
        """
        src = Path(src)
        dest = Path(dest)
        if dest.is_file():
            src.unlink()
            return
        if src.is_dir() and dest.is_dir():
            for content in src.iterdir():
                self.move(src / content, dest / content)
            src.rmdir()
        else:
            shutil_move(src, dest)

    def remove(self, path):
        """
        Use to remove either a file or a whole directory.
        """
        path = Path(path)
        full_path = self.project_rootdir / path
        if full_path.is_file():
            full_path.remove()
        elif full_path.is_dir():
            shutil_rmtree(full_path)
        else:
            print("{path} not in cookiecutter output".format(path=full_path))

    def add_template(self, template_name, extra_context, remove_object=None):
        """
        Used to add templates.

        The templates will be used in order they are added.
        """
        if remove_object is None:
            remove_object = []
        template_info = {
                "extra_context": extra_context,
                "template_name": template_name,
                "remove_object": remove_object,
                }
        self.templates.append(template_info)

    def create_cookiecutter(self):
        """
        creates cookeicutter using templates added using add_template
        """
        for counter, template in enumerate(self.templates):
            template["extra_context"]["placeholder_repo_name"] = "placeholder_dir_{}".format(counter)
            cookiecutter(
                    str(self.EDX_COOKIECUTTER_ROOTDIR),
                    extra_context=template["extra_context"],
                    no_input=True,
                    directory=template["template_name"],
                )

            template_output_loc = self.project_rootdir / Path(template["extra_context"]["placeholder_repo_name"])
            for f in template_output_loc.iterdir():
                self.move(template_output_loc / f, self.project_rootdir / f.name)

            for object_name in template["remove_object"]:
                self.remove(object_name)
            # Post build fixes
            write_main(['pylintrc'])
