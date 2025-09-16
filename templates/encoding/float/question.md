<p>
{{tr("Represent under IEEE-754 32 bits standard the following number:")}}


**{{ number }}**

---

{% if RENDER_MODE == "answer" %}
**{{tr("Final binary representation")}}:** `{{ binary_repr|group4 }}`<sub>IEEE-754-32bits</sub>  


| {{tr("Step")}}                   | {{tr("Value")}}  |
|------------------------|-------|
| {{tr("Input")}}                | ({{ "%.4f"|format(abs_value) }})<sub>10</sub> = ({{ binary_repr|group4 }})<sub>2</sub> |
| {{tr("Normalized form")}}       | 1.{{ mantissa|group4 }} × 2<sup>{{ exponent }}</sup> |
| {{tr("Sign bit")}}              | {% if sign == 1 %}-{% else %}+{% endif %} ⇒ {{ sign }} |
| {{tr("Exponent")}}              | {{ exponent }} + 127 = {{ exponent_raw }} ⇒ ({{ exponent_bits|group4 }})<sub>2</sub> |
| {{tr("Pseudo-mantissa")}}       | {{ mantissa|group4 }} |
| {{tr("Final representation")}}  | {{ final_binary|group4 }} |
| {{tr("Hexadecimal form")}}      | ({{ hex|group4 }})<sub>16</sub> |

{% endif %}
