
#  Question

####  Q1

<p>
<span dir="rtl">مثّل بمعيار IEEE-754 علي 32 بت العدد الآتي:</span> / Represent under IEEE-754 32 bits standard the following number:

**158.508**

---

--------

##  Correction

####  Q1

<p>
<span dir="rtl">مثّل بمعيار IEEE-754 علي 32 بت العدد الآتي:</span> / Represent under IEEE-754 32 bits standard the following number:

**158.508**

---

**<span dir="rtl">التمثيل الثنائي النهائي</span> / Final binary representation:** `1001 1110.1001 0100 0111 1010 1110 1100 1100 11`<sub>IEEE-754-32bits</sub>  

| <span dir="rtl">الخطوة</span> / Step                   | <span dir="rtl">القيمة</span> / Value  |
|------------------------|-------|
| <span dir="rtl">المدخل</span> / Input                | (158.5080)<sub>10</sub> = (1001 1110.1001 0100 0111 1010 1110 1100 1100 11)<sub>2</sub> |
| <span dir="rtl">الشكل المعياري</span> / Normalized form       | 1.001 1110 1001 0100 0111 1010 × 2<sup>7</sup> |
| <span dir="rtl">بت الإشارة</span> / Sign bit              | + ⇒ 0 |
| <span dir="rtl">الأس</span> / Exponent              | 7 + 127 = 134 ⇒ (1000 0110)<sub>2</sub> |
| <span dir="rtl">القسم العشري المعدّل</span> / Pseudo-mantissa       | 001 1110 1001 0100 0111 1010 |
| <span dir="rtl">التمثيل النهائي</span> / Final representation  | 0100 0011 0001 1110 1001 0100 0111 1010 |
| <span dir="rtl">الشكل الستعشري</span> / Hexadecimal form      | (431E 947A)<sub>16</sub> |

####  Q1

<span dir="rtl">حدد المجالات التي يمكن تمثيلها لأعداد الموجبة والتمثيل بالقيمة المطلقة والمتمم إلى 1 و 2 على 16 بت</span> / Give the intervals which can be represented in positive numbers, absolute value, 1's complement, and 2's complement on 16 bits.  

---

--------

##  Correction

####  Q1

<span dir="rtl">حدد المجالات التي يمكن تمثيلها لأعداد الموجبة والتمثيل بالقيمة المطلقة والمتمم إلى 1 و 2 على 16 بت</span> / Give the intervals which can be represented in positive numbers, absolute value, 1's complement, and 2's complement on 16 bits.  

---

| <span dir="rtl">عنوان</span> / Label                   | <span dir="rtl">العبارة</span> / Formula            | <span dir="rtl">محسوبة</span> / Evaluated   |
|--------------------------------------------------------|-----------------------------------------------------|---------------------------------------------|
| <span dir="rtl">الأعداد الموجبة</span> / Positives     | [0; 2<sup>(16</sup> - 1)]                           | [0; 65535]                                  |
| <span dir="rtl">القيمة بالإشارة</span> / Signed value  | [-(2<sup>(16-1)</sup> - 1); 2<sup>(16-1)</sup> - 1] | [-32767; 32767]                             |
| <span dir="rtl">المتمم إلى 1</span> / One's complement | [-(2<sup>(16-1) </sup>- 1); 2<sup>(16-1) </sup>- 1] | [-32767; 32767]                             |
| <span dir="rtl">المتمم إلى 2</span> / Two's complement | [-2<sup>(16-1)</sup>; 2<sup>(16-1) </sup>- 1]       | [-32768; 32767]                             |

####  Q1

<span dir="rtl">مثل  العدد الآتي في المتمم إلى الواحد وإلى الاثنين  :</span>
Represent in 1's and 2's complement, the following number

**103**

---

--------

##  Correction

####  Q1

<span dir="rtl">مثل  العدد الآتي في المتمم إلى الواحد وإلى الاثنين  :</span>
Represent in 1's and 2's complement, the following number

**103**

---

- -103 = ( -110 0111 )<sub>2</sub>  
- ( 1001 1000 )<sub>c1</sub>  
- +1  
- ( 1001 1001 )<sub>c2</sub>  

####  Q1

<span dir="rtl">حوّل الأعداد الآتية</span> / Convert the following numbers

`(1010 1110 1000 0100 1010 0000 0100 1000)_2` = `........`_16

--------

##  Correction

####  Q1

<span dir="rtl">حوّل الأعداد الآتية</span> / Convert the following numbers

`(1010 1110 1000 0100 1010 0000 0100 1000)_2` = `(ae84 a048)_16`

  <h3>Convert from base 2 to base 16</h3>
      <table border="1" cellpadding="5" cellspacing="0">
    <tr> <td> Base 2 </td>
        <td>1010</td>
        <td>1110</td>
        <td>1000</td>
        <td>0100</td>
        <td>1010</td>
        <td>0000</td>
        <td>0100</td>
        <td>1000</td>
    </tr>
    <tr> <td> Base 16 </td>
        <td>A</td>
        <td>E</td>
        <td>8</td>
        <td>4</td>
        <td>A</td>
        <td>0</td>
        <td>4</td>
        <td>8</td>
    </tr>
  </table>

####  Q1

<span dir="rtl">احسب ما يلي في الأساس 8</span>
Calculate  the following operations in base 8:

```text
  626 6306
+ 3464 7643
-------------------
= ........

```

--------

##  Correction

####  Q1

<span dir="rtl">احسب ما يلي في الأساس 8</span>
Calculate  the following operations in base 8:

```text
  626 6306
+ 3464 7643
-------------------
= 4313 6151
```

####  Q1

#### <span dir="rtl">رمّز النص الآتي بترميز</span> / Encode the following text into ASCII

**<span dir="rtl">نص:</span> / Text:** "Decode Message 77"

#### <span dir="rtl">فكك الرموز الآتية من ترميز ASCII إلى نص</span> / Decode the following ASCII codes into text

**<span dir="rtl">رموز</span> / Codes:** ['0x44', '0x65', '0x63', '0x6f', '0x64', '0x65', '0x20', '0x4d', '0x65', '0x73', '0x73', '0x61', '0x67', '0x65', '0x20', '0x37', '0x37']

--------

##  Correction

####  Q1

#### <span dir="rtl">رمّز النص الآتي بترميز</span> / Encode the following text into ASCII

  **<span dir="rtl">نص:</span> / Text:** "Decode Message 77"

| <span dir="rtl">محرف</span> / Character | D | e | c | o | d | e | space | M | e | s | s | a | g | e | space | 7 | 7 |
|-----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| <span dir="rtl">رمز ascii</span> / ascii Code Point  | 0x44 | 0x65 | 0x63 | 0x6f | 0x64 | 0x65 | 0x20 | 0x4d | 0x65 | 0x73 | 0x73 | 0x61 | 0x67 | 0x65 | 0x20 | 0x37 | 0x37 |

#### <span dir="rtl">فكك الرموز الآتية من ترميز ASCII إلى نص</span> / Decode the following ASCII codes into text

**<span dir="rtl">رموز</span> / Codes:** ['0x44', '0x65', '0x63', '0x6f', '0x64', '0x65', '0x20', '0x4d', '0x65', '0x73', '0x73', '0x61', '0x67', '0x65', '0x20', '0x37', '0x37']

| <span dir="rtl">رمز ASCII</span> / ASCII Code Point | 0x44 | 0x65 | 0x63 | 0x6f | 0x64 | 0x65 | 0x20 | 0x4d | 0x65 | 0x73 | 0x73 | 0x61 | 0x67 | 0x65 | 0x20 | 0x37 | 0x37 |
|-----------------------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| <span dir="rtl">محرف</span> / Character | D | e | c | o | d | e | space | M | e | s | s | a | g | e | space | 7 | 7 |

####  Q1

####  <span dir="rtl">رمّز الأعداد الآتية بالBCD، ثم اشرح كيفية الجمع في الBCD.</span> / Encode the following numbers into BCD, then illustrate the addition in BCD:
- **A =** `35955`
- **B =** `82202`

--------

##  Correction

####  Q1

(35955)<sub>10</sub> = (0011 0101 1001 0101 0101)<sub>bcd</sub>  
(35955)<sub>10</sub> = (0110 1000 1100 1000 1000)<sub>x3</sub>  

** <span dir="rtl">شرح</span> / Explanation: **  

<span dir="rtl">العشري إلى BCD</span> / Base 10 to BCD

#### X <span dir="rtl">العشري إلى BCD</span> / Decimal to BCD 

|  3 | 5 | 9 | 5 | 5 |
|---|---|---|---|---|
|  0011 | 0101 | 1001 | 0101 | 0101 |

<span dir="rtl">BCD إلى العشري</span> / BCD to base 10

####  <span dir="rtl">العشري إلى BCD</span> / BCD to Decimal 

|  0011 | 0101 | 1001 | 0101 | 0101 |
|---|---|---|---|---|
|  3 | 5 | 9 | 5 | 5 |

###  <span dir="rtl">شرح الجمع في BCD</span> / BCD Addition Explanation 

 <span dir="rtl">الحساب في العشري</span> / Decimal calculation:   
`35955 + 82202 = 118157`  

| <span dir="rtl">الاحتفاظ</span> / Carry in | 1 |  | 1 |  |  |  |
|----------|---|---|---|---|---|---|
| A (dec)  | 0 | 3 | 5 | 9 | 5 | 5 |
| B (dec)  | 0 | 8 | 2 | 2 | 0 | 2 |
| Final (dec) | 1 | 1 | 8 | 1 | 5 | 7 |

###  <span dir="rtl">الجمع في BCD</span> / Addition in BCD 

| Carry In |  |  |  |  |  |  |
|----------|---|---|---|---|---|---|
| A (bin)  | 0000 | 0011 | 0101 | 1001 | 0101 | 0101 |
| B (bin)  | 0000 | 1000 | 0010 | 0010 | 0000 | 0010 |
| Carry Out| 1 |  | 1 |  |  |  || Raw Sum  | 0000 | 1011 | 0111 | 1011 | 0101 | 0111 |
| Correction |  | +110 |  | +110 |  |  |
| Final (bin) | 0001 | 0001 | 1000 | 0001 | 0101 | 0111 |
| Final (dec) | 1 | 1 | 8 | 1 | 5 | 7 |

###  <span dir="rtl">شرح الجمع في EXCESS3</span> / EXCESS3 Addition Explanation 

 <span dir="rtl">الحساب في العشري</span> / Decimal calculation:   
`35955 + 82202 = 118157`  

| <span dir="rtl">الاحتفاظ</span> / Carry in | 1 |  | 1 |  |  |  |
|----------|---|---|---|---|---|---|
| A (dec)  | 0 | 3 | 5 | 9 | 5 | 5 |
| B (dec)  | 0 | 8 | 2 | 2 | 0 | 2 |
| Final (dec) | 1 | 1 | 8 | 1 | 5 | 7 |

###  <span dir="rtl">الجمع في EXCESS3</span> / Addition in EXCESS3 

| Carry In | 1 |  | 1 |  |  |  |
|----------|---|---|---|---|---|---|
| A (bin)  | 0011 | 0110 | 1000 | 1100 | 1000 | 1000 |
| B (bin)  | 0011 | 1011 | 0101 | 0101 | 0011 | 0101 |
| Raw Sum  | 0111 | 0001 | 1110 | 0001 | 1011 | 1101 |
| Correction | -11 | +11 | -11 | +11 | -11 | -11 |
| Final (bin) | 0100 | 0100 | 1011 | 0100 | 1000 | 1010 |
| Final (dec) | 1 | 1 | 8 | 1 | 5 | 7 |

####  Q1

### <span dir="rtl">حوّل العدد الآتي من الثنائي إلى غراي</span> / Convert the following number from Binary to Gray:

`10110000`  

---

### <span dir="rtl">حوّل العدد الموالي من غراي إلى الثنائي</span> / Convert the following number from Gray to Binary:

`11101000`  

--------

##  Correction

####  Q1

### <span dir="rtl">التحويل من الثنائي إلى غراي</span> / Binary → Gray Conversion

**<span dir="rtl">التحويل من الثنائي إلى غراي</span> / Binary → Gray Conversion**

| <span dir="rtl">الثنائي</span> / Binary | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| <span dir="rtl">أسهم</span> / Arrows | ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ | ↘ ⊕ ↓ || <span dir="rtl">غراي</span> / Gray | **1** | **1** | **1** | **0** | **1** | **0** | **0** | **0** |
| <span dir="rtl">الخطوات</span> / Steps | Copy first bit | XOR 1 ⊕ 0 = 1 | XOR 0 ⊕ 1 = 1 | XOR 1 ⊕ 1 = 0 | XOR 1 ⊕ 0 = 1 | XOR 0 ⊕ 0 = 0 | XOR 0 ⊕ 0 = 0 | XOR 0 ⊕ 0 = 0 |

