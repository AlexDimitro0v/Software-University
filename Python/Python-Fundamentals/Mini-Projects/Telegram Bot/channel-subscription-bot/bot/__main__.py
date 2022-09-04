import logging

from .misc import run_bot

FORMAT = "%(levelname)s:%(filename)s:%(funcName)s():%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

run_bot()
