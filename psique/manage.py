#!/usr/bin/env python
import os
import sys
from pathlib import Path

from utils.settings import get_project_package

PROJECT_DIR = Path(__file__).absolute().parent
PROJECT_PACKAGE = get_project_package(PROJECT_DIR)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_PACKAGE}.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
