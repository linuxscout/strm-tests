{% set debug = False %}
{% import "sequential/macros/flipmacros.html" as flpmacro%}
{% import "sequential/macros/flipmacros.md" as flpmacromd%}
{% import "sequential/macros/timingmacros.html" as tmmacro%}


{# -------------------------
draw_flip
----------------------------#}
{%macro draw_flip(flip_type) %}
<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
  {{ flpmacro.define_standard_flips() }}
  {{ flpmacro.place_flip(id=flip_type, name="f1", xpos=20, ypos=20)}}
</svg>
{%endmacro%}

{# -------------------------
draw_flip customized
----------------------------#}

{%macro draw_custom_flip(flip_data) %}
<svg width="1200" height="1200" xmlns="http://www.w3.org/2000/svg">
  {{ flpmacro.define_costum_flip(id=flip_data.type, inputs=flip_data.inputs)|normalize_newlines }}
  {{ flpmacro.place_flip(id=flip_data.type, name="f1", xpos=2, ypos=2)|normalize_newlines }}
</svg>
{%endmacro%}
# Flip


{% if RENDER_MODE == "question" %}

{% if flip_data.type.upper() in flpmacro.globals.AVAILABLE_FLIPS %}

Cite the truth table of flipflop **{{ flip_data.type }}**.

<span dir="rtl" lang="ar">
اذكر جدول الحقيقة للقلاب <span dir="ltr">{{ flip_data.type }}</span>.
</span>


{{draw_flip(flip_data.type)|normalize_newlines}}

{% else %}

Let’s consider the following flip flop **{{ flip_data.type }}**, with its given truth table.

<span dir="rtl" lang="ar">
نفرض القلاب {{ flip_data.type }} المعرّف بجدول الحقيقة الآتي:
</span>

{{draw_custom_flip(flip_data)|normalize_newlines}}
{{ flipmacrosmd.truth_table(
    type=flip_data.type,
    edge="rising",
    customized=True,
    custom_vars=flip_data.inputs,
    custom_values=flip_data.truth_table
) }}

{% endif %}

Complete the following timing diagram, according to the given flip-flop.

<span dir="rtl" lang="ar">
أكمل المخطط المنطقي الآتي، حسب القلاب المعطى.
</span>

<div class="timing-diagram">
{{ tmmacro.draw_timing_diagram(data, mode="question")|normalize_newlines }}
</div>

{% endif %}

{% if RENDER_MODE == "answer" %}
{% if flip_data.type.upper() in flpmacro.globals.AVAILABLE_FLIPS %}

Cite the truth table of flipflop **{{ flip_data.type }}**.

<span dir="rtl" lang="ar">
اذكر جدول الحقيقة للقلاب <span dir="ltr">{{ flip_data.type }}</span>.
</span>

{{ flpmacromd.truth_table(
    type=flip_data.type,
    edge="rising",
    customized=True,
    custom_vars=flip_data.inputs,
    custom_values=flip_data.truth_table
) }}

{% endif %}

<div class="timing-diagram">

{{ tmmacro.draw_timing_diagram(data, mode="answer")|normalize_newlines }}

</div>

{% endif %}

{% if debug and RENDER_MODE == "answer" %}

# Test Truth tables
{{ flpmacromd.truth_table(type="D") }}
{{ flpmacromd.truth_table(type="jk") }}
{{ flpmacromd.truth_table(type="rs") }}

## Customized table
{{ flpmacromd.truth_table(type="XY", customized=True) }}

# Test Flips
{#--------------------
used only to avoid extra newlines which breaks figure
---------------------#}
{% macro draw_example()%}

<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
{{ flpmacro.define_standard_flips()|normalize_newlines }}
{{ flpmacro.define_costum_flip(id="XY", inputs=["X", "Y"])|normalize_newlines }}
{% set step = 100 %}
{% set xstep = 100 %}
{{ flpmacro.place_flip(id="JK", name="JK0", xpos=20, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="D", name="D0", xpos=20+xstep, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="RST", name="RS0", xpos=20+2*xstep, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="JKA", name="JK1", xpos=20+3*xstep, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="XY", name="JK2", xpos=20+4*xstep, ypos=20)|normalize_newlines }}
</svg>

{%endmacro%}

{{draw_example()|normalize_newlines}}

{#--------------------
used only to avoid extra newlines which breaks figure
---------------------#}
{% macro draw_example2()%}

<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
{% set step = 100 %}
{% set xstep = 100 %}
{{ flpmacro.place_flip(id="JK", name="JK0", xpos=20, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="D", name="D0", xpos=20+xstep, ypos=20)|normalize_newlines }}
{{ flpmacro.place_flip(id="RST", name="RS0", xpos=20+2*xstep, ypos=20)|normalize_newlines }}
</svg>

{%endmacro%}

{{draw_example2()|normalize_newlines}}
# Test timing diagram

## Question Mode

{{ tmmacro.draw_timing_diagram(data, mode="question")|normalize_newlines  }}

## Answer Mode

{{ tmmacro.draw_timing_diagram(data, mode="answer")|normalize_newlines  }}

# Test context data
```
{{ flpmacro.globals.AVAILABLE_FLIPS }}
{{ data|pprint }}
{{ flip_data|pprint }}
```
{% endif %}