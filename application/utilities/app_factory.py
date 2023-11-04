from typing import Optional, Sequence
from sanic import Sanic

from .autodiscovery import autodiscover

DEFAULT_BLUEPRINTS = [
    "blueprints.measurement.view",
    "worker.mongo",
]


def create_app(
    init_blueprints: Optional[Sequence[str]] = None,
) -> Sanic:
    app = Sanic("app")

    if not init_blueprints:
        init_blueprints = DEFAULT_BLUEPRINTS

    autodiscover(app, *init_blueprints)

    return app