### <span dir="rtl"> ترميز غراي إلى الثنائي</span> / Gray → Binary Conversion

**<span dir="rtl"> ترميز غراي إلى الثنائي</span> / Gray → Binary Conversion**

| <span dir="rtl">غراي</span> / Gray | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| <span dir="rtl">أسهم</span> / Arrows | ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ | ↗ ⊕ ↓ || <span dir="rtl">الثنائي</span> / Binary | **1** | **0** | **1** | **1** | **0** | **0** | **0** | **0** |
| <span dir="rtl">الخطوات</span> / Steps | Copy first bit | XOR 1 ⊕ 1 = 0 | XOR 0 ⊕ 1 = 1 | XOR 1 ⊕ 0 = 1 | XOR 1 ⊕ 1 = 0 | XOR 0 ⊕ 0 = 0 | XOR 0 ⊕ 0 = 0 | XOR 0 ⊕ 0 = 0 |

### <span dir="rtl">توضيح تغيرات البتات (رمز غراي التالي)</span> / Illustration of Bit Change (Next Gray Code)
### <span dir="rtl">توضيح الزيادة في الثنائي</span> / Binary Increment Illustration

**x:** `11101000` → **x+1:** `11101001`  

| <span dir="rtl">موضع</span> / Position | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| x | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| x+1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **1** |*<span dir="rtl">الخلايا المميزة = البتات المعدّلة</span> / Highlighted cell(s) = changed bit(s)*  

### <span dir="rtl">سلسلة ترميز غراي</span> / Gray Code Sequence
### <span dir="rtl">سلسلة ترميز غراي (تغيرات البتات)</span> / Gray Code Sequence (Bit Changes)

| <span dir="rtl">الخطوة</span> / Step | Bit 0 | Bit 1 | Bit 2 | Bit 3 | Bit 4 | Bit 5 | Bit 6 | Bit 7 |
|---|---|---|---|---|---|---|---|---|
| x + 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| x + 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **1** |
| x + 2 | 1 | 1 | 1 | 0 | 1 | 0 | **1** | 1 |

*<span dir="rtl">الخلايا المميزة تبيّن البتات المقلوبة من رمز غراي السابق</span> / Highlighted cell shows the bit that flipped compared to the previous Gray code.*  

####  Q1

# <span dir="rtl">سؤال</span> / Question
**A file of size 500.00 MB is downloaded with a speed of 40.00 Mbps. How long will the download take (in minutes)?**

---

--------

##  Correction

####  Q1

# <span dir="rtl">سؤال</span> / Question
**A file of size 500.00 MB is downloaded with a speed of 40.00 Mbps. How long will the download take (in minutes)?**

---

## <span dir="rtl">معطيات</span> / Given:
- Size = 500.00 MB
- Speed = 40.00 Mbps
- Time = 1.67 minutes

---

## <span dir="rtl">خطوات الحل</span> / Solution steps

| <span dir="rtl">الخطوة</span> / Step | <span dir="rtl">عملية</span> / Operation | <span dir="rtl">عبارة</span> / Expression |
|------|-----------|------------|
| 1 | Convert size to MB | 500.00 MB = 500.00 MB |
| 2 | Convert speed to MB/s | 40.00 Mbps = 5.00 MB/s |
| 3 | Time = Size / Speed | 500.00 ÷ 5.00 = 100.00 seconds |
| 4 | Convert seconds → minutes | 100.00 ÷ 60 = 1.67 minutes |

---

## <span dir="rtl">الجواب</span> / Final Answer
**1.67 minutes**

####  Q1

<span dir="rtl">بسّط العبارة الآتية</span> / Simpilfy the following expression

$$
S =  \overline{a}.b + \overline{a}.\overline{d} + b.\overline{c}.\overline{d} + \overline{b}.c.\overline{d}  +  \overline{a}.b + \overline{a}.\overline{d} + b.\overline{c}.\overline{d} + \overline{b}.c.\overline{d}   
$$

--------

##  Correction

####  Q1

<span dir="rtl">بسّط العبارة الآتية</span> / Simpilfy the following expression

$$
S =  \overline{a}.b + \overline{a}.\overline{d} + b.\overline{c}.\overline{d} + \overline{b}.c.\overline{d}  +  \overline{a}.b + \overline{a}.\overline{d} + b.\overline{c}.\overline{d} + \overline{b}.c.\overline{d}   
$$

<div>

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 1, RMAX 1, CMIN 0, CMAX 3 -->
            <rect x="80" y="140"
                  width="240" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- edge border -->
            <!-- <text x="150" y="20"  font-family="serif" font-size="8">cmin=0 cmax=3 rmin=0 rmax=1 </text>-->
  <path d="M 88,80 L 132,80 Q 140,80 140,88 L 140,192 Q 140,200 132,200 L 88,200"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 268,80 L 312,80 Q 320,80 320,88 M 260,88 L 260,192 Q 260,200 268,200 L 312,200"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 1, RMAX 2, CMIN 0, CMAX 0 -->
            <rect x="80" y="140"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="blue" stroke-width="2"/>
            <!-- edge border -->
            <!-- <text x="150" y="40"  font-family="serif" font-size="8">cmin=3 cmax=3 rmin=0 rmax=3 </text>-->
  <path d="M 260,88 L 260,132 Q 260,140 268,140 L 312,140 Q 320,140 320,132 L 320,88"
        stroke="cyan" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 260,268 L 260,312 M 268,260 L 312,260 Q 320,260 320,268 M 320,268 L 320,312"
        stroke="cyan" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
     </svg>

</div>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products :
 $$
  \overline{a}.b + \overline{a}.\overline{d} + b.\overline{c}.\overline{d} + \overline{b}.c.\overline{d}  
 $$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums :
$$
 (b+\overline{d}).(\overline{a}+\overline{d}).(\overline{a}+b+c).(\overline{a}+\overline{b}+\overline{c})
$$

####  Q1

<span dir="rtl">بسّط  جداول كارنوف الآتية.</span> / Simplify the following Karnaugh table

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
     </svg>

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
     </svg>

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
     </svg>

--------

##  Correction

####  Q1

<span dir="rtl">بسّط  جداول كارنوف الآتية.</span> / Simplify the following Karnaugh table

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- edge border -->
            <!-- <text x="150" y="10"  font-family="serif" font-size="8">cmin=0 cmax=3 rmin=2 rmax=2 </text>-->
  <path d="M 88,200 L 132,200 Q 140,200 140,208 L 140,252 Q 140,260 132,260 L 88,260"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 268,200 L 312,200 Q 320,200 320,208 M 260,208 L 260,252 Q 260,260 268,260 L 312,260"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- edge border -->
            <!-- <text x="150" y="20"  font-family="serif" font-size="8">cmin=2 cmax=2 rmin=0 rmax=3 </text>-->
  <path d="M 200,88 L 200,132 Q 200,140 208,140 L 252,140 Q 260,140 260,132 L 260,88"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 200,268 L 200,312 M 208,260 L 252,260 Q 260,260 260,268 M 260,268 L 260,312"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 1, RMAX 1, CMIN 0, CMAX 1 -->
            <rect x="80" y="140"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="blue" stroke-width="2"/>
            <!-- RMIN 0, RMAX 1, CMIN 0, CMAX 0 -->
            <rect x="80" y="80"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="cyan" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$ 
 a.b.\overline{d} + \overline{b}.c.d + \overline{a}.b.\overline{c} + \overline{a}.\overline{c}.\overline{d}  
$$
-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  :
$$ 
(a+\overline{c}+d).(b+c+\overline{d}).(\overline{a}+b+d).(a+\overline{b}+\overline{c}).(\overline{a}+\overline{b}+\overline{d}) 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- edge border -->
            <!-- <text x="150" y="10"  font-family="serif" font-size="8">cmin=0 cmax=3 rmin=0 rmax=3 </text>-->
  <path d="M 88,80 L 132,80 Q 140,80 140,88 L 140,312 Q 140,320 132,320 L 88,320"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 268,80 L 312,80 Q 320,80 320,88 M 260,88 L 260,312 Q 260,320 268,320 L 312,320"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 0, RMAX 0, CMIN 0, CMAX 3 -->
            <rect x="80" y="80"
                  width="240" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$ 
 \overline{d} + \overline{a}.\overline{b}  
$$
-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  :
$$ 
(\overline{a}+\overline{d}).(\overline{b}+\overline{d}) 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 2, RMAX 3, CMIN 1, CMAX 1 -->
            <rect x="140" y="200"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 0, RMAX 1, CMIN 2, CMAX 2 -->
            <rect x="200" y="80"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
            <!-- edge border -->
            <!-- <text x="150" y="30"  font-family="serif" font-size="8">cmin=0 cmax=3 rmin=3 rmax=3 </text>-->
  <path d="M 88,260 L 132,260 Q 140,260 140,268 L 140,312 Q 140,320 132,320 L 88,320"
        stroke="blue" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 268,260 L 312,260 Q 320,260 320,268 M 260,268 L 260,312 Q 260,320 268,320 L 312,320"
        stroke="blue" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 0, RMAX 0, CMIN 1, CMAX 2 -->
            <rect x="140" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="cyan" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$ 
 a.\overline{c}.d + \overline{a}.c.d + a.\overline{b}.\overline{d} + \overline{a}.\overline{b}.d  
$$
-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  :
$$ 
(a+d).(\overline{b}+d).(a+\overline{b}+c).(\overline{a}+\overline{c}+\overline{d}) 
$$

####  Q1

 <span dir="rtl">لتكن الدالة المعطاة بشكلها القانوني، ارسم جدول كارنو وبسطها.</span> / Let the function be given by its canonical form, Draw the Karnaugh table and simplify.  

- 
$$
 F1(A,B,C,D) = \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.B.\overline{C}.D + A.\overline{B}.\overline{C}.D + A.\overline{B}.C.\overline{D} + A.B.C.D 
$$

- 
$$
 F2(A,B,C,D) = \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.\overline{B}.C.D + \overline{A}.B.\overline{C}.D + A.\overline{B}.\overline{C}.D + A.B.\overline{C}.D + A.B.C.\overline{D} + A.B.C.D 
$$

- 
$$
 F3(A,B,C,D) = \overline{A}.\overline{B}.\overline{C}.\overline{D} + \overline{A}.\overline{B}.\overline{C}.D + \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.\overline{B}.C.D + \overline{A}.B.C.D + A.\overline{B}.\overline{C}.\overline{D} + A.\overline{B}.C.\overline{D} + A.\overline{B}.C.D + A.B.\overline{C}.D 
$$

--------

##  Correction

####  Q1

 <span dir="rtl">لتكن الدالة المعطاة بشكلها القانوني، ارسم جدول كارنو وبسطها.</span> / Let the function be given by its canonical form, Draw the Karnaugh table and simplify.  

$$
 F1(A,B,C,D) = \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.B.\overline{C}.D + A.\overline{B}.\overline{C}.D + A.\overline{B}.C.\overline{D} + A.B.C.D 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 2, RMAX 2, CMIN 2, CMAX 2 -->
            <rect x="200" y="200"
                  width="60" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- edge border -->
            <!-- <text x="150" y="20"  font-family="serif" font-size="8">cmin=3 cmax=3 rmin=0 rmax=3 </text>-->
  <path d="M 260,88 L 260,132 Q 260,140 268,140 L 312,140 Q 320,140 320,132 L 320,88"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 260,268 L 260,312 M 268,260 L 312,260 Q 320,260 320,268 M 320,268 L 320,312"
        stroke="green" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 3, RMAX 3, CMIN 1, CMAX 1 -->
            <rect x="140" y="260"
                  width="60" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="blue" stroke-width="2"/>
            <!-- RMIN 1, RMAX 1, CMIN 1, CMAX 1 -->
            <rect x="140" y="140"
                  width="60" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="cyan" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$
  a.b.c.d + \overline{b}.c.\overline{d} + a.\overline{b}.\overline{c}.d + \overline{a}.b.\overline{c}.d  
$$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  : 
$$
 (c+d).(\overline{b}+d).(a+b+c).(a+\overline{c}+\overline{d}).(b+\overline{c}+\overline{d}).(\overline{a}+\overline{b}+c) 
$$

$$
 F2(A,B,C,D) = \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.\overline{B}.C.D + \overline{A}.B.\overline{C}.D + A.\overline{B}.\overline{C}.D + A.B.\overline{C}.D + A.B.C.\overline{D} + A.B.C.D 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 2, RMAX 2, CMIN 2, CMAX 3 -->
            <rect x="200" y="200"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 2, RMAX 3, CMIN 1, CMAX 1 -->
            <rect x="140" y="200"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
            <!-- RMIN 1, RMAX 2, CMIN 1, CMAX 1 -->
            <rect x="140" y="140"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="blue" stroke-width="2"/>
            <!-- RMIN 0, RMAX 0, CMIN 2, CMAX 3 -->
            <rect x="200" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="cyan" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$
  a.b.c + a.\overline{c}.d + b.\overline{c}.d + \overline{a}.\overline{b}.c  
$$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  : 
$$
 (c+d).(a+b+c).(a+\overline{b}+\overline{c}).(\overline{a}+b+\overline{c}) 
$$

$$
 F3(A,B,C,D) = \overline{A}.\overline{B}.\overline{C}.\overline{D} + \overline{A}.\overline{B}.\overline{C}.D + \overline{A}.\overline{B}.C.\overline{D} + \overline{A}.\overline{B}.C.D + \overline{A}.B.C.D + A.\overline{B}.\overline{C}.\overline{D} + A.\overline{B}.C.\overline{D} + A.\overline{B}.C.D + A.B.\overline{C}.D 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- edge border -->
            <!-- <text x="150" y="10"  font-family="serif" font-size="8">cmin=2 cmax=3 rmin=0 rmax=3 </text>-->
  <path d="M 200,88 L 200,132 Q 200,140 208,140 L 312,140 Q 320,140 320,132 L 320,88"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 200,268 L 200,312 M 208,260 L 312,260 Q 320,260 320,268 M 320,268 L 320,312"
        stroke="red" stroke-width="3"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- RMIN 0, RMAX 0, CMIN 0, CMAX 3 -->
            <rect x="80" y="80"
                  width="240" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
            <!-- conrder border -->
            <rect x="80" y="80"  width="60" height="60" fill="none" stroke="blue" stroke-width="2" stroke-dasharray="2,4" rx="14" ry="14"/>
            <rect x="260" y="80"  width="60" height="60" fill="none" stroke="blue" stroke-width="2" stroke-dasharray="2,4" rx="14" ry="14"/>
            <rect x="80" y="260"  width="60" height="60" fill="none" stroke="blue" stroke-width="2" stroke-dasharray="2,4" rx="14" ry="14"/>
            <rect x="260" y="260"  width="60" height="60" fill="none" stroke="blue" stroke-width="2" stroke-dasharray="2,4" rx="14" ry="14"/>
            <!-- RMIN 0, RMAX 1, CMIN 2, CMAX 2 -->
            <rect x="200" y="80"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="cyan" stroke-width="2"/>
            <!-- RMIN 2, RMAX 2, CMIN 1, CMAX 1 -->
            <rect x="140" y="200"
                  width="60" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="magenta" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products  : 
$$
  \overline{b}.c + \overline{a}.\overline{b} + \overline{b}.\overline{d} + \overline{a}.c.d + a.b.\overline{c}.d  
$$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums  : 
$$
 (\overline{b}+d).(a+\overline{b}+c).(\overline{a}+\overline{b}+\overline{c}).(\overline{a}+b+c+\overline{d}) 
$$

####  Q1

<span dir="rtl">ادرس الدالة الآتية:</span> / Study the following function:

` a.c.\overline{d} + \overline{a}.\overline{b}.c.d  +  a.c.\overline{d} + \overline{a}.\overline{b}.c.d `

--------

##  Correction

####  Q1

<span dir="rtl">ادرس الدالة الآتية:</span> / Study the following function:

` a.c.\overline{d} + \overline{a}.\overline{b}.c.d  +  a.c.\overline{d} + \overline{a}.\overline{b}.c.d `

$$
F = [3, 10, 14] 
$$

**Don't Care**  
$$
F = [] 
$$

** <span dir="rtl">جدول الحقيقة</span> / Truth Table**

| Num | A | B | C | D | F |
|-----|--------------------|--------------------|--------------------|--------------------|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 2 | 0 | 0 | 1 | 0 | 0 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 1 | 0 | 0 | 0 |
| 5 | 0 | 1 | 0 | 1 | 0 |
| 6 | 0 | 1 | 1 | 0 | 0 |
| 7 | 0 | 1 | 1 | 1 | 0 |
| 8 | 1 | 0 | 0 | 0 | 0 |
| 9 | 1 | 0 | 0 | 1 | 0 |
| 10 | 1 | 0 | 1 | 0 | 1 |
| 11 | 1 | 0 | 1 | 1 | 0 |
| 12 | 1 | 1 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 | 1 | 0 |
| 14 | 1 | 1 | 1 | 0 | 1 |
| 15 | 1 | 1 | 1 | 1 | 0 |

** <span dir="rtl">الأشكال القانونية</span> / Canonical Forms  **

$$
F(A, B, C, D) = \overline{A}.\overline{B}.C.D + A.\overline{B}.C.\overline{D} + A.B.C.\overline{D} 
$$

$$
F(A, B, C, D) = (A+B+C+D) . (A+B+C+\overline{D}) . (A+B+\overline{C}+D) . (A+\overline{B}+C+D) . (A+\overline{B}+C+\overline{D}) . (A+\overline{B}+\overline{C}+D) . (A+\overline{B}+\overline{C}+\overline{D}) . (\overline{A}+B+C+D) . (\overline{A}+B+C+\overline{D}) . (\overline{A}+B+\overline{C}+\overline{D}) . (\overline{A}+\overline{B}+C+D) . (\overline{A}+\overline{B}+C+\overline{D}) . (\overline{A}+\overline{B}+\overline{C}+\overline{D}) 
$$

 $$
F(A, B, C, D) = Σ(3, 10, 14) 
$$

$$
F(A, B, C, D) = Π(0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15) 
$$

---

### NAND forms <span dir="rtl">بوابات نفي الوصل</span>

$$
F = (a\uparrow c\uparrow \overline{d})\big\uparrow (\overline{a}\uparrow \overline{b}\uparrow c\uparrow d) 
$$

    <span dir="rtl">شرح</span> / Explanation :
   $$
   F =  a.c.\overline{d} + \overline{a}.\overline{b}.c.d 
   $$
   $$
   F = \overline{\overline{ a.c.\overline{d} + \overline{a}.\overline{b}.c.d }}
   $$
   $$
   F = \overline{\overline{ a.c.\overline{d} }.\overline{ \overline{a}.\overline{b}.c.d }}
   $$
   $$
   F = (a\uparrow c\uparrow \overline{d})\big\uparrow (\overline{a}\uparrow \overline{b}\uparrow c\uparrow d)
   $$

---

### NOR forms <span dir="rtl">بوابات نفي الفصل</span>
$$
F = (\overline{c})\big\downarrow (a\downarrow d)\big\downarrow (a\downarrow \overline{b})\big\downarrow (\overline{a}\downarrow \overline{d}) 
$$

    <span dir="rtl">شرح</span> / Explanation :
$$
F = (c).(a+d).(a+\overline{b}).(\overline{a}+\overline{d}) 
$$
$$ 
F = \overline{\overline{(c).(a+d).(a+\overline{b}).(\overline{a}+\overline{d})}} 
$$
$$ 
F = \overline{\overline{(c)}+\overline{(a+d)}+\overline{(a+\overline{b})}+\overline{(\overline{a}+\overline{d})}} 
$$
$$ 
F = (\overline{c})\big\downarrow (a\downarrow d)\big\downarrow (a\downarrow \overline{b})\big\downarrow (\overline{a}\downarrow \overline{d}) 
$$

---

** <span dir="rtl">جدول كارنوف</span> / Karnaugh map**

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">CD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">AB</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">1</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 2, RMAX 3, CMIN 3, CMAX 3 -->
            <rect x="260" y="200"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 0, RMAX 0, CMIN 2, CMAX 2 -->
            <rect x="200" y="80"
                  width="60" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products : 
$$ 
 a.c.\overline{d} + \overline{a}.\overline{b}.c.d  
$$
-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums : 
$$ 
 (c).(a+d).(a+\overline{b}).(\overline{a}+\overline{d}) 
$$

---

