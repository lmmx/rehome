import defopt
import warnings

from .new_home import Rehome

__all__ = ["cli"]

def cli():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        home = defopt.run(Rehome, strict_kwonly=True)
        if home.debug:
            breakpoint()
