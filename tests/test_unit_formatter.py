import unittest
import tempfile
import os
from strmquiz.display.quiz_format import quiz_format  # تأكد من استيراد فئة Formatter


class TestFormatter(unittest.TestCase):

    def setUp(self):
        # إنشاء مجلد مؤقت للقوالب
        self.temp_dir = tempfile.TemporaryDirectory()
        template_base = os.path.join(self.temp_dir.name, "float")
        # Create the "float" directory
        os.makedirs(template_base, exist_ok=True)

        # إنشاء قالب للسؤال
        with open(os.path.join(template_base, "question.tex"), "w", encoding="utf-8") as f:
            text = "سؤال: {{ arabic_text }}\"nQuestion: {{ question_text }}\nNumber: {{ number }}"\
                + "Representation: {{ ieee_representation }}"
            f.write(text)

        # إعداد Formatter
        self.formatter = quiz_format(lang="ar-en", formatting="tex", templates_dir=self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_render_question_answer(self):
        context = {
            "question_text": "Representer sous la norme IEEE-754 32 bits le nombre suivant",
            "arabic_text": "مثل العدد الآتي حسب المعيار IEEE-754 32 bits",
            "number": 12.345,
            "ieee_representation": "01000001010001011010000111101011"
        }

        question, answer = self.formatter.render_question_answer("float", context)

        self.assertIn("مثل العدد", question)
        self.assertIn("12.345", question)
        self.assertIn("01000001", answer, msg=f"{answer}")

if __name__ == '__main__':
    unittest.main()
