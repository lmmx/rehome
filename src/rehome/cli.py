import defopt

from .new_home import Rehome

__all__ = ["cli"]


def cli():
    home = defopt.run(Rehome, cli_options="has_default", no_negated_flags=True)
    if home.debug:
        breakpoint()
