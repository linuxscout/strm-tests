#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gettest.py
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

import random

import boolquiz
import ieee754
import question


class correction:
    """Generate the third test"""

    def __init__(self):
        self.qs = question.questionGenerator(latex=True)
        self.bq = boolquiz.bool_quiz()
        self.vf = ieee754.float_point()

    def question_funct(self, minterms, dontcares=[]):
        question = "Etudier la fonction suivante\n"
        arabic = "ادرس الدالة الآتية"
        cnf, dnf = self.bq.form_canonique(minterms)
        data = "F = R(%s)" % repr(minterms)
        answer = ""
        answer += self.bq.truth_table(minterms, latex=True, dontcares=dontcares)
        sop, pos = self.bq.simplify(minterms)
        answer += "\nSum of products \n f(a,b,c,d) = $%s$\n" % self.bq.normalize_latex(
            dnf
        )
        answer += "\nProduct of sums \n f(a,b,c,d) = $%s$\n" % self.bq.normalize_latex(
            cnf
        )
        answer += "\nKarnough map\\todo{fix map}\n"
        answer += self.bq.draw_map(minterms, latex=True)
        answer += "\n\n"
        answer += "Simplified Sum of products: $%s$\n" % self.bq.normalize_latex(sop)
        answer += "\nSimplified Product of sums: $%s$\n" % self.bq.normalize_latex(pos)

        answer += """\paragraph{Logigramme} de la fonction\\\\
        %%\missingfigure[figwidth=6cm]{Logigramme}\n\n"""

        answer += self.bq.draw_logigram(sop)
        return question, arabic, data, answer

    def get_question(self, command, minterms):
        """
        return question from command
        """
        if command == "float":
            return self.question_vf()
        elif command == "intervalle":
            return self.question_intervalle()
        elif command == "complement":
            return self.question_cp()
        elif command == "exp":

            return self.question_exp()
        elif command == "map":

            return self.question_map()
        elif command == "map-sop":

            return self.question_map_for_sop()
        elif command == "function":

            return self.question_funct(minterms)
        else:
            return (
                "Question Error: %s" % command.replace("_", ""),
                "Arabic",
                "Data",
                "Answer",
            )

    def correction(self, questions_table, rand=True, nb=2, repeat=2):
        """generate a test"""

        for cpt, value in enumerate(questions):
            q, ar, data, an = value
            print(
                ("\\paragraph{Q%d}%s\hfill\\aRL{%s}" % (cpt + 1, q, ar)).encode("utf8")
            )
            print(("\n%s" % (data)).encode("utf8"))
        print("\n\n\n\n\\hrule width 1\linewidth")
        # ~ print((u"""\\begin{minipage}{11cm}
        # ~ \paragraph{Q%d}%s
        # ~ \\end{minipage}\\hfill
        # ~ \\begin{minipage}{7cm}
        # ~ \\aRL{%s}
        # ~ \\end{minipage}"""%(cpt+1, q,ar)).encode('utf8'))

        print("\pagebreak \subsection{La correction}")

        for cpt, value in enumerate(questions):
            q, ar, data, ans = value
            print(("\paragraph{Q%d} %s" % (cpt + 1, ans)).encode("utf8"))


def test5():
    ts = correction()
    randq = False
    tests = [
        ["function", [6, 7], [0, 1, 2, 3]],
    ]
    for test in tests:
        minterms = test[1]
        dontcares = test[2]
        question, arabic, data, answer = ts.question_funct(minterms, dontcares)
        print(question)
        print(data)
        print(answer)

        print("\\pagebreak\\section{Questions}\n\n")
    return 0


def main(args):
    test5()


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
