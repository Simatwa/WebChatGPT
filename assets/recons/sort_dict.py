import json
import logging
import os
from sys import exit

root_path = os.path.dirname(__file__)

path_to_dict = "dict.txt"
path_to_save = "dict-sorted.txt"
indent_level = 4  # Json indent level
# echo = True  # stdout contents of files

logging.basicConfig(
    format="%(asctime)s - %(levelname)s : %(message)s [%(funcName)s : %(lineno)d]",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

get_exc = lambda e: e.args[1] if len(e.args) > 1 else str(e)

abs_path = lambda path: os.path.join(root_path, path)


def error_handler(exit_on_error=False):
    """Decorator for handling exceptions"""

    def decorator(func):
        def main(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # logging.exception(e)
                logging.error(get_exc(e))
                if exit_on_error:
                    logging.info("Quitting")
                    exit(1)

        return main

    return decorator


def open_file(path):
    """Reads content of a file"""
    logging.info("Opening path")
    with open(abs_path(path)) as fh:
        return json.load(fh)


def write_data(path, data):
    """Echoes dict data to a file"""
    logging.info("Writing data")
    with open(abs_path(path), "w") as fh:
        json.dump(data, fh, indent=indent_level)


@error_handler(exit_on_error=True)
def main():
    """Startup"""
    write_data(path_to_save, open_file(path_to_dict))


if __name__ == "__main__":
    main()
