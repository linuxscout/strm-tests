{# =========================================================
   Shared Macro: Conversion Table (Markdown)
   ========================================================= #}
{% macro conversion_table(input_bits, output_bits, steps, mode="bin2gray") %}

{% if mode == "bin2gray" %}
**{{tr("Binary → Gray Conversion")}}**
{% else %}
**{{tr("Gray → Binary Conversion")}}**
{% endif %}

| {% if mode == "bin2gray" %}{{tr("Binary")}}{% else %}{{tr("Gray")}}{% endif %} |{% for b in input_bits %} {{ b }} |{% endfor %}

|---|{% for b in input_bits %}---|{% endfor %}

| {{tr("Arrows")}} |{% for i in range(input_bits|length) %}
{% if i == 0 %} ↓ |{% else %}{% if mode == "bin2gray" %} ↘ ⊕ ↓ |{% else %} ↗ ⊕ ↓ |{% endif %}{% endif %}
{% endfor %}
| {% if mode == "bin2gray" %}{{tr("Gray")}}{% else %}{{tr("Binary")}}{% endif %} |{% for o in output_bits %} **{{ o }}** |{% endfor %}

| {{tr("Steps")}} |{% for step in steps %} {{ step }} |{% endfor %}
{% endmacro %}


{# =========================================================
   Illustrate bit changes
   ========================================================= #}
{% macro illustrate_bit_change(x, x_next) %}
### {{tr("Binary Increment Illustration")}}

**x:** `{{ x|join }}` → **x+1:** `{{ x_next|join }}`  

| {{tr("Position")}} |{% for i in range(x|length) %} {{ i }} |{% endfor %}

|---|{% for i in range(x|length) %}---|{% endfor %}

| x |{% for bit in x %} {{ bit }} |{% endfor %}

| x+1 |{% for i in range(x|length) %}
{% if x[i] != x_next[i] %} **{{ x_next[i] }}** |{% else %} {{ x_next[i] }} |{% endif %}
{% endfor %}
*{{tr("Highlighted cell(s) = changed bit(s)")}}*  
{% endmacro %}


{% macro illustrate_gray_sequence(gray_codes, x_name="x") %}
### {{tr("Gray Code Sequence (Bit Changes)")}}

| {{tr("Step")}} |{% for b in range(gray_codes[0]|length) %} Bit {{ loop.index0 }} |{% endfor %}

|---|{% for b in range(gray_codes[0]|length) %}---|{% endfor %}

{% for i in range(gray_codes|length) %}
| {{ x_name }} + {{ i }} |{% for j in range(gray_codes[i]|length) %}
{% if i > 0 and gray_codes[i][j] != gray_codes[i-1][j] %} **{{ gray_codes[i][j] }}** |{% else %} {{ gray_codes[i][j] }} |{% endif %}
{% endfor %}

{% endfor %}


*{{tr("Highlighted cell shows the bit that flipped compared to the previous Gray code.")}}*  
{% endmacro %}


{# =========================================================
   Main Template: Binary <-> Gray Exercises
   ========================================================= #}
{% if RENDER_MODE == "question" %}

### {{tr("Convert the following number from Binary to Gray:")}}
 
`{{ number_bin|join }}`  

---

### {{tr("Convert the following number from Gray to Binary:")}}

`{{ number_gray|join }}`  

{% elif RENDER_MODE == "answer" %}

### {{tr("Binary → Gray Conversion")}}
{{ conversion_table(number_bin, number_gray, steps_bin2gray, mode="bin2gray") }}

### {{tr("Gray → Binary Conversion")}}
{{ conversion_table(number_gray, number_bin, steps_gray2bin, mode="gray2bin") }}

### {{tr("Illustration of Bit Change (Next Gray Code)")}}
{{ illustrate_bit_change(gray_sequence[0], gray_sequence[1]) }}

### {{tr("Gray Code Sequence")}}
{{ illustrate_gray_sequence(gray_sequence, "x") }}

{% endif %}
