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

The `-e` is optional but lets modifications to the files take immediate effect without the need to reinstall the
standard every time we change something.

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

If you do not get the expected validation error, make sure you followed all the previous instructions.
If it is still not working, feel free to open a new issue.

## Adding new schemas

Next we will take a look on how to add more custom schemas.
First navigate to the directory `/resources/ORGANIZATION_NAME/schemas`.
The `ORGANIZATION_NAME` is a name you specified during the cookiecutter run.
We want to replace the schema for the `weldx.Error` class and create the file `new_error_schema-0.1.0.yaml` in the
`schemas` directory.
Our goal is that the error must always be a quantity with percent as unit.
The original schema allows quantities of any unit and plain numbers as well.

We copy the content of the original schema to our new schema file and modify it so that it looks as follows:

~~~ yaml
%YAML 1.1
---
$schema: "http://stsci.edu/schemas/yaml-schema/draft-01"
id: "asdf://weldx.bam.de/weldx/schemas/measurement/error-0.1.0"

type: object
properties:
  deviation:
    tag: "asdf://weldx.bam.de/weldx/tags/units/quantity-0.1.*"
    wx_unit: "percent"
required: [deviation]
flowStyle: block
...
~~~

`wx_unit` is a special validation key of WelDX that can be combined with a quantity tag to limit the possible units of the quantity.
Its value are the required units.
All other unit will cause an error during schema validation.

Now we open the manifest file of our standard located at `/resources/ORGANIZATION_NAME/manifests`.
Finally, add the following two lines to the `tags` list:

~~~ yaml
  - uri: "asdf://weldx.bam.de/weldx/schemas/measurement/error-0.1.0"
    file: "new_error_schema-0.1.0"
~~~

The full file should look like this:

~~~ yaml
id: http://weldx.bam.de/weldx/standards/manifests/quality_standard_demo-1.0.0
extension_uri: http://weldx.bam.de/weldx/standards/quality_standard_demo-1.0.0
title: Quality Standard Demo
description: |-
  A demonstrative weldx quality standard
asdf_standard_requirement: 1.0.0
tags:
  - uri: "asdf://weldx.bam.de/weldx/schemas/equipment/measurement_equipment-0.1.0"
    file: "measurement_equipment_example_schema-1.0.0"
  - uri: "asdf://weldx.bam.de/weldx/schemas/measurement/error-0.1.0"
    file: "new_error_schema-0.1.0"
~~~

We test if everything works as expected with this short script:

~~~ python
from weldx import Q_, WeldxFile
from weldx.config import enable_quality_standard
from weldx.measurement import Error

enable_quality_standard("quality_standard_demo")

error = Error(Q_("12%"))

tree = dict(error=error)
WeldxFile(tree=tree, mode="rw")
~~~

If you followed the instructions, the script should run without any problems and changing the unit to something else than `%` will cause a validation error.
