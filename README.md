# DHM Example Module

Basic module meant as a plugin for dhm_module_base. It shows basic functionality on how to "plug" in commands into the main CLI.

Plugin for https://github.com/Kortforsyningen/dhm-module-base

The CLI module is based on Click https://click.palletsprojects.com/en/7.x/

Module is packaged by PyPi: https://pypi.org/project/dhm-module-example/

Build status Linux: [![CircleCI](https://circleci.com/gh/Kortforsyningen/dhm-module-example.svg?style=svg)](https://circleci.com/gh/Kortforsyningen/dhm-module-example)

## Installation

### Conda Environment

```
git clone https://github.com/Kortforsyningen/dhm-module-example
cd dhm-module-example
conda env create -n dhm_module_example -f environment.yml
conda activate dhm_module_example
pip install .
```

The plugin can also be installed in developer or "editable" mode.

```
git clone https://github.com/Kortforsyningen/dhm-module-example
cd dhm-module-base
conda env create -n dhm_module_example -f environment-dev.yml
conda activate dhm_module_example
pip install -e .
```

# Usage

This plugin has `dhm_module_base` https://github.com/Kortforsyningen/dhm-module-base as a dependency, and does not work without it.

This plugin "plugs" into `dhm_module_base` using a click group and a set of entrypoints in `setup.py`

Adding commands is done by adding an entrypoint to `setup.py` under the `[dhm_module_base.plugins]` section. Each command **has** to be added here for it to be exposed on the CLI.

```
ENTRY_POINTS = """
      [dhm_module_base.plugins]
      inout=dhm_module_example.core:inout
      pipe=dhm_module_example.core:pipe
      configuration=dhm_module_example.core:configuration

"""
```

Calling the base plugin will now reveal these three commands:

```
Usage: dhm_module_base [OPTIONS] COMMAND [ARGS]...

  dhm_module_base command line interface.

Options:
  --version                       Show the version and exit.
  -v, --verbosity [CRITICAL|ERROR|WARNING|INFO|DEBUG]
                                  Set verbosity level
  -c, --config FILENAME           Configuration file
  --help                          Show this message and exit.

Commands:
  configuration  Example command configuration.
  inout          Example command inout.
  pipe           Example of a custom options handler being used along with
                 a...
```

If a command is **not** able to be imported it is considered broken, and will display a small error on the CLI. If we deliberately break a command (we can mispell to command in the entrypoing) we get the following error:

```
Usage: dhm_module_base [OPTIONS] COMMAND [ARGS]...

  dhm_module_base command line interface.

Options:
  --version                       Show the version and exit.
  -v, --verbosity [CRITICAL|ERROR|WARNING|INFO|DEBUG]
                                  Set verbosity level
  -c, --config FILENAME           Configuration file
  --help                          Show this message and exit.

Commands:
  configuration  † Warning: could not load plugin. See `dhm_module_base
                 configuration --help`.

  inout          Example command inout.
  pipe           Example of a custom options handler being used along with
                 a...
```

To debug, we check `dhm_module_base configuration --help` and get the following output:

```
ImportError: module 'dhm_module_example.core' has no attribute 'configurationsssss'
```

This error is fabricated for the purpose of this example. Usually commands will return errors if package requirements are not met, commands are not linked properly in setup.py etc.

## Registering a new command

Registering a new command is done by decorating a python function with the `@click.command()` decorator, telling click that the function is a CLI command. Descriptions are harvested by the functions docstring, so make sure it's descriptive of what the command does. Arguments and options are added by using the `@click.argument()` and `@click.option()` decorators. For more information see:

https://click.palletsprojects.com/en/7.x/quickstart/#basic-concepts-creating-a-command

## Accessing the configuration object

Click commands can access the current context `ctx` by decorating commands with `@click.pass_context` and setting the first argument to `ctx`. The base module puts the configuration object on `ctx.obj["config"]`, so if a command is decorated with `@click.pass_context` this context can be fetched. See https://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts.

The base module can be supplied with an `.ini` file using the `-c | --config` option. A command could look like `dhm_module_base -c "config.ini" inout - "out.txt"` which will call the `inout` plugin command with a base configuration in `config.ini`. If inout is decorated with `pass_context`, configuration specific options like database connections or paths can be retrieved.
