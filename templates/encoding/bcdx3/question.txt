{# =========================================================
   BCD/Excess-3 → Decimal
   ========================================================= #}
{% macro bcdx3_dec(number, bin_digits, scheme="bcd", mode="encode") %}

{% if mode.lower() == "decode" %}
#### {{scheme|upper}} to Decimal
  {% set code2_digits = number|list %}
  {% set code1_digits = bin_digits %}
{% else %}
#### XDecimal to {{scheme|upper}}
  {% set code1_digits = number|list %}
  {% set code2_digits = bin_digits %}
{% endif %}

| {% for c1 in code1_digits %} {{ c1 }} |{% endfor %}

|{% for c1 in code1_digits %}---|{% endfor %}

| {% for c2 in code2_digits %} {{ c2 }} |{% endfor %}

{% endmacro %}


{# =========================================================
   Render result
   ========================================================= #}
{% macro render_bcd(result, scheme="bcd") %}
### {{scheme|upper}} Addition Explanation

Decimal calculation:  
`{{ result.a_dec }} + {{ result.b_dec }} = {{ result.total_dec }}`  

| Carry In |{% for c in result.carry_in %} {{ '1' if c or result.carry_out[loop.index0] }} |{% endfor %}

|----------|{% for c in result.carry_in %}---|{% endfor %}

| A (dec)  |{% for d in result.digits_a_dec %} {{ d }} |{% endfor %}

| B (dec)  |{% for d in result.digits_b_dec %} {{ d }} |{% endfor %}

| Final (dec) |{% for f in result.final_digits_dec %} {{ f }} |{% endfor %}


### Addition in {{scheme|upper}}

| Carry In |{% for c in result.carry_in %} {{ '1' if c }} |{% endfor %}

|----------|{% for c in result.carry_in %}---|{% endfor %}

| A (bin)  |{% for d in result.digits_a_bin %} {{ d }} |{% endfor %}

| B (bin)  |{% for d in result.digits_b_bin %} {{ d }} |{% endfor %}

{% if scheme.lower() == "bcd" %}
| Carry Out|{% for c in result.carry_out %} {{ '1' if c }} |{% endfor %}
{% endif %}
| Raw Sum  |{% for s in result.sums_bin %} {{ s }} |{% endfor %}

| Correction |{% for corr in result.corrections %}{% if scheme.lower() == "bcd" %} {% if corr %}+{{ corr|to_bin }}{% endif %} |{% else %} {{ '+11' if corr > 0 else '-11' }} |{% endif %}{% endfor %}

| Final (bin) |{% for f in result.final_digits_bin %} {{ f }} |{% endfor %}

| Final (dec) |{% for f in result.final_digits_dec %} {{ f }} |{% endfor %}

{% endmacro %}


{# =========================================================
   Main call
   ========================================================= #}
{% if RENDER_MODE == "question" %}
  {% if scheme in ("bcd", "both", "") %}
#### Encode the following numbers into BCD, then illustrate the addition in BCD:
- **A =** `{{ number }}`
- **B =** `{{ data_bcd.b_dec }}`
  {% endif %}

  {% if scheme in ("x3", "both","") %}
#### Encode the following numbers into Excess-3, then illustrate the addition in Excess-3:
- **N =** `{{ number }}`
- **B =** `{{ data_bcd.b_dec }}`
  {% endif %}

{% elif RENDER_MODE == "answer" %}

({{number}})<sub>10</sub> = ({{bcd}})<sub>bcd</sub>  
({{number}})<sub>10</sub> = ({{x3}})<sub>x3</sub>  

**Explanation:**  

{% if method in ("encode", "both", "")%}
{% if scheme in ("bcd", "both","") %}
Base 10 → BCD  

{{ bcdx3_dec(number, bcd_digits, "bcd","encode") }}
{% endif %}
{% if scheme in ("x3", "both","") %}
Base 10 → Excess-3  

{{ bcdx3_dec(number, x3_digits, "x3","encode") }}
{% endif %}
{% endif %}

{% if method in ("decode", "both", "")%}
{% if scheme in ("bcd", "both","") %}
BCD → Base 10  

{{ bcdx3_dec(number, bcd_digits, "bcd","decode") }}
{% endif %}
{% if scheme in ("x3", "both","") %}
Excess-3 → Base 10  

{{ bcdx3_dec(number, x3_digits, "x3","decode") }}
{% endif %}
{% endif %}

{{ render_bcd(data_bcd) }}

{{ render_bcd(data_x3, scheme="excess3") }}

{% if not data_bcd.test_ok %}
 **Warning:** Please check addition, there are errors.  
{{ data_bcd|pprint}}

{% endif %}
{% endif %}