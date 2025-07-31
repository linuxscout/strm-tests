import unittest


import unittest
from strmquiz.question_builder import Question_Builder  # تأكد من المسار الصحيح
from strmquiz.display.quiz_format_factory import quiz_format_factory

class TestQuestionBuilder(unittest.TestCase):

    def setUp(self):
        # إعداد Formatter تجريبي بقوالب افتراضية
        self.formatter = quiz_format_factory.factory(
            typef="tex",
            lang="ar-en",
            templates_dir="tests/templates"  # مجلد يحتوي على قوالب test
        )
        self.qb = Question_Builder(self.formatter)

    def test_question_vf_structure(self):
        result = self.qb.question_vf()

        # تحقق من أن النتيجة عبارة عن 4 عناصر
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)

        question, arabic, data, answer = result

        self.assertIsInstance(question, str)
        self.assertIsInstance(answer, str)

        self.assertIn("IEEE", question)
        self.assertIn("bits", answer)

    def test_question_map(self):
        # يجب أن تعالج المعطيات المطلوبة بنجاح وتعيد سؤالًا منطقيًا
        context = {
            "var_names": ["A", "B", "C"],
            "minterms": [5],
            "output_names": ["X"],
            "dontcare": []
        }
        result = self.qb.question_map(context)
        self.assertEqual(len(result), 4)
        self.assertIn("A", result[0])  # السؤال يحتوي أسماء المتغيرات

if __name__ == '__main__':
    unittest.main()
