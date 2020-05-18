# DHM Example Module

Build status Linux: [![CircleCI](https://circleci.com/gh/Kortforsyningen/dhm-module-example.svg?style=svg)](https://circleci.com/gh/Kortforsyningen/dhm-module-example)

# Usage

todo

## Accessing the configuration object

Click commands can access the current context `ctx` by decorating commands with `@click.pass_context` and setting the first argument to `ctx`. The base module puts the configuration object on `ctx.obj["config"]`, so if a command is decorated with `@click.pass_context` this context can be fetched. See https://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts.

The base module can be supplied with an `.ini` file using the `-c | --config` option. A command could look like `dhm_module_base -c "config.ini" inout - "out.txt"` which will call the `inout` plugin command with a base configuration in `config.ini`. If inout is decorated with `pass_context`, configuration specific options like database connections or paths can be retrieved.
