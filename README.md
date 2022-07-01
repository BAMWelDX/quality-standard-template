# quality-standard-template

## About

This repository is a template to create installable quality standards for the WelDX Python API.
Check out the [corresponding tutorial](https://weldx.readthedocs.io/en/latest/tutorials/quality_standards.html) if you 
don't know what quality standards are.

## Basic setup

Open a terminal and install `cookiecutter` using conda:

~~~ shell
conda install cookiecutter -c conda-forge
~~~

Navigate to the directory where you want the new quality standard to be created.
Note that `cookiecutter` creates a new directory with the name of the quality standard that will contain all the files.
Now execute:

~~~
cookiecutter https://github.com/BAMWeldx/quality-standard-template
~~~

Now you need to fill out a bunch of fields on accept the default values displayed in brackets.
Before finishing, you will be asked if you want to create git repository automatically.
If you choose yes, the initial commit will be tagged as the `0.1.0`.
Note that the current installation setup requires the files to be in a git repository.
So if you didn't choose to create a repository automatically, you need to do it manually before you can continue.

Now navigate to the newly created directory and run:


~~~ shell
pip install -e .
~~~

> **IMPORTANT NOTE:** This will install `weldx` from pypi if `weldx` is not locally installed

## Checking the installation

The template automatically creates a first schema and the necessary manifest file.
You can use them to check if everything is configured correctly.
Create a new python file and copy the following code into it:

~~~ python
from weldx import WeldxFile
from weldx.config import enable_quality_standard
from weldx.measurement import MeasurementEquipment

enable_quality_standard("quality_standard_demo")

me = MeasurementEquipment("Equipment")

# me.wx_metadata = {"serial_number": 1234}

tree = dict(equip=me)
WeldxFile(tree=tree, mode="rw")

~~~

If you run the script, you should get a validation error because the schema included in the template requires a `MeasurementEquipment` to have a `wx_metadata` field containing a `serial_number`.
In case you do not get the error the setup has failed.

The validation error should disappear if you uncomment the line containing `me.wx_metadata = {"serial_number": 1234}`.
Removing `enable_quality_standard("quality_standard_demo")` should also remove the error.

## Adding new schemas

...