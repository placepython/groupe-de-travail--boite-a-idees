from pathlib import Path
from subprocess import run
from shutil import rmtree

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Build the frontend assets using webpack'

    def add_arguments(self, parser):
        parser.add_argument('--watch', action="store_true", default=False)

    def handle(self, *args, **options):
        node_modules = Path("./assets/node_modules")
        if not node_modules.exists():
            run(['npm', 'install'], cwd="./assets")

        command = ['npm', 'run']
        if options['watch']:
            command.append("dev:watch")
        else:
            command.append("dev")
        run(command, cwd="./assets")
