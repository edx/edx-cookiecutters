.PHONY: help quality requirements test upgrade validate

BAKE_OPTIONS=--no-input

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade.
PIP_COMPILE = pip-compile --upgrade $(PIP_COMPILE_OPTS)

TEMPLATES=$(wildcard cookiecutter-*)
.PHONY: $(TEMPLATES)
$(TEMPLATES): requirements ## Create a new repo from the template
	test -e var/ || mkdir var
	EDX_COOKIECUTTER_ROOTDIR=$(PWD) cookiecutter $(PWD) --directory $(@) --output-dir var

# Order is very important in this list: files must appear after everything they include!
REQ_FILES = \
	requirements/pip-tools \
	requirements/base \
	requirements/test \
	requirements/ci \
	requirements/dev \


upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade

upgrade: ## update the pip requirements files to use the latest releases satisfying our constraints
	pip install -qr requirements/pip-tools.txt
	@ export REBUILD='--rebuild'; \
	for f in $(REQ_FILES); do \
		echo ; \
		echo "== $$f ===============================" ; \
		echo "pip-compile -v --no-emit-trusted-host --no-index $$REBUILD --upgrade -o $$f.txt $$f.in"; \
		pip-compile -v --no-emit-trusted-host --no-index $$REBUILD --upgrade -o $$f.txt $$f.in || exit 1; \
		export REBUILD=''; \
	done
	scripts/post-pip-compile.sh $(REQ_FILES:=.txt)

quality: ## check coding style with pycodestyle and pylint
	pylint */hooks/pre_gen_project.py */hooks/post_gen_project.py
	pycodestyle */hooks/pre_gen_project.py */hooks/post_gen_project.py
	pydocstyle */hooks/pre_gen_project.py */hooks/post_gen_project.py

	pylint utils_edx_cookiecutters test_utils
	pycodestyle tests utils_edx_cookiecutters test_utils
	isort --check-only --diff --recursive */hooks tests utils_edx_cookiecutters test_utils

requirements: ## install development environment requirements
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip-tools.txt
	pip install -r requirements/dev.txt

test: ## run tests on every supported Python version
	tox

validate: ## run tests and quality checks
	tox -e quality,py38
