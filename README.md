# Toolbox_subpackage2
The whole plan to have a internal package named **MolDesToolBox** and create different subpackage within the framwork    
This is a simple repo ashowing the right folder structure and setting in the `project.toml` 

[Toolbox_subpackage1](https://github.com/WHPAN0108/Toolbox_subpackage1) is another repo in the **MolDesToolBox**

## Install

If you have [poetry](https://python-poetry.org/) installed 

```shell
poetry add git+https://github.com/WHPAN0108/Toolbox_subpackage2
```

You can also use `pip`
```shell
pip install git+https://github.com/WHPAN0108/Toolbox_subpackage2
```

## Test if susseesful installed

You can try in the python console
```python
>>> from BioInfoToolBox.goodbye import Goodbye
>>> Goodbye.goodbye()
Goodbye World
```
