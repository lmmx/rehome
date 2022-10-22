import defopt

from .new_home import Rehome

__all__ = ["cli"]

def cli():
    home = defopt.run(Rehome)
    breakpoint()
