# STRM Tests

Create Random tests for Stucture Machine 1- first Year MI, Mathematiques &amp; Informatiques in Algerian universities.

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

  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
------------|-----------
Authors  | Taha Zerrouki: http://tahadz.com,  taha dot zerrouki at gmail dot com
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/strm-tests/master/LICENSE)
Tracker  |[linuxscout/strm-tests/Issues](https://github.com/linuxscout/strm-tests/issues)
Website  |[https://github.com/linuxscout/strm-tes)[github)
Source  |[Github](https://github.com/linuxscout/strm-tests)
Feedbacks  |[Comments](https://github.com/linuxscout/strm-tests/issues)
Accounts  |[@Twitter](https://twitter.com/linuxscout) 




## تطبيقات 
* توليد الأسئلة

## Usage

* Generate test n° 1
```
make test1 
make test2 
make test3

```

* Generate moodle questions bank

هذا سيولد ملفات latex موضوعة في المجد edits

### Available commands:
 This commands are used to generate question within a test

Category |Command | explaination
---------|--------|-------------
Codage | "base" |    Convert between numeral bases
Codage | "arithm" |  Make arithmetic calculs between bases
Codage | "mesure" |  Converstion between different mesure units
Codage | "float" | Question about floating points representation IEEE-754
Codage | "intervalle" | Question about integer numbers intervalles with VS/Complement1  and complement 2
Codage | "complement" | Complement to one and two
Logic | "exp" |     Boolean expression to simplify
Logic |"map" |     Simplify a Karnaugh Map
Logic |"map-sop" |      Simplify a Karnaugh Map with canonic forms
Logic | "function" |    Study a logical function
Logic | "static_funct" |  Study a logical function given by canonical form
Logic | "multi_funct" |   Draw a circuit with multi functions given by minterms

### Use config file

We can use a config file to configurate multiple tests generation

see config/quiz.conf

