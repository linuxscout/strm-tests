import unittest
import os

import unittest
from strmquiz.question_builder import Question_Builder  # تأكد من المسار الصحيح
# from strmquiz.display.quiz_format_factory import quiz_format_factory

class TestQuestionBuilder(unittest.TestCase):

    def setUp(self):
        # إعداد Formatter تجريبي بقوالب افتراضية
        self.qb = Question_Builder(
            outformat="tex",
            lang="ar-en",
            templates_dir = os.path.join(os.getcwd(),"strmquiz/templates")  # مجلد يحتوي على قوالب test
        )


    def test_question_vf_structure(self):
        result = self.qb.question_vf()

        # تحقق من أن النتيجة عبارة عن 4 عناصر
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)

        question, arabic, data, answer = result

        self.assertIsInstance(question, str)
        self.assertIsInstance(answer, str)

        self.assertIn("IEEE", question)
        self.assertIn("Pseudo-mantissa", answer)
        # self.assertTrue(False, msg=f"{question} \n{answer}")

    def test_prepare_kmap_data_basic(self):
        minterms = [1,3,6,7]
        simply_terms = self.qb.bq.simplify_map(minterms)
        print(simply_terms)
        result = self.qb.prepare_kmap_data(
            minterms=minterms,
            dontcares=[5, 9],
            correct=True,
            variables=["A", "B", "C", "D"],
            simply_terms= simply_terms,
            method="sop"
        )

        expected_maxterms = [x for x in range(16) if x not in minterms and x not in [5, 9]]

        self.assertEqual(result["minterms"], minterms)
        self.assertEqual(result["dontcares"], [5, 9])
        self.assertEqual(result["maxterms"], expected_maxterms)
        self.assertEqual(result["variables"], ["A", "B", "C", "D"])
        self.assertEqual(result["ab"], "AB")
        self.assertEqual(result["cd"], "CD")
        self.assertEqual(result["simplification"], ["a'.b.c", "a'.b'.d"])
        self.assertEqual(result["simplify_terms"], "CD")
if __name__ == '__main__':
    unittest.main()
