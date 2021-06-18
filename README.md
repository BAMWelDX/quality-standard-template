# quality-standard-template

Setup steps:

- install cookiecutter
  ```
  conda install cookiecutter
  ```
- navigate your terminal into the directory where you want to create the project
- start the cookiecutter setup
  ```
  cookiecutter https://github.com/BAMWeldx/quality-standard-template
  ```
- fill out all fields as necessary
- the template automatically creates a git repository and tags `0.1.0` release
- test installing the created project
  ```
  pip install -e ./quality_standard_demo
  ```
  (careful, this will install weldx from pypi if weld is not locally installed)
