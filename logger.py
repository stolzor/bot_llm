import logging
import sys


def get_logger(process_name: str, filename: str) -> logging.Logger:
    """Create logger

    Args:
        process_name (str): process name

    Returns:
        logging.Logger: logger which logging some information
    """
    logger = logging.getLogger(process_name)
    logger.setLevel(logging.INFO)

    formmater = logging.Formatter(
        "%(asctime)s %(name)-12s %(levelname)-8s %(message)s", "%m-%d-%Y %H:%M"
    )
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formmater)

    fh = logging.FileHandler(f"logs/{filename}")
    fh.setLevel(logging.INFO)
    fh.setFormatter(formmater)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger
