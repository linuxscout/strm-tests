#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz_builder.py
#  
#  Copyright 2019 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import logging
# --- Configure logging ---
logging.basicConfig(
    level=logging.DEBUG,  # change to INFO or WARNING in production
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)

import random

from .display import quiz_format_factory

from deprecated import deprecated
# 🔹 Constants
LANG_AR = "arabic"
LANG_EN = "english"


class Question_Builder:
    """Generate quiz questions for different domains."""

    def __init__(self, outformat="latex", config_file="", lang="ar-en", templates_dir="",):
        # 🔹 Inject dependencies (makes testing easier)
        self.rng = random.Random()
        # self.qs = question.questionGenerator(latex=True)
        # self.bq = boolquiz.bool_quiz()
        # self.bq.set_format('')
        # self.vf = ieee754.float_point()

        self.formater = quiz_format_factory.quiz_format_factory.factory(outformat,
                                                                        # lang=lang, templates_dir=templates_dir
        )

    # 🔹 Common rendering helper
    @deprecated(reason=" All format and rendrening operation are moved to quizbuilder")
    def _render(self, template: str, context: dict):
        """Render a question and answer using the current formatter."""
        try:
            q, a = self.formater.render_question_answer(template, context)
            # return q, LANG_AR, "data", a
            return q, a
        except Exception as e:
            logger.exception("Error rendering template %s", template)
            return f"Error: {e}",  "Error"

    def use_fixed_random(self, rng=None):
        """
        Ensure that self.rng has the required methods:
        - randint
        - choice
        - choices

        If rng is missing or incomplete, fallback to random.Random().
        """
        required_methods = {"randint", "choice", "choices"}

        if rng is not None and all(hasattr(rng, m) for m in required_methods):
            self.rng = rng
        else:
            self.rng = random.Random()

        return self.rng

    def use_formatter(self, formatter=None):
        obj = formatter
        method_name = "render_question_answer"
        method = getattr(obj, method_name, None)
        if not callable(method):
            raise AttributeError(f"In method 'use_formatter', {obj.__class__.__name__} has no callable method '{method_name}'")
        else:
            self.formater = formatter
        return method



def main(args):
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
