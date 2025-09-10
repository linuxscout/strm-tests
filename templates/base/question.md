{% import "base/binmacros.html" as binmacro %}

{# =========================================================
   Macro: one manual vertical division step (keeps inline SVG)
   ========================================================= #}
{% macro division_step(dividend, divisor, quotient, remainder, x=0, y=0, cell_w=30, cell_h=30, font_size=16) %}
{% set char_size = 12 %}
    <g transform="translate({{x}},{{y}})" font-family="monospace" font-size="{{font_size}}">
      <line x1="{{ cell_w }}" y1="0" x2="{{ cell_w }}" y2="{{ cell_h*2 }}" stroke="black"/>
      <line x1="{{ cell_w }}" y1="{{ cell_h }}" x2="{{ cell_w+cell_w }}" y2="{{ cell_h }}" stroke="black"/>
      <text x="{{ cell_w-4 }}" y="{{ cell_h*0.75 }}" text-anchor="end">{{ dividend }}</text>
      <text x="{{ cell_w+4 }}" y="{{ cell_h*0.75 }}" text-anchor="start">{{ divisor }}</text>
      <text x="{{ cell_w+cell_w+4 }}" y="{{ cell_h*1.75 }}" text-anchor="end">{{ quotient }}</text>
      <text x="{{ cell_w/2 }}" y="{{ cell_h*1.75 }}" text-anchor="middle">{{ remainder }}</text>
    </g>
{% endmacro %}


{# =========================================================
   Macro: whole division process (Markdown-safe)
   ========================================================= #}
{% macro division_process(dividend, divisor, steps, cell_h=30) %}


<svg xmlns="http://www.w3.org/2000/svg"
     width="{{ (steps|length+1) * 20 * ((dividend|string)|length) + 50 }}"
     height="{{ (steps|length+1) * cell_h*1.2 + 50 }}">
  <g transform="translate(20,20)">
    <text x="0" y="{{cell_h*0.75}}">Dividend: {{ dividend }}</text>
    <text x="200" y="{{cell_h*0.75}}">Divisor: {{ divisor }}</text>
  </g>
  {% set div_width = 12*((dividend|string)|length) %}
  {% set cell_w = div_width %}
  {% set ns= namespace(y_offset = 80, x_offset=20) %}
  {% for s in steps %}
    {% set dividend_str = s.dividend if loop.first else "" %}
{{ division_step(dividend_str, divisor, s.quotient, s.remainder, ns.x_offset, ns.y_offset, cell_w, cell_h) }} {% set ns.y_offset = ns.y_offset + cell_h %}
    {% set ns.x_offset = ns.x_offset + cell_w*1.1 %}{% endfor %}
</svg>

{% endmacro %}


{% macro base_conversion_table(digits, base, number_label="") %}
**Table: base {{ base }} representation**

{% if number_label %}
_Number in base {{ base }}: `{{ number_label }}`_
{% endif %}



| {% for d in digits %}{{ base }}^{{ loop.revindex0 }} |{% endfor %}

| {% for d in digits %}---|{% endfor %}

| {% for d in digits %}{{ d.symbol }} |{% endfor %}


{% endmacro %}


{% macro base_sum_expression(digits, base) %}
**Base {{ base }} → 10 Expansion**

- `N = {% for d in digits %}{{ d.symbol }}·{{ base }}^{{ loop.revindex0 }}{% if not loop.last %}+{% endif %}{% endfor %}`
- `N = {% for d in digits %}{{ d.value }}·{{ base }}^{{ loop.revindex0 }}{% if not loop.last %}+{% endif %}{% endfor %}`
- `N = {% set ns=namespace(total=0) %}{% for d in digits %}{% set product=d.value*(base**loop.revindex0) %}{% set ns.total=ns.total+product %}{{ product }}{% if not loop.last %}+{% endif %}{% endfor %}`
- `N = {{ ns.total }}`
{% endmacro %}


Convert the following numbers  
<span dir="rtl">أنجز التحويلات الآتية</span>  

{% if RENDER_MODE == "question" %}
`({{ number|group4 }})_{{ in_base }}` = `........`_{{ out_base }}
{% elif RENDER_MODE == "answer" %}
`({{ number|group4 }})_{{ in_base }}` = `({{ output|group4 }})_{{ out_base }}`
{% endif %}


{% if binary_mode %}
{{ binmacro.base_convert_table(number, in_base, out_base) }}
{% endif %}

{% if steps_to10 and steps_from10 %}
### Convert from base {{ in_base }} to {{ out_base }}
1. Convert from base {{ in_base }} to base 10  
2. Convert from base 10 to base {{ out_base }}
{% endif %}


{% if steps_to10 %}
### Convert from base {{ in_base }} to base 10

{{ base_conversion_table(steps_to10, in_base, number_label) }}

{{ base_sum_expression(steps_to10, in_base) }}

**Result:** {{ output }}
{% endif %}


{% if steps_from10 %}
### Convert from base 10 to base {{ out_base }}

<div>
{{ division_process(number_tmp if number_tmp else number, out_base, steps_from10, cell_h=30)| | normalize_newlines  }}
</div>

Result (bottom→top remainders):  
`({{ output }})_{{ out_base }}`
{% endif %}


{% if debug %}
{{ binmacro.bin2hex_table("101110101101") }}
{{ binmacro.bin2oct_table("101110101101") }}
{{ binmacro.hex2bin_table("BAD") }}
{{ binmacro.oct2bin_table("5725") }}
{{ binmacro.hex2oct_table("62F") }}
{{ binmacro.oct2hex_table("745") }}
{{ binmacro.base_convert_table("1A3", 16, 8) }}
{{ binmacro.base_convert_table("745", 8, 2) }}
{{ binmacro.base_convert_table("1011101", 2, 16) }}
{% endif %}
