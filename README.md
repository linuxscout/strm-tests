# STRM Tests

Create Random tests for Structure Machine 1 and 2 - first Year MI, Mathematics &amp; Informatics in Algerian universities.

توليد الفحوص والأسئلة في مادة "بنية الآلة 1" لشعبة الرياضيات والإعلام الآلي في الجامعة الجزائرية

##  مزايا

* توليد الفحوص والأسئلة مع الحلول
* تدعم الفصول الآتية:
  * أنظمة التعداد
  * تمثيل الأعداد الطبيعية والحقيقية والحروف
  * ترميز المعلومات
  * الجبر البولياني
* تولّد الأجوبة :
  * إمكانية رسم مخطط دالة منطقية
  * توليد جداول كارنوف
  * توليد الحلول البيانية لجدول كارنوف
* توليد نماذج مكررة من الأسئلة لتسهيل الطباعة
* توليد عشوائي للأسئلة

  Developers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
------------|-----------
Authors  | Taha Zerrouki: http://tahadz.com,  taha dot zerrouki at gmail dot com
Release  | 0.2
License  |[GPL](https://github.com/linuxscout/strm-tests/master/LICENSE)
Tracker  |[linuxscout/strm-tests/Issues](https://github.com/linuxscout/strm-tests/issues)
Website  |[https://github.com/linuxscout/strm-tes)[github)
Source  |[Github](https://github.com/linuxscout/strm-tests)
Feedbacks  |[Comments](https://github.com/linuxscout/strm-tests/issues)
Accounts  |[@Twitter](https://twitter.com/linuxscout) 




## تطبيقات 
* توليد الأسئلة

## Requirements
* Need :

 	- sympy>=1.7.1
 * to produce Latex/pdf
	 - Need Linux command line 'make'
	 - Latex commands (texlive)
 * To launch GUI
	- pywebview>=3.5
	- moodlexport>=0.0.29
	- webview>=0.1.5

## Usage

* Graphical interface
```
python3 strm_tests_webviewer.py
```


* Generate test n° 1
```
make test1 
make test2 
make test3

```

* Generate Moodle questions bank

هذا سيولد ملفات latex موضوعة في المجلد edits

### Available commands:
 This commands are used to generate question within a test

Category |Command | explaination
---------|--------|-------------
Codage | "base" |    Convert between numeral bases
Codage | "arithm" | Make arithmetic calculus between bases 
Codage | "mesure" | Conversion between different measure units 
Codage | "float" | Question about floating points representation IEEE-754
Codage | "intervalle" | Question about integer numbers intervals with VS/Complement 1  and complement 2 
Codage | "complement" | Complement to one and two
Logic | "exp" |     Boolean expression to simplify
Logic |"map" |     Simplify a Karnaugh Map
Logic |"map-sop" |      Simplify a Karnaugh Map with canonic forms
Logic | "function" |    Study a logical function
Logic | "static_funct" |  Study a logical function given by canonical form
Logic | "multi_funct" | Draw a circuit with multi functions given by min-terms 
Sequentiel | "chronogram" | Draw a chronogram question with D, JK, RS flip-flop 

### Use config file

We can use a configuration file to configure multiple tests generation

see config/quiz.conf

