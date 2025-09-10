Represent under **IEEE-754 32 bits** standard the following number:  
<span dir="rtl">مثل العدد الآتي حسب المعيار IEEE-754 32 bits</span>  

{% if "fr" in languages %}
Représenter sous la norme **IEEE-754 32 bits** le nombre suivant:  
{% endif %}

**{{ number }}**

---

{% if RENDER_MODE == "answer" %}
**Final binary representation:** `{{ binary_repr|group4 }}`<sub>IEEE-754-32bits</sub>  

| Step                  | Value |
|------------------------|-------|
| Input                 | ({{ "%.4f"|format(abs_value) }})<sub>10</sub> = ({{ binary_repr|group4 }})<sub>2</sub> |
| Normalized form       | 1.{{ mantissa|group4 }} × 2<sup>{{ exponent }}</sup> |
| Sign bit              | {% if sign == 1 %}-{% else %}+{% endif %} ⇒ {{ sign }} |
| Exponent              | {{ exponent }} + 127 = {{ exponent_raw }} ⇒ ({{ exponent_bits|group4 }})<sub>2</sub> |
| Pseudo-mantissa       | {{ mantissa|group4 }} |
| Final representation  | {{ final_binary|group4 }} |
| Hexadecimal form      | ({{ hex|group4 }})<sub>16</sub> |

{% endif %}
