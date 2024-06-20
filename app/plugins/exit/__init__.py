import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        logging.info("Exitiung...")
        sys.exit("Exiting...")