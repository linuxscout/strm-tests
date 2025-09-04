import sys
import logging
import builtins
import pytest
import os
from unittest.mock import patch, MagicMock
from strmquiz.quizbuilder import QuizBuilder
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "../","templates")
import strmquiz.__main__ as app  # replace with the actual filename (without .py)
