"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""
import os

from edx_lint.cmd.write import write_main

from utils_edx_cookiecutters.layered_cookiecutter import LayeredCookiecutter

layered_cookiecutter = LayeredCookiecutter(os.getcwd())

# Using the template to create things
extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["project_name"] = "{{cookiecutter.repo_name}}"
extra_context["sub_dir_name"] = "{{cookiecutter.package_name}}"
extra_context["project_short_description"] = "{{cookiecutter.project_desc}}"
extra_context["version"] = "{{cookiecutter.version}}"
extra_context["author_name"] = "{{cookiecutter.author_name}}"
extra_context["author_email"] = "{{cookiecutter.author_email}}"
extra_context["open_source_license"] = "{{cookiecutter.open_source_license}}"
extra_context["setup_py_loading_pkg_data"] = "yes"
setup_py_keyword_args = """entry_points={
        'xblock.v1': [
            '{{cookiecutter.tag_name}} = {{cookiecutter.package_name}}:{{cookiecutter.class_name}}',
        ]
    },
    package_data=package_data("{{cookiecutter.package_name}}", ["static", "public"]),
"""
extra_context["setup_py_keyword_args"] = setup_py_keyword_args
extra_context["placeholder_repo_name"] = "placeholder_repo_name"


layered_cookiecutter.add_template(template_name='python-template', extra_context=extra_context)

# Post build fixes
write_main(['pylintrc'])
