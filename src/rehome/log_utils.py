import logging

__all__ = ["set_up_logging"]


def set_up_logging(name: str, quiet: bool = True):
    """
    Initialise the log

    Args:
      name  : To be set as ``__name__`` from the calling module
      quiet : Change this flag to True/False to turn off/on console logging
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")
    if not quiet:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(log_format)
        logger.addHandler(console)
    return logger