** <span dir="rtl">المخطط المنطقي</span> / Logic diagram  **

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="250" viewBox="0 0 900 180" preserveAspectRatio="xMinYMin meet">
  <style>
    .wire { stroke: #222; stroke-width: 2; fill: none; }
    .gate { stroke: #222; stroke-width: 2; fill: white; }
    .not-bubble { stroke: #222; stroke-width: 2; fill: white; }
    .label { font-family: "DejaVu Sans", "Arial", sans-serif; font-size:14px; text-anchor: middle; }
    .var-name { font-weight: bold; }
  </style>
 <!-- Define NOT gate as reusable symbol -->
  <defs>
    <g id="not-gate">
      <!-- Triangle -->
      <polygon points="0,0 20,10 0,20" stroke="black" fill="none"/>
      <!-- Circle (inversion bubble) -->
      <circle cx="25" cy="10" r="5" stroke="black" fill="none"/>
      <!-- Input wire -->
      <line x1="-5" y1="10" x2="0" y2="10" stroke="black"/>
      <!-- Output wire -->
      <line x1="30" y1="10" x2="35" y2="10" stroke="red"/>
    </g>
 <!-- Define NOR gate as reusable symbol -->
    <g id="nor-gate">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
 <!-- Define OR gate as reusable symbol  NO wires-->
    <g id="or-gate0">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
 <!-- Define OR gate as reusable symbol -->
    <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate3">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate2">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate1">
        <!-- replacement Output wire -->
        <use href="#and-gate1" x="0" y="0"/>
      </g>
<!-- Define BIG OR gate as reusable symbol -->
    <g id="big-or-gate3">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
      <path d="M0,0
               Q40,60 0,125
               Q100,125 125,60
               Q100,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="250" y1="120" x2="300" y2="120" stroke="red"/>
    </g>
        <g id="big-or-gate2">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
     <path d="M0,0
               Q40,40 0,80
               Q80,80 80,40
               Q80,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="80" y1="40" x2="100" y2="40" stroke="red"/>
    </g>
    <!-- Define AND gate as reusable symbol -->
      <g id="and-gate4">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate3">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate2">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate1">
        <!-- replacement Output wire -->
        <line x1="-20" y1="20" x2="80" y2="20" stroke="orange"/>
      </g>
      <g id="and-gate0">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="white"/>
        <!-- Input wires -->
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <!-- NAND Gate -->
    <g id="nand-gate0">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <line x1="-20" y1="10" x2="0" y2="10" stroke="black"/>
      <line x1="-20" y1="30" x2="0" y2="30" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate4">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate3">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate2">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate1">
        <use href="#and-gate1" x="0" y="0"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate0">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate4">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate3">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate2">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate1">
      <use href="#and-gate1" x="0" y="0"/>
    </g>
    <g id="nor-gate-not">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate-not">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    </defs>
   <!-- Draw variables A, B, C, D with NOT gates -->
  <g transform="translate(20,30)">
    <!-- A -->
    <text x="0" y="-5" font-family="serif" font-size="20">A</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(70,30)">
    <!-- B -->
    <text x="0" y="-5" font-family="serif" font-size="20">B</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(120,30)">
    <!-- C -->
    <text x="0" y="-5" font-family="serif" font-size="20">C</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(170,30)">
    <!-- D -->
    <text x="0" y="-5" font-family="serif" font-size="20">D</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
      <!-- Draw terms of fucntion -->
      <g transform="translate(250,100)">
        <!-- Draw the term {'default': "a'.b'.c.d", 'formatted': "a'.b'.c.d"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F  :  a'.b'.c.d</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-145" y1="15" x2="0" y2="15" stroke="red"/>
                <line x1="-120" y1="25" x2="0" y2="25" stroke="black"/>
                <line x1="-70" y1="35" x2="0" y2="35" stroke="black"/>
      </g>
      <g transform="translate(250,150)">
        <!-- Draw the term {'default': "a.c.d'", 'formatted': "a.c.d'"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F  :  a.c.d'</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-220" y1="5" x2="0" y2="5" stroke="black"/>
                <line x1="-120" y1="15" x2="0" y2="15" stroke="black"/>
                <line x1="-45" y1="25" x2="0" y2="25" stroke="red"/>
      </g>
        <g transform="translate(450,125.0)">
        <!-- F -->
        <text x="60" y="15" font-family="serif" font-size="10">F</text>
          <g id="wires">
        <!-- vertical wire -->
        <line x1="-5" y1="5.0" x2="-5" y2="-5.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="5.0" x2="20" y2="5.0" stroke="red"/>
        <!-- vertical wire -->
        <line x1="-5" y1="35.0" x2="-5" y2="45.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="35.0" x2="20" y2="35.0" stroke="red"/>
  </g>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0
               Q8.0,20.0 0,40
               Q24.0,40 40,20.0
               Q24.0,0 0,0"
            stroke="black" fill="white"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        </g>
</svg>

####  Q1

<span dir="rtl">ادرس الدالة الآتية:</span> / Study the following function:

``

--------

##  Correction

####  Q1

<span dir="rtl">ادرس الدالة الآتية:</span> / Study the following function:

``

$$
F1 = [0, 1, 3] 
$$

**Don't Care**  
$$
F1 = [] 
$$

** <span dir="rtl">جدول الحقيقة</span> / Truth Table**

| Num | X | Y | Z | D | F |
|-----|--------------------|--------------------|--------------------|--------------------|---|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 2 | 0 | 0 | 1 | 0 | 0 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 1 | 0 | 0 | 0 |
| 5 | 0 | 1 | 0 | 1 | 0 |
| 6 | 0 | 1 | 1 | 0 | 0 |
| 7 | 0 | 1 | 1 | 1 | 0 |
| 8 | 1 | 0 | 0 | 0 | 0 |
| 9 | 1 | 0 | 0 | 1 | 0 |
| 10 | 1 | 0 | 1 | 0 | 0 |
| 11 | 1 | 0 | 1 | 1 | 0 |
| 12 | 1 | 1 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 | 1 | 0 |
| 14 | 1 | 1 | 1 | 0 | 0 |
| 15 | 1 | 1 | 1 | 1 | 0 |

** <span dir="rtl">الأشكال القانونية</span> / Canonical Forms  **

$$
F1(X, Y, Z, D) = \overline{X}.\overline{Y}.\overline{Z}.\overline{D} + \overline{X}.\overline{Y}.\overline{Z}.D + \overline{X}.\overline{Y}.Z.D 
$$

$$
F1(X, Y, Z, D) = (X+Y+\overline{Z}+D) . (X+\overline{Y}+Z+D) . (X+\overline{Y}+Z+\overline{D}) . (X+\overline{Y}+\overline{Z}+D) . (X+\overline{Y}+\overline{Z}+\overline{D}) . (\overline{X}+Y+Z+D) . (\overline{X}+Y+Z+\overline{D}) . (\overline{X}+Y+\overline{Z}+D) . (\overline{X}+Y+\overline{Z}+\overline{D}) . (\overline{X}+\overline{Y}+Z+D) . (\overline{X}+\overline{Y}+Z+\overline{D}) . (\overline{X}+\overline{Y}+\overline{Z}+D) . (\overline{X}+\overline{Y}+\overline{Z}+\overline{D}) 
$$

 $$
F1(X, Y, Z, D) = Σ(0, 1, 3) 
$$

$$
F1(X, Y, Z, D) = Π(2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) 
$$

---

### NAND forms <span dir="rtl">بوابات نفي الوصل</span>

$$
F1 = (d\uparrow \overline{x}\uparrow \overline{y})\big\uparrow (\overline{x}\uparrow \overline{y}\uparrow \overline{z}) 
$$

    <span dir="rtl">شرح</span> / Explanation :
   $$
   F1 =  d.\overline{x}.\overline{y} + \overline{x}.\overline{y}.\overline{z} 
   $$
   $$
   F1 = \overline{\overline{ d.\overline{x}.\overline{y} + \overline{x}.\overline{y}.\overline{z} }}
   $$
   $$
   F1 = \overline{\overline{ d.\overline{x}.\overline{y} }.\overline{ \overline{x}.\overline{y}.\overline{z} }}
   $$
   $$
   F1 = (d\uparrow \overline{x}\uparrow \overline{y})\big\uparrow (\overline{x}\uparrow \overline{y}\uparrow \overline{z})
   $$

---

### NOR forms <span dir="rtl">بوابات نفي الفصل</span>
$$
F1 = (x)\big\downarrow (y)\big\downarrow (d\downarrow \overline{z}) 
$$

    <span dir="rtl">شرح</span> / Explanation :
$$
F1 = (\overline{x}).(\overline{y}).(d+\overline{z}) 
$$
$$ 
F1 = \overline{\overline{(\overline{x}).(\overline{y}).(d+\overline{z})}} 
$$
$$ 
F1 = \overline{\overline{(\overline{x})}+\overline{(\overline{y})}+\overline{(d+\overline{z})}} 
$$
$$ 
F1 = (x)\big\downarrow (y)\big\downarrow (d\downarrow \overline{z}) 
$$

---

** <span dir="rtl">جدول كارنوف</span> / Karnaugh map**

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">ZD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">XY</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 0, RMAX 0, CMIN 1, CMAX 2 -->
            <rect x="140" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 0, RMAX 0, CMIN 0, CMAX 1 -->
            <rect x="80" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products : 
$$ 
 d.\overline{x}.\overline{y} + \overline{x}.\overline{y}.\overline{z}  
$$
-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums : 
$$ 
 (\overline{x}).(\overline{y}).(d+\overline{z}) 
$$

---

** <span dir="rtl">المخطط المنطقي</span> / Logic diagram  **

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="250" viewBox="0 0 900 180" preserveAspectRatio="xMinYMin meet">
  <style>
    .wire { stroke: #222; stroke-width: 2; fill: none; }
    .gate { stroke: #222; stroke-width: 2; fill: white; }
    .not-bubble { stroke: #222; stroke-width: 2; fill: white; }
    .label { font-family: "DejaVu Sans", "Arial", sans-serif; font-size:14px; text-anchor: middle; }
    .var-name { font-weight: bold; }
  </style>
 <!-- Define NOT gate as reusable symbol -->
  <defs>
    <g id="not-gate">
      <!-- Triangle -->
      <polygon points="0,0 20,10 0,20" stroke="black" fill="none"/>
      <!-- Circle (inversion bubble) -->
      <circle cx="25" cy="10" r="5" stroke="black" fill="none"/>
      <!-- Input wire -->
      <line x1="-5" y1="10" x2="0" y2="10" stroke="black"/>
      <!-- Output wire -->
      <line x1="30" y1="10" x2="35" y2="10" stroke="red"/>
    </g>
 <!-- Define NOR gate as reusable symbol -->
    <g id="nor-gate">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
 <!-- Define OR gate as reusable symbol  NO wires-->
    <g id="or-gate0">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
 <!-- Define OR gate as reusable symbol -->
    <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate3">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate2">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate1">
        <!-- replacement Output wire -->
        <use href="#and-gate1" x="0" y="0"/>
      </g>
<!-- Define BIG OR gate as reusable symbol -->
    <g id="big-or-gate3">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
      <path d="M0,0
               Q40,60 0,125
               Q100,125 125,60
               Q100,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="250" y1="120" x2="300" y2="120" stroke="red"/>
    </g>
        <g id="big-or-gate2">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
     <path d="M0,0
               Q40,40 0,80
               Q80,80 80,40
               Q80,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="80" y1="40" x2="100" y2="40" stroke="red"/>
    </g>
    <!-- Define AND gate as reusable symbol -->
      <g id="and-gate4">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate3">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate2">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate1">
        <!-- replacement Output wire -->
        <line x1="-20" y1="20" x2="80" y2="20" stroke="orange"/>
      </g>
      <g id="and-gate0">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="white"/>
        <!-- Input wires -->
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <!-- NAND Gate -->
    <g id="nand-gate0">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <line x1="-20" y1="10" x2="0" y2="10" stroke="black"/>
      <line x1="-20" y1="30" x2="0" y2="30" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate4">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate3">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate2">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate1">
        <use href="#and-gate1" x="0" y="0"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate0">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate4">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate3">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate2">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate1">
      <use href="#and-gate1" x="0" y="0"/>
    </g>
    <g id="nor-gate-not">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate-not">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    </defs>
   <!-- Draw variables A, B, C, D with NOT gates -->
  <g transform="translate(20,30)">
    <!-- X -->
    <text x="0" y="-5" font-family="serif" font-size="20">X</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(70,30)">
    <!-- Y -->
    <text x="0" y="-5" font-family="serif" font-size="20">Y</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(120,30)">
    <!-- Z -->
    <text x="0" y="-5" font-family="serif" font-size="20">Z</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(170,30)">
    <!-- D -->
    <text x="0" y="-5" font-family="serif" font-size="20">D</text>
    <line x1="10" y1="0" x2="10" y2="200" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="200" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
      <!-- Draw terms of fucntion -->
      <g transform="translate(250,100)">
        <!-- Draw the term {'default': "x'.y'.z'", 'formatted': "x'.y'.z'"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F1  :  x'.y'.z'</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-145" y1="15" x2="0" y2="15" stroke="red"/>
                <line x1="-95" y1="25" x2="0" y2="25" stroke="red"/>
      </g>
      <g transform="translate(250,150)">
        <!-- Draw the term {'default': "d.x'.y'", 'formatted': "d.x'.y'"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F1  :  d.x'.y'</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-145" y1="15" x2="0" y2="15" stroke="red"/>
                <line x1="-70" y1="25" x2="0" y2="25" stroke="black"/>
      </g>
        <g transform="translate(450,125.0)">
        <!-- F1 -->
        <text x="60" y="15" font-family="serif" font-size="10">F1</text>
          <g id="wires">
        <!-- vertical wire -->
        <line x1="-5" y1="5.0" x2="-5" y2="-5.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="5.0" x2="20" y2="5.0" stroke="red"/>
        <!-- vertical wire -->
        <line x1="-5" y1="35.0" x2="-5" y2="45.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="35.0" x2="20" y2="35.0" stroke="red"/>
  </g>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0
               Q8.0,20.0 0,40
               Q24.0,40 40,20.0
               Q24.0,0 0,0"
            stroke="black" fill="white"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        </g>
</svg>

####  Q1

<span dir="rtl">ادرس الدارة الآتية:</span> / Study the following circuit:

-   - 
$$
 F1 = [0, 1, 3] 
$$

  - 
$$
 F2 = [2, 6, 7] 
$$

** <span dir="rtl">الحالات الممنوعة</span> / Don't Care **  
-   - 
$$
 F1 = [] 
$$

  - 
$$
 F2 = [] 
$$

$$
 F(A,B,C,D) =  
$$

--------

##  Correction

####  Q1

<span dir="rtl">ادرس الدارة الآتية:</span> / Study the following circuit:

-   - 
$$
 F1 = [0, 1, 3] 
$$

  - 
$$
 F2 = [2, 6, 7] 
$$

** <span dir="rtl">الحالات الممنوعة</span> / Don't Care **  
-   - 
$$
 F1 = [] 
$$

  - 
$$
 F2 = [] 
$$

$$
 F(A,B,C,D) =  
$$

** <span dir="rtl">المداخل والمخارج</span> / Inputs and Outputs  <span dir="rtl">المداخل والمخارج</span>**

- Inputs  
  - X = 0 / 1
  - Y = 0 / 1
  - Z = 0 / 1
  - D = 0 / 1

- Outputs  
  - F1 = 0 / 1
  - F2 = 0 / 1

** <span dir="rtl">جدول الحقيقة</span> / Truth Table**

| Num | X | Y | Z | D  | F1  | F2  |
|-----|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| 0 | 0 | 0 | 0 | 0 | 1 | 0  |
| 1 | 0 | 0 | 0 | 1 | 1 | 0  |
| 2 | 0 | 0 | 1 | 0 | 0 | 1  |
| 3 | 0 | 0 | 1 | 1 | 1 | 0  |
| 4 | 0 | 1 | 0 | 0 | 0 | 0  |
| 5 | 0 | 1 | 0 | 1 | 0 | 0  |
| 6 | 0 | 1 | 1 | 0 | 0 | 1  |
| 7 | 0 | 1 | 1 | 1 | 0 | 1  |
| 8 | 1 | 0 | 0 | 0 | 0 | 0  |
| 9 | 1 | 0 | 0 | 1 | 0 | 0  |
| 10 | 1 | 0 | 1 | 0 | 0 | 0  |
| 11 | 1 | 0 | 1 | 1 | 0 | 0  |
| 12 | 1 | 1 | 0 | 0 | 0 | 0  |
| 13 | 1 | 1 | 0 | 1 | 0 | 0  |
| 14 | 1 | 1 | 1 | 0 | 0 | 0  |
| 15 | 1 | 1 | 1 | 1 | 0 | 0  |

** <span dir="rtl">الأشكال القانونية</span> / Canonical Forms  **

- ** <span dir="rtl">الأشكال القانونية الأولى</span> / First Canonical Forms  **  
  - 
$$
 F1 = \overline{X}.\overline{Y}.\overline{Z}.\overline{D} + \overline{X}.\overline{Y}.\overline{Z}.D + \overline{X}.\overline{Y}.Z.D 
$$

  - 
$$
 F2 = \overline{X}.\overline{Y}.Z.\overline{D} + \overline{X}.Y.Z.\overline{D} + \overline{X}.Y.Z.D 
$$

- ** <span dir="rtl">الأشكال القانونية الثانية</span> / Second Canonical Forms  **  
  - 
$$
 F1 = (X+Y+\overline{Z}+D) . (X+\overline{Y}+Z+D) . (X+\overline{Y}+Z+\overline{D}) . (X+\overline{Y}+\overline{Z}+D) . (X+\overline{Y}+\overline{Z}+\overline{D}) . (\overline{X}+Y+Z+D) . (\overline{X}+Y+Z+\overline{D}) . (\overline{X}+Y+\overline{Z}+D) . (\overline{X}+Y+\overline{Z}+\overline{D}) . (\overline{X}+\overline{Y}+Z+D) . (\overline{X}+\overline{Y}+Z+\overline{D}) . (\overline{X}+\overline{Y}+\overline{Z}+D) . (\overline{X}+\overline{Y}+\overline{Z}+\overline{D}) 
$$

  - 
$$
 F2 = (X+Y+Z+D) . (X+Y+Z+\overline{D}) . (X+Y+\overline{Z}+\overline{D}) . (X+\overline{Y}+Z+D) . (X+\overline{Y}+Z+\overline{D}) . (\overline{X}+Y+Z+D) . (\overline{X}+Y+Z+\overline{D}) . (\overline{X}+Y+\overline{Z}+D) . (\overline{X}+Y+\overline{Z}+\overline{D}) . (\overline{X}+\overline{Y}+Z+D) . (\overline{X}+\overline{Y}+Z+\overline{D}) . (\overline{X}+\overline{Y}+\overline{Z}+D) . (\overline{X}+\overline{Y}+\overline{Z}+\overline{D}) 
$$

- ** <span dir="rtl">الأشكال القانونية الأولى</span> / First Canonical Forms  **  
  - 
$$
 F1 = ∑(0, 1, 3) 
$$

  - 
$$
 F2 = ∑(2, 6, 7) 
$$

- ** <span dir="rtl">الأشكال القانونية الثانية</span> / Second Canonical Forms  **  
  - 
$$
 F1 = ∏(2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) 
$$

  - 
$$
 F2 = ∏(0, 1, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15) 
$$

** <span dir="rtl">جدول كارنوف</span> / Karnaugh map  **

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">ZD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">XY</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 0, RMAX 0, CMIN 1, CMAX 2 -->
            <rect x="140" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 0, RMAX 0, CMIN 0, CMAX 1 -->
            <rect x="80" y="80"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products : 
$$
 F1 =  d.\overline{x}.\overline{y} + \overline{x}.\overline{y}.\overline{z}  
$$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums : 
$$
 F1 = (\overline{x}).(\overline{y}).(d+\overline{z}) 
$$

<svg width="340" height="340">
      <!-- Variable labels -->
      <text x="100" y="20" font-size="16" font-family="sans-serif">ZD</text>
      <text x="20" y="100" font-size="16" font-family="sans-serif" transform="rotate(-90,20,100)">XY</text>
      <!-- Column labels -->
        <text x="110.0" y="50" font-size="14" text-anchor="middle">00</text>
        <text x="170.0" y="50" font-size="14" text-anchor="middle">01</text>
        <text x="230.0" y="50" font-size="14" text-anchor="middle">11</text>
        <text x="290.0" y="50" font-size="14" text-anchor="middle">10</text>
      <!-- Row labels -->
        <text x="50" y="110.0" font-size="14" dominant-baseline="middle">00</text>
        <text x="50" y="170.0" font-size="14" dominant-baseline="middle">01</text>
        <text x="50" y="230.0" font-size="14" dominant-baseline="middle">11</text>
        <text x="50" y="290.0" font-size="14" dominant-baseline="middle">10</text>
      <!-- Cells -->
          <!-- rectangle -->
          <rect x="80" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="115.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="80" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="115.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="175.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="260" y="140" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="175.0"
                font-size="16" text-anchor="middle">1</text>
          <!-- rectangle -->
          <rect x="80" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="200" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="235.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="80" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="110.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="140" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="170.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="200" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="230.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
          <!-- rectangle -->
          <rect x="260" y="260" width="60" height="60"
                stroke="black" fill="white" />
          <!-- text -->
          <text x="290.0" y="295.0"
                font-size="16" text-anchor="middle">0</text>
      <!-- Groups (simple bounding boxes) -->
            <!-- RMIN 1, RMAX 1, CMIN 2, CMAX 3 -->
            <rect x="200" y="140"
                  width="120" height="60"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="red" stroke-width="2"/>
            <!-- RMIN 0, RMAX 1, CMIN 3, CMAX 3 -->
            <rect x="260" y="80"
                  width="60" height="120"
                  rx="14" ry="14"
                  fill="none" fill-opacity="0.25" stroke="green" stroke-width="2"/>
     </svg>

-  <span dir="rtl">مجموع الجداءات المبسط</span> / Simplified Sum of products : 
$$
 F2 =  \overline{x}.y.z + \overline{d}.\overline{x}.z  
$$

-  <span dir="rtl">جداء المجاميع المبسط</span> / Simplified product of sums : 
$$
 F2 = (z).(\overline{x}).(\overline{d}+y) 
$$

** <span dir="rtl">المخطط المنطقي</span> / Logic diagram  **

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="350" viewBox="0 0 900 180" preserveAspectRatio="xMinYMin meet">
  <style>
    .wire { stroke: #222; stroke-width: 2; fill: none; }
    .gate { stroke: #222; stroke-width: 2; fill: white; }
    .not-bubble { stroke: #222; stroke-width: 2; fill: white; }
    .label { font-family: "DejaVu Sans", "Arial", sans-serif; font-size:14px; text-anchor: middle; }
    .var-name { font-weight: bold; }
  </style>
 <!-- Define NOT gate as reusable symbol -->
  <defs>
    <g id="not-gate">
      <!-- Triangle -->
      <polygon points="0,0 20,10 0,20" stroke="black" fill="none"/>
      <!-- Circle (inversion bubble) -->
      <circle cx="25" cy="10" r="5" stroke="black" fill="none"/>
      <!-- Input wire -->
      <line x1="-5" y1="10" x2="0" y2="10" stroke="black"/>
      <!-- Output wire -->
      <line x1="30" y1="10" x2="35" y2="10" stroke="red"/>
    </g>
 <!-- Define NOR gate as reusable symbol -->
    <g id="nor-gate">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
 <!-- Define OR gate as reusable symbol  NO wires-->
    <g id="or-gate0">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
 <!-- Define OR gate as reusable symbol -->
    <g id="or-gate4">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate3">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="or-gate2">
      <!-- OR gate body (shorter) -->
      <path d="M0,0
               Q8,20 0,40
               Q20,40 40,20
               Q20,0 0,0
               Z"
            stroke="black" fill="white"/>
      <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Output wire -->
      <line x1="40" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
      <g id="or-gate1">
        <!-- replacement Output wire -->
        <use href="#and-gate1" x="0" y="0"/>
      </g>
<!-- Define BIG OR gate as reusable symbol -->
    <g id="big-or-gate3">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
      <path d="M0,0
               Q40,60 0,125
               Q100,125 125,60
               Q100,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="250" y1="120" x2="300" y2="120" stroke="red"/>
    </g>
        <g id="big-or-gate2">
      <!-- OR gate body (shorter) -->
      <!-- OR gate body -->
     <path d="M0,0
               Q40,40 0,80
               Q80,80 80,40
               Q80,0 0,0"
            stroke="black" fill="none"/>
      <!-- Output wire -->
      <line x1="80" y1="40" x2="100" y2="40" stroke="red"/>
    </g>
    <!-- Define AND gate as reusable symbol -->
      <g id="and-gate4">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate3">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate2">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="none"/>
        <!-- Input wires -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <g id="and-gate1">
        <!-- replacement Output wire -->
        <line x1="-20" y1="20" x2="80" y2="20" stroke="orange"/>
      </g>
      <g id="and-gate0">
        <!-- Left side (flat) -->
        <line x1="0" y1="0" x2="0" y2="40" stroke="black"/>
        <!-- Top arc -->
        <path d="M0,0 H20 A20,20 0 0,1 20,40 H0" stroke="black" fill="white"/>
        <!-- Input wires -->
        <!-- Output wire -->
        <line x1="40" y1="20" x2="80" y2="20" stroke="red"/>
      </g>
      <!-- NAND Gate -->
    <g id="nand-gate0">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
      <line x1="-20" y1="10" x2="0" y2="10" stroke="black"/>
      <line x1="-20" y1="30" x2="0" y2="30" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate4">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate3">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate2">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate1">
        <use href="#and-gate1" x="0" y="0"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate0">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <!-- NOR Gate -->
    <g id="nor-gate4">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate3">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
        <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate2">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="70" y2="20" stroke="red"/>
    </g>
    <g id="nor-gate1">
      <use href="#and-gate1" x="0" y="0"/>
    </g>
    <g id="nor-gate-not">
      <!-- OR body -->
      <path d="M0,0
               Q8,20 0,40
               Q25,40 45,20
               Q25,0 0,0 Z"
            stroke="black" fill="none"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="50" cy="20" r="4" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="54" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    <g id="nand-gate-not">
      <!-- AND body -->
      <path d="M0,0 H20 A20,20 0 0,1 20,40 H0 Z"
            stroke="black" fill="white"/>
      <!-- Inputs -->
        <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
        <line x1="-20" y1="35" x2="0" y2="35" stroke="black"/>
      <!-- Inversion bubble -->
      <circle cx="40" cy="20" r="5" stroke="black" fill="white"/>
      <!-- Output -->
      <line x1="45" y1="20" x2="60" y2="20" stroke="red"/>
    </g>
    </defs>
   <!-- Draw variables A, B, C, D with NOT gates -->
  <g transform="translate(20,30)">
    <!-- X -->
    <text x="0" y="-5" font-family="serif" font-size="20">X</text>
    <line x1="10" y1="0" x2="10" y2="300" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="300" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(70,30)">
    <!-- Y -->
    <text x="0" y="-5" font-family="serif" font-size="20">Y</text>
    <line x1="10" y1="0" x2="10" y2="300" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="300" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(120,30)">
    <!-- Z -->
    <text x="0" y="-5" font-family="serif" font-size="20">Z</text>
    <line x1="10" y1="0" x2="10" y2="300" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="300" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
  <g transform="translate(170,30)">
    <!-- D -->
    <text x="0" y="-5" font-family="serif" font-size="20">D</text>
    <line x1="10" y1="0" x2="10" y2="300" stroke="black"/>
    <line x1="35.0" y1="10" x2="35.0" y2="300" stroke="red"/>
        <g transform="translate(15,5)">       <g>
          <polygon points="0,0 15,5.0 0,10" stroke="black" fill="white"/>
          <line x1="-5" y1="5.0" x2="0" y2="5.0" stroke="black"/>
          <circle cx="20" cy="5.0" r="4" stroke="black" fill="white"/>
          <line x1="25" y1="5.0" x2="25" y2="5.0" stroke="red"/>
      </g></g>
  </g>
      <!-- Draw terms of fucntion -->
      <g transform="translate(250,100)">
        <!-- Draw the term {'default': "x'.y'.z'", 'formatted': "x'.y'.z'"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F1  :  x'.y'.z'</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-145" y1="15" x2="0" y2="15" stroke="red"/>
                <line x1="-95" y1="25" x2="0" y2="25" stroke="red"/>
      </g>
      <g transform="translate(250,150)">
        <!-- Draw the term {'default': "d.x'.y'", 'formatted': "d.x'.y'"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F1  :  d.x'.y'</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-145" y1="15" x2="0" y2="15" stroke="red"/>
                <line x1="-70" y1="25" x2="0" y2="25" stroke="black"/>
      </g>
        <g transform="translate(450,125.0)">
        <!-- F1 -->
        <text x="60" y="15" font-family="serif" font-size="10">F1</text>
          <g id="wires">
        <!-- vertical wire -->
        <line x1="-5" y1="5.0" x2="-5" y2="-5.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="5.0" x2="20" y2="5.0" stroke="red"/>
        <!-- vertical wire -->
        <line x1="-5" y1="35.0" x2="-5" y2="45.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="35.0" x2="20" y2="35.0" stroke="red"/>
  </g>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0
               Q8.0,20.0 0,40
               Q24.0,40 40,20.0
               Q24.0,0 0,0"
            stroke="black" fill="white"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        </g>
      <!-- Draw terms of fucntion -->
      <g transform="translate(250,200)">
        <!-- Draw the term {'default': "d'.x'.z", 'formatted': "d'.x'.z"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F2  :  d'.x'.z</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-120" y1="15" x2="0" y2="15" stroke="black"/>
                <line x1="-45" y1="25" x2="0" y2="25" stroke="red"/>
      </g>
      <g transform="translate(250,250)">
        <!-- Draw the term {'default': "x'.y.z", 'formatted': "x'.y.z"} -->
        <text x="60" y="15" font-family="serif" font-size="10">F2  :  x'.y.z</text>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0 H20.0 A20.0,20.0 0 0 1 20.0,40 H0 Z"
            stroke="black" fill="white"/>
                      <line x1="-20" y1="5" x2="0" y2="5" stroke="black"/>
            <line x1="-20" y1="15" x2="0" y2="15" stroke="black"/>
            <line x1="-20" y1="25" x2="0" y2="25" stroke="black"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        <!-- Extend output line -->
                <line x1="80" y1="20" x2="195" y2="20" stroke="blue"/>
      <!-- Draw vars of term  -->
                <line x1="-195" y1="5" x2="0" y2="5" stroke="red"/>
                <line x1="-170" y1="15" x2="0" y2="15" stroke="black"/>
                <line x1="-120" y1="25" x2="0" y2="25" stroke="black"/>
      </g>
        <g transform="translate(450,225.0)">
        <!-- F2 -->
        <text x="60" y="15" font-family="serif" font-size="10">F2</text>
          <g id="wires">
        <!-- vertical wire -->
        <line x1="-5" y1="5.0" x2="-5" y2="-5.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="5.0" x2="20" y2="5.0" stroke="red"/>
        <!-- vertical wire -->
        <line x1="-5" y1="35.0" x2="-5" y2="45.0" stroke="green"/>
        <!-- horizontal wire -->
        <line x1="-5" y1="35.0" x2="20" y2="35.0" stroke="red"/>
  </g>
        <g transform="translate(15,0)">       <g>
             <path d="M0,0
               Q8.0,20.0 0,40
               Q24.0,40 40,20.0
               Q24.0,0 0,0"
            stroke="black" fill="white"/>
            <line x1="40" y1="20.0" x2="70" y2="20.0" stroke="red"/>
      </g></g>
        </g>
</svg>

####  Q1

 <span dir="rtl">أكمل المخطط الزمني الآتي:</span> / Complete the following timing diagram:   

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="840" height="480">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="30.0" y1="0"
            x2="30.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="90.0" y1="0"
            x2="90.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="150.0" y1="0"
            x2="150.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="210.0" y1="0"
            x2="210.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="270.0" y1="0"
            x2="270.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="330.0" y1="0"
            x2="330.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="390.0" y1="0"
            x2="390.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="450.0" y1="0"
            x2="450.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="510.0" y1="0"
            x2="510.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="570.0" y1="0"
            x2="570.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="630.0" y1="0"
            x2="630.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="690.0" y1="0"
            x2="690.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="750.0" y1="0"
            x2="750.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="donwarraw" transform="translate(0.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(60.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(120.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(180.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(240.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(300.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(360.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(420.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(480.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(540.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(600.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(660.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(720.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      J
    </text>
  <path d="
    M 0 50
        h 60
          v -50
        h 60
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      K
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 320)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q'
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

--------

##  Correction

####  Q1

 <span dir="rtl">أكمل المخطط الزمني الآتي:</span> / Complete the following timing diagram:   

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="840" height="480">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="30.0" y1="0"
            x2="30.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="90.0" y1="0"
            x2="90.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="150.0" y1="0"
            x2="150.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="210.0" y1="0"
            x2="210.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="270.0" y1="0"
            x2="270.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="330.0" y1="0"
            x2="330.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="390.0" y1="0"
            x2="390.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="450.0" y1="0"
            x2="450.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="510.0" y1="0"
            x2="510.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="570.0" y1="0"
            x2="570.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="630.0" y1="0"
            x2="630.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="690.0" y1="0"
            x2="690.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="750.0" y1="0"
            x2="750.0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="donwarraw" transform="translate(0.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(60.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(120.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(180.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(240.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(300.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(360.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(420.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(480.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(540.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(600.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(660.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(720.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      J
    </text>
  <path d="
    M 0 50
        h 60
          v -50
        h 60
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      K
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q
    </text>
  <path d="
    M 0 50
        h 0
        h 0
          v -50
        h 120
          v 50
        h 120
          v -50
        h 120
        h 120
        h 120
        h 120
          v 50
        h 120
          v -50
        h 120
        h 120
          v 50
        h 120
        h 120
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 320)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q'
    </text>
  <path d="
    M 0 50
        h 0
        h 0
        h 120
          v -50
        h 120
          v 50
        h 120
        h 120
        h 120
        h 120
          v -50
        h 120
          v 50
        h 120
        h 120
          v -50
        h 120
        h 120
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

####  Q1

# Flip

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  **D**.

<span dir="rtl" lang="ar">
اذكر جدول الحقيقة للقلاب <span dir="ltr">D</span>.
</span>

<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .overline {
      text-decoration: overline;
      /* optional tweaks */
      text-decoration-color: red;          /* color of the line */
      text-decoration-thickness: 2px;      /* line thickness (supported in modern browsers) */
      /* offset is not controllable for overline; see method #2 for precise control */
    }
  </style>
<defs>
<g id="jkbody">
     <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="-10" y1="40" x2="0" y2="40" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Outputs -->
    <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
    <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
    <!-- Output lines -->
    <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Bubble for Q' -->
    <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <!-- Triangle for CLK -->
    <polygon points="5,40 0,35 0,45" fill="none" stroke="#000" stroke-width="1"/>
</g>
<g id="JK">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">J</text>
    <text x="5" y="75" font-family="Arial" font-size="12">K</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
    <g id="RST">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">R</text>
    <text x="5" y="75" font-family="Arial" font-size="12">S</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
<g id="JKA">
        <!-- Bubble for cl -->
    <circle cx="25" cy="-2.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="-5" x2="25" y2="-10" stroke="#000" stroke-width="1"/>
    <text x="20" y="10" font-family="Arial" class="overline" font-size="8">cl</text>
    <!-- Bubble for pr -->
    <circle cx="25" cy="82.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="85" x2="25" y2="90" stroke="#000" stroke-width="1"/>
    <text x="20" y="75" font-family="Arial" class="overline" font-size="8">pr</text>
    <use href="#JK" x="0" y="0"/>
</g>
<g id="D">
      <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Inputs -->
      <text x="5" y="15" font-family="Arial" font-size="12">D</text>
      <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="-10" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Outputs -->
      <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
      <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
      <!-- Output lines -->
      <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Bubble for Q' -->
      <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Triangle for CLK -->
      <polygon points="5,70 0,65 0,75" fill="none" stroke="#000" stroke-width="1"/>
  </g>
<!--  Define a jk flip from as module register  -->
    <g id="jkreg">
<!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs to pr/cl  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
<line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- vertical -->
<line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<use href="#jkflip" x="20" y="20"/>
</g>
<!--  Define a register  -->
<g id="reg">
<use href="#clocklink" x="5" y="40"/>
<use href="#jkreg" x="20" y="20"/>
<use href="#link" x="105" y="40"/>
<use href="#jkreg" x="140" y="20"/>
<use href="#link" x="225" y="40"/>
<use href="#jkreg" x="260" y="20"/>
<use href="#link" x="345" y="40"/>
<use href="#jkreg" x="380" y="20"/>
</g>
<!--  Define a link  -->
<g id="link">
<!-- Q' to clock -->
<!-- vertical -->
<line x1="0" y1="40" x2="45" y2="40" stroke="#f00" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="70" stroke="#0f0" stroke-width="1"/>
</g>
<g id="clocklink">
<!-- Q' to clock -->
<text x="-20" y="120" font-family="Arial" font-size="12">Clock</text>
<!-- vertical -->
<line x1="0" y1="40" x2="25" y2="40" stroke="#0ff" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="120" stroke="#00f" stroke-width="1"/>
</g>
<g id="varlink">
    <!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
</g>
</defs>
  <use href="#D" x="40" y="20"/>
</svg>

 <span dir="rtl">أكمل المخطط الزمني حسب القلاب المعطى</span> / Complete the following timing diagram, according to the given flip-flop. 

<div class="timing-diagram">

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="0" y1="0"
            x2="0" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="60" y1="0"
            x2="60" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="120" y1="0"
            x2="120" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="180" y1="0"
            x2="180" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="240" y1="0"
            x2="240" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="300" y1="0"
            x2="300" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="360" y1="0"
            x2="360" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="420" y1="0"
            x2="420" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="480" y1="0"
            x2="480" y2="640"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="uparraw" transform="translate(-30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(90,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(150,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(210,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(270,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(330,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(390,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(450,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      D
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q
    </text>
  <path d="
    M 0 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>
</div>

--------

##  Correction

####  Q1

# Flip

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  **D**.

<span dir="rtl" lang="ar">
اذكر جدول الحقيقة للقلاب <span dir="ltr">D</span>.
</span>

### <span dir="rtl">جدول حقيقة القلاب D</span> / Truth table of D flipflop

| Ck | D |  | Qₜ   |
|----|-------------------|-------------------|------|
| 0  | X                 | X                 | Qₜ₋₁ |
| ↑ | 0 | 0 | 0 |
| ↑ | 0 | 1 | 1 |
| ↑ | 1 | 0 |  |
| ↑ | 1 | 1 |  |

<div class="timing-diagram">

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="0" y1="0"
            x2="0" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="60" y1="0"
            x2="60" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="120" y1="0"
            x2="120" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="180" y1="0"
            x2="180" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="240" y1="0"
            x2="240" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="300" y1="0"
            x2="300" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="360" y1="0"
            x2="360" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="420" y1="0"
            x2="420" y2="640"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="480" y1="0"
            x2="480" y2="640"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="uparraw" transform="translate(-30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(90,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(150,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(210,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(270,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(330,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(390,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(450,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      D
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q
    </text>
  <path d="
    M 0 50
        h 60
        h 120
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="480" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

</div>

####  Q1

##  <span dir="rtl">عداد</span> / Counter

 <span dir="rtl">إليك التركيب الآتي</span> / Let have the following setup   

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <style>
    .overline {
      text-decoration: overline;
      /* optional tweaks */
      text-decoration-color: red;          /* color of the line */
      text-decoration-thickness: 2px;      /* line thickness (supported in modern browsers) */
      /* offset is not controllable for overline; see method #2 for precise control */
    }
  </style>
<defs>
<g id="jkbody">
     <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="-10" y1="40" x2="0" y2="40" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Outputs -->
    <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
    <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
    <!-- Output lines -->
    <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Bubble for Q' -->
    <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <!-- Triangle for CLK -->
    <polygon points="5,40 0,35 0,45" fill="none" stroke="#000" stroke-width="1"/>
</g>
<g id="JK">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">J</text>
    <text x="5" y="75" font-family="Arial" font-size="12">K</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
    <g id="RST">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">R</text>
    <text x="5" y="75" font-family="Arial" font-size="12">S</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
<g id="JKA">
        <!-- Bubble for cl -->
    <circle cx="25" cy="-2.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="-5" x2="25" y2="-10" stroke="#000" stroke-width="1"/>
    <text x="20" y="10" font-family="Arial" class="overline" font-size="8">cl</text>
    <!-- Bubble for pr -->
    <circle cx="25" cy="82.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="85" x2="25" y2="90" stroke="#000" stroke-width="1"/>
    <text x="20" y="75" font-family="Arial" class="overline" font-size="8">pr</text>
    <use href="#JK" x="0" y="0"/>
</g>
<g id="D">
      <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Inputs -->
      <text x="5" y="15" font-family="Arial" font-size="12">D</text>
      <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="-10" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Outputs -->
      <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
      <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
      <!-- Output lines -->
      <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Bubble for Q' -->
      <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Triangle for CLK -->
      <polygon points="5,70 0,65 0,75" fill="none" stroke="#000" stroke-width="1"/>
  </g>
<!--  Define a jk flip from as module register  -->
    <g id="jkreg">
<!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs to pr/cl  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
<line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- vertical -->
<line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<use href="#jkflip" x="20" y="20"/>
</g>
<!--  Define a register  -->
<g id="reg">
<use href="#clocklink" x="5" y="40"/>
<use href="#jkreg" x="20" y="20"/>
<use href="#link" x="105" y="40"/>
<use href="#jkreg" x="140" y="20"/>
<use href="#link" x="225" y="40"/>
<use href="#jkreg" x="260" y="20"/>
<use href="#link" x="345" y="40"/>
<use href="#jkreg" x="380" y="20"/>
</g>
<!--  Define a link  -->
<g id="link">
<!-- Q' to clock -->
<!-- vertical -->
<line x1="0" y1="40" x2="45" y2="40" stroke="#f00" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="70" stroke="#0f0" stroke-width="1"/>
</g>
<g id="clocklink">
<!-- Q' to clock -->
<text x="-20" y="120" font-family="Arial" font-size="12">Clock</text>
<!-- vertical -->
<line x1="0" y1="40" x2="25" y2="40" stroke="#0ff" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="120" stroke="#00f" stroke-width="1"/>
</g>
<g id="varlink">
    <!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
</g>
</defs>
<g transform="translate(25,20)">
    <!--\draw (-20,140) node[circle, fill, inner sep=1pt] {};-->
<!--\draw (-20,140) node[left] (Ck)  {$Ck$};-->
<g transform="translate(-20,140)">
<text x="0" y="-5" font-family="Arial" font-size="12">Ck</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Ck(-20,140)[]</text>-->
<!--   clock line -->
<line x1="10" y1="0" x2="15" y2="0" stroke="#000" stroke-width="1"/>
</g>
        <g id="countmodule0" transform="translate(0,20)">
        <use href="#JKA" x="20" y="20"/>
<g transform="translate(5,0)">
<line x1="-10" y1="60" x2="15" y2="60" stroke="#0ff" stroke-width="1"/>
<line x1="-10" y1="60" x2="-10" y2="120" stroke="#00f" stroke-width="1"/>
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(-5,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Vcc0</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Vcc0(-5,0)[0]</text>-->
</g>
        <g transform="translate(0,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
    <line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
 <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Warning not supported pin 'pin 1'</text>-->
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
</g>
</g>  <!-- end counter module -->
        <g id="countmodule1" transform="translate(100,20)">
        <use href="#JKA" x="20" y="20"/>
        <!-- Register flip Output  var placement  -->
<g transform="translate(-5,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Vcc1</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Vcc1(-5,0)[0]</text>-->
</g>
        <g transform="translate(0,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
    <line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
 <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Warning not supported pin 'pin 1'</text>-->
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
</g>
             <g transform="translate(0,0)">
        <line x1="-15" y1="30" x2="10" y2="60" stroke="#0f0" stroke-width="1"/>
</g>
</g>  <!-- end counter module -->
        <g id="countmodule2" transform="translate(200,20)">
        <use href="#JKA" x="20" y="20"/>
        <!-- Register flip Output  var placement  -->
<g transform="translate(-5,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Vcc2</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Vcc2(-5,0)[0]</text>-->
</g>
        <g transform="translate(0,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
    <line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<!-- Register flip Output line -->
 <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Warning not supported pin 'pin 1'</text>-->
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
</g>
             <g transform="translate(0,0)">
        <line x1="-15" y1="30" x2="10" y2="60" stroke="#0f0" stroke-width="1"/>
</g>
</g>  <!-- end counter module -->
</g>  <!-- end counter group-->
</svg>

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  D.  

Compl<span dir="rtl">أكمل المخطط الزمني حسب التركيب المعطى.</span> / Complete the following timing diagram, according to the given setup. 

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="3120" height="400">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="30.0" y1="0"
            x2="30.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="90.0" y1="0"
            x2="90.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="150.0" y1="0"
            x2="150.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="210.0" y1="0"
            x2="210.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="270.0" y1="0"
            x2="270.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="330.0" y1="0"
            x2="330.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="390.0" y1="0"
            x2="390.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="450.0" y1="0"
            x2="450.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="510.0" y1="0"
            x2="510.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="570.0" y1="0"
            x2="570.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="630.0" y1="0"
            x2="630.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="690.0" y1="0"
            x2="690.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="750.0" y1="0"
            x2="750.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="810.0" y1="0"
            x2="810.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="870.0" y1="0"
            x2="870.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="930.0" y1="0"
            x2="930.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="990.0" y1="0"
            x2="990.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1050.0" y1="0"
            x2="1050.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1110.0" y1="0"
            x2="1110.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1170.0" y1="0"
            x2="1170.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1230.0" y1="0"
            x2="1230.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1290.0" y1="0"
            x2="1290.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1350.0" y1="0"
            x2="1350.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1410.0" y1="0"
            x2="1410.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1470.0" y1="0"
            x2="1470.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1530.0" y1="0"
            x2="1530.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1590.0" y1="0"
            x2="1590.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1650.0" y1="0"
            x2="1650.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1710.0" y1="0"
            x2="1710.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1770.0" y1="0"
            x2="1770.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1830.0" y1="0"
            x2="1830.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1890.0" y1="0"
            x2="1890.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1950.0" y1="0"
            x2="1950.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2010.0" y1="0"
            x2="2010.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2070.0" y1="0"
            x2="2070.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2130.0" y1="0"
            x2="2130.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2190.0" y1="0"
            x2="2190.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2250.0" y1="0"
            x2="2250.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2310.0" y1="0"
            x2="2310.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2370.0" y1="0"
            x2="2370.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2430.0" y1="0"
            x2="2430.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2490.0" y1="0"
            x2="2490.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2550.0" y1="0"
            x2="2550.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2610.0" y1="0"
            x2="2610.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2670.0" y1="0"
            x2="2670.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2730.0" y1="0"
            x2="2730.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2790.0" y1="0"
            x2="2790.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2850.0" y1="0"
            x2="2850.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2910.0" y1="0"
            x2="2910.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2970.0" y1="0"
            x2="2970.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="3030.0" y1="0"
            x2="3030.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="donwarraw" transform="translate(0.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(60.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(120.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(180.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(240.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(300.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(360.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(420.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(480.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(540.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(600.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(660.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(720.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(780.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(840.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(900.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(960.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1020.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1080.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1140.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1200.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1260.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1320.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1380.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1440.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1500.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1560.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1620.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1680.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1740.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1800.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1860.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1920.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1980.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2040.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2100.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2160.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2220.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2280.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2340.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2400.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2460.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2520.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2580.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2640.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2700.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2760.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2820.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2880.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2940.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(3000.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q0
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q1
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q2
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

--------

##  Correction

####  Q1

##  <span dir="rtl">عداد</span> / Counter

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  D.  

### <span dir="rtl">جدول حقيقة القلاب D</span> / Truth table of D flipflop

| Ck     | D | Qₜ   |
|--------|---|------|
| 0/1    | X | Qₜ₋₁ |
| ↑ | 0 | 0    |
| ↑ | 1 | 1    |

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="3120" height="400">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="30.0" y1="0"
            x2="30.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="90.0" y1="0"
            x2="90.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="150.0" y1="0"
            x2="150.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="210.0" y1="0"
            x2="210.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="270.0" y1="0"
            x2="270.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="330.0" y1="0"
            x2="330.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="390.0" y1="0"
            x2="390.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="450.0" y1="0"
            x2="450.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="510.0" y1="0"
            x2="510.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="570.0" y1="0"
            x2="570.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="630.0" y1="0"
            x2="630.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="690.0" y1="0"
            x2="690.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="750.0" y1="0"
            x2="750.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="810.0" y1="0"
            x2="810.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="870.0" y1="0"
            x2="870.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="930.0" y1="0"
            x2="930.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="990.0" y1="0"
            x2="990.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1050.0" y1="0"
            x2="1050.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1110.0" y1="0"
            x2="1110.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1170.0" y1="0"
            x2="1170.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1230.0" y1="0"
            x2="1230.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1290.0" y1="0"
            x2="1290.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1350.0" y1="0"
            x2="1350.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1410.0" y1="0"
            x2="1410.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1470.0" y1="0"
            x2="1470.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1530.0" y1="0"
            x2="1530.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1590.0" y1="0"
            x2="1590.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1650.0" y1="0"
            x2="1650.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1710.0" y1="0"
            x2="1710.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1770.0" y1="0"
            x2="1770.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1830.0" y1="0"
            x2="1830.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1890.0" y1="0"
            x2="1890.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="1950.0" y1="0"
            x2="1950.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2010.0" y1="0"
            x2="2010.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2070.0" y1="0"
            x2="2070.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2130.0" y1="0"
            x2="2130.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2190.0" y1="0"
            x2="2190.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2250.0" y1="0"
            x2="2250.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2310.0" y1="0"
            x2="2310.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2370.0" y1="0"
            x2="2370.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2430.0" y1="0"
            x2="2430.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2490.0" y1="0"
            x2="2490.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2550.0" y1="0"
            x2="2550.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2610.0" y1="0"
            x2="2610.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2670.0" y1="0"
            x2="2670.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2730.0" y1="0"
            x2="2730.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2790.0" y1="0"
            x2="2790.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2850.0" y1="0"
            x2="2850.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2910.0" y1="0"
            x2="2910.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="2970.0" y1="0"
            x2="2970.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="3030.0" y1="0"
            x2="3030.0" y2="4000"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="donwarraw" transform="translate(0.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(60.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(120.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(180.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(240.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(300.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(360.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(420.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(480.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(540.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(600.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(660.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(720.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(780.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(840.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(900.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(960.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1020.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1080.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1140.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1200.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1260.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1320.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1380.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1440.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1500.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1560.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1620.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1680.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1740.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1800.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1860.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1920.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(1980.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2040.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2100.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2160.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2220.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2280.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2340.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2400.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2460.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2520.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2580.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2640.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2700.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2760.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2820.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2880.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(2940.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
      <g id="donwarraw" transform="translate(3000.0,30)">
        <polygon points="25,10 30,20 35,10" fill="green"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q0
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 120
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q1
    </text>
  <path d="
    M 0 50
        h 60
        h 240
          v -50
        h 240
          v 50
        h 240
          v -50
        h 240
          v 50
        h 240
          v -50
        h 240
          v 50
        h 240
          v -50
        h 240
          v 50
        h 240
          v -50
        h 240
          v 50
        h 240
          v -50
        h 240
          v 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="3000" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q2
    </text>
  <path d="
    M 0 50
        h 60
        h 480
          v -50
        h 480
          v 50
        h 480
          v -50
        h 480
          v 50
        h 480
          v -50
        h 480
          v 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

####  Q1

## <span dir="rtl">سجل</span> / Register

 <span dir="rtl">إليك التركيب الآتي</span> / Let have the following setup   

<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
  <style>
    .overline {
      text-decoration: overline;
      /* optional tweaks */
      text-decoration-color: red;          /* color of the line */
      text-decoration-thickness: 2px;      /* line thickness (supported in modern browsers) */
      /* offset is not controllable for overline; see method #2 for precise control */
    }
  </style>
<defs>
<g id="jkbody">
     <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="-10" y1="40" x2="0" y2="40" stroke="#000" stroke-width="1"/>
    <line x1="-20" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Outputs -->
    <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
    <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
    <!-- Output lines -->
    <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
    <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
    <!-- Bubble for Q' -->
    <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <!-- Triangle for CLK -->
    <polygon points="5,40 0,35 0,45" fill="none" stroke="#000" stroke-width="1"/>
</g>
<g id="JK">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">J</text>
    <text x="5" y="75" font-family="Arial" font-size="12">K</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
    <g id="RST">
    <!-- Inputs -->
    <text x="5" y="15" font-family="Arial" font-size="12">R</text>
    <text x="5" y="75" font-family="Arial" font-size="12">S</text>
    <use href="#jkbody" x="0" y="0"/>
</g>
<g id="JKA">
        <!-- Bubble for cl -->
    <circle cx="25" cy="-2.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="-5" x2="25" y2="-10" stroke="#000" stroke-width="1"/>
    <text x="20" y="10" font-family="Arial" class="overline" font-size="8">cl</text>
    <!-- Bubble for pr -->
    <circle cx="25" cy="82.5" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
    <line x1="25" y1="85" x2="25" y2="90" stroke="#000" stroke-width="1"/>
    <text x="20" y="75" font-family="Arial" class="overline" font-size="8">pr</text>
    <use href="#JK" x="0" y="0"/>
</g>
<g id="D">
      <rect x="0" y="0" width="50" height="80" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Inputs -->
      <text x="5" y="15" font-family="Arial" font-size="12">D</text>
      <line x1="-20" y1="10" x2="0" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="-10" y1="70" x2="0" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Outputs -->
      <text x="35" y="15" font-family="Arial" font-size="12">Q</text>
      <text x="35" y="75" font-family="Arial" class="overline" font-size="12">Q</text>
      <!-- Output lines -->
      <line x1="50" y1="10" x2="65" y2="10" stroke="#000" stroke-width="1"/>
      <line x1="55" y1="70" x2="65" y2="70" stroke="#000" stroke-width="1"/>
      <!-- Bubble for Q' -->
      <circle cx="52.5" cy="70" r="2.5" fill="none" stroke="#000" stroke-width="1"/>
      <!-- Triangle for CLK -->
      <polygon points="5,70 0,65 0,75" fill="none" stroke="#000" stroke-width="1"/>
  </g>
<!--  Define a jk flip from as module register  -->
    <g id="jkreg">
<!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="90" stroke="#000" stroke-width="1"/>
<!-- Vcc inputs to pr/cl  -->
<text x="0" y="0" font-family="Arial" font-size="12">Vcc</text>
<line x1="0" y1="5" x2="0" y2="110" stroke="#000" stroke-width="1"/>
<line x1="0" y1="10" x2="45" y2="10" stroke="#000" stroke-width="1"/>
<!-- vertical -->
<line x1="0" y1="110" x2="45" y2="110" stroke="#000" stroke-width="1"/>
<use href="#jkflip" x="20" y="20"/>
</g>
<!--  Define a register  -->
<g id="reg">
<use href="#clocklink" x="5" y="40"/>
<use href="#jkreg" x="20" y="20"/>
<use href="#link" x="105" y="40"/>
<use href="#jkreg" x="140" y="20"/>
<use href="#link" x="225" y="40"/>
<use href="#jkreg" x="260" y="20"/>
<use href="#link" x="345" y="40"/>
<use href="#jkreg" x="380" y="20"/>
</g>
<!--  Define a link  -->
<g id="link">
<!-- Q' to clock -->
<!-- vertical -->
<line x1="0" y1="40" x2="45" y2="40" stroke="#f00" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="70" stroke="#0f0" stroke-width="1"/>
</g>
<g id="clocklink">
<!-- Q' to clock -->
<text x="-20" y="120" font-family="Arial" font-size="12">Clock</text>
<!-- vertical -->
<line x1="0" y1="40" x2="25" y2="40" stroke="#0ff" stroke-width="1"/>
<line x1="0" y1="40" x2="0" y2="120" stroke="#00f" stroke-width="1"/>
</g>
<g id="varlink">
    <!-- Register flip Output  -->
<text x="90" y="0" font-family="Arial" font-size="12">Q0</text>
<line x1="85" y1="5" x2="85" y2="30" stroke="#000" stroke-width="1"/>
</g>
</defs>
<g transform="translate(25,20)">
    <!--\draw (-20,140) node[circle, fill, inner sep=1pt] {};-->
<!--\draw (-20,140) node[left] (Ck)  {$Ck$};-->
<g transform="translate(-20,140)">
<text x="0" y="-5" font-family="Arial" font-size="12">Ck</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Ck(-20,140)[]</text>-->
<!--   clock line -->
<line x1="10" y1="0" x2="315" y2="0" stroke="#000" stroke-width="1"/>
</g>
        <g id="regmodule0" transform="translate(0,20)">
        <use href="#D" x="20" y="20"/>
<g transform="translate(5,0)">
<line x1="-10" y1="90" x2="15" y2="90" stroke="#0ff" stroke-width="1"/>
<line x1="-10" y1="90" x2="-10" y2="120" stroke="#00f" stroke-width="1"/>
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(80,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Q0</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Q0(80,0)[0]</text>-->
</g>
        <g transform="translate(85,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
</g>
         </g> <!-- end register module-->
        <g id="regmodule1" transform="translate(100,20)">
        <use href="#D" x="20" y="20"/>
<g transform="translate(5,0)">
<line x1="-10" y1="90" x2="15" y2="90" stroke="#0ff" stroke-width="1"/>
<line x1="-10" y1="90" x2="-10" y2="120" stroke="#00f" stroke-width="1"/>
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(80,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Q1</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Q1(80,0)[0]</text>-->
</g>
        <g transform="translate(85,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
</g>
            <g transform="translate(5,7.5)">
<!-- Register flip Output line -->
    <!--    link var Q1-->
    <line x1="80" y1="0" x2="-105" y2="0" stroke="#FCAF3E" stroke-width="1"/>
    <line x1="-105" y1="0" x2="-105" y2="22.5" stroke="#A40000" stroke-width="1"/>
    <!--<text x="0" y="-10" font-family="Arial" font-size="8">Link var  Q1(0,7.5)</text>-->
</g>
         </g> <!-- end register module-->
        <g id="regmodule2" transform="translate(200,20)">
        <use href="#D" x="20" y="20"/>
<g transform="translate(5,0)">
<line x1="-10" y1="90" x2="15" y2="90" stroke="#0ff" stroke-width="1"/>
<line x1="-10" y1="90" x2="-10" y2="120" stroke="#00f" stroke-width="1"/>
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(80,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Q2</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Q2(80,0)[0]</text>-->
</g>
        <g transform="translate(85,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
</g>
            <g transform="translate(5,10.0)">
<!-- Register flip Output line -->
    <!--    link var Q2-->
    <line x1="80" y1="0" x2="-105" y2="0" stroke="#FCAF3E" stroke-width="1"/>
    <line x1="-105" y1="0" x2="-105" y2="20.0" stroke="#A40000" stroke-width="1"/>
    <!--<text x="0" y="-10" font-family="Arial" font-size="8">Link var  Q2(0,10.0)</text>-->
</g>
         </g> <!-- end register module-->
        <g id="regmodule3" transform="translate(300,20)">
        <use href="#D" x="20" y="20"/>
<g transform="translate(5,0)">
<line x1="-10" y1="90" x2="15" y2="90" stroke="#0ff" stroke-width="1"/>
<line x1="-10" y1="90" x2="-10" y2="120" stroke="#00f" stroke-width="1"/>
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(-5,0)">
<text x="0" y="0" font-family="Arial" font-size="12">E</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">E(-5,0)[0]</text>-->
</g>
        <g transform="translate(0,0)">
<!-- Register flip Output line -->
 <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Warning not supported pin 'pin 1'</text>-->
</g>
        <!-- Register flip Output  var placement  -->
<g transform="translate(80,0)">
<text x="0" y="0" font-family="Arial" font-size="12">Q3</text>
<!--<text x="0" y="-10" font-family="Arial" font-size="8">Q3(80,0)[0]</text>-->
</g>
        <g transform="translate(85,0)">
<!-- Register flip Output line -->
    <line x1="0" y1="5" x2="0" y2="30" stroke="#000" stroke-width="1"/>
</g>
            <g transform="translate(5,12.5)">
<!-- Register flip Output line -->
    <!--    link var Q3-->
    <line x1="80" y1="0" x2="-105" y2="0" stroke="#FCAF3E" stroke-width="1"/>
    <line x1="-105" y1="0" x2="-105" y2="17.5" stroke="#A40000" stroke-width="1"/>
    <!--<text x="0" y="-10" font-family="Arial" font-size="8">Link var  Q3(0,12.5)</text>-->
</g>
         </g> <!-- end register module-->
 </g> <!-- end register group-->
</svg>

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  D.  

 <span dir="rtl">أكمل المخطط الزمني حسب التركيب المعطى.</span> / Complete the following timing diagram, according to the given setup.   

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="840" height="560">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="0" y1="0"
            x2="0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="60" y1="0"
            x2="60" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="120" y1="0"
            x2="120" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="180" y1="0"
            x2="180" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="240" y1="0"
            x2="240" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="300" y1="0"
            x2="300" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="360" y1="0"
            x2="360" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="420" y1="0"
            x2="420" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="480" y1="0"
            x2="480" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="540" y1="0"
            x2="540" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="600" y1="0"
            x2="600" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="660" y1="0"
            x2="660" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="720" y1="0"
            x2="720" y2="960"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="uparraw" transform="translate(-30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(90,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(150,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(210,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(270,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(330,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(390,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(450,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(510,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(570,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(630,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(690,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      E
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q0
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q1
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 320)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q2
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 400)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q3
    </text>
  <path d="
    M 0 50
        h 0
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

---

---

--------

##  Correction

####  Q1

## <span dir="rtl">سجل</span> / Register

---

 <span dir="rtl">اذكر جدول حقيقة القلاب</span> / Cite the truth table of flipflop  D.  

<div class="arabic">
اذكر جدول الحقيقة للقلاب <span class="lr">D</span>.
</div>

### <span dir="rtl">جدول حقيقة القلاب D</span> / Truth table of D flipflop

| Ck     | D | Qₜ   |
|--------|---|------|
| 0/1    | X | Qₜ₋₁ |
| ↑ | 0 | 0    |
| ↑ | 1 | 1    |

<div class="timing-diagram">
  <p class="title"><span dir="rtl">المخطط الزمني</span> / Timing diagram</p>
<svg xmlns="http://www.w3.org/2000/svg" width="840" height="880">
<g transform="translate(0,00)">
<g class="multi-signals" transform="translate(80,00)">
  <g class="guides">
      <!--initial guide line -->
      <line x1="0" y1="0"
            x2="0" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="60" y1="0"
            x2="60" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="120" y1="0"
            x2="120" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="180" y1="0"
            x2="180" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="240" y1="0"
            x2="240" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="300" y1="0"
            x2="300" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="360" y1="0"
            x2="360" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="420" y1="0"
            x2="420" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="480" y1="0"
            x2="480" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="540" y1="0"
            x2="540" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="600" y1="0"
            x2="600" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="660" y1="0"
            x2="660" y2="960"
            stroke="lightgray" stroke-width="1.0" />
      <line x1="720" y1="0"
            x2="720" y2="960"
            stroke="lightgray" stroke-width="1.0" />
  </g>
    <g class="clock-signal">
    <text x="-20" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      H
    </text>
<path d="
    M 0 50
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
        v -50
        h 30.0
        v 50
        h 30.0
  "
  fill="none"
  stroke="green"
  stroke-width="2" />
  <g class="guides">
      <!--font_edge -->
      <g id="uparraw" transform="translate(-30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(30,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(90,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(150,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(210,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(270,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(330,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(390,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(450,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(510,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(570,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(630,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
      <g id="uparraw" transform="translate(690,-10)">
        <polygon points="25,20 30,10 35,20" fill="black"/>
    </g>
  </g>
</g>
    <g transform="translate(0, 80)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      E
    </text>
  <path d="
    M 0 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 160)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q0
    </text>
  <path d="
    M 0 50
        h 60
        h 120
        h 120
        h 120
        h 120
        h 60
          v -50
        h 60
          v 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 240)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q1
    </text>
  <path d="
    M 0 50
        h 60
        h 120
        h 120
        h 120
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 320)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q2
    </text>
  <path d="
    M 0 50
        h 60
        h 120
        h 120
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 400)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q3
    </text>
  <path d="
    M 0 50
        h 60
        h 120
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
          v -50
        h 60
          v 50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 480)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q3'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 560)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q2'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 120
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
        h 60
          v 50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 640)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q1'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 120
        h 120
        h 60
          v 50
        h 60
          v -50
        h 60
          v 50
        h 60
          v -50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
    <g transform="translate(0, 720)">
  <g class="guides">
      <line x1="0" y1="50"
            x2="720" y2="50"
            stroke="lightgray" stroke-width="" />
  </g>
      <g class="signal">
    <text x="-10" y="37.5"
          font-family="Arial" font-size="16" text-anchor="end"
          dominant-baseline="middle">
      Q0'
    </text>
  <path d="
    M 0 50
          v -50
        h 60
        h 120
        h 120
        h 120
        h 120
        h 60
          v 50
        h 60
          v -50
        h 60
  "
  fill="none"
  stroke="blue"
  stroke-width="2" />
</g>
    </g>
</g>
  </g>
</svg>
</div>

---

