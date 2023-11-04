from importlib import import_module
from types import ModuleType
from inspect import getmembers
from typing import Union


from sanic.blueprints import Blueprint


def autodiscover(app, *module_names: Union[str, ModuleType]) -> None:
    mod = app.__module__
    blueprints = set()

    def _find_bps(module: ModuleType) -> None:
        nonlocal blueprints

        for _, member in getmembers(module):
            if isinstance(member, Blueprint):
                blueprints.add(member)

    for module in module_names:
        if isinstance(module, str):
            module = import_module(module, mod)
        _find_bps(module)

    for bp in blueprints:
        app.blueprint(bp)
