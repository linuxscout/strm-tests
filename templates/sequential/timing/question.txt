{% import "sequential/macros/timingmacros.html" as tmmacro %}

Complete the following timing diagram:  
<span class="aRL">أكمل المخطط الزمني الآتي</span>

{% if RENDER_MODE.lower() == "question" %}
{{ tmmacro.draw_timing_diagram(data, mode="question")|normalize_newlines }}
{%endif%}
{% if RENDER_MODE.lower() == "answer" %}
{{ tmmacro.draw_timing_diagram(data, mode="answer")|normalize_newlines }}
{%endif%}

{% if RENDER_MODE|lower == "answer" and debug %}
### Debug

```
Clock:
{{ data.clock|pprint }}

Input signals (raw):
{{ data.input_signals|pprint }}

Output signals (raw):
{{ data.output_signals|pprint }}

Full data:
{{ data|pprint }}
```


{% for edge in ("rising", "falling", "high", "low", "dual") %}
### Test of list of signals on {{ edge }}

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500">
  {% set s1 = [-1, 2, -2, 3, -1, 2] %}
  {% set s2 = [2, -1, 1, -2, 3] %}
  {% set s3 = [-2, 1, -1, 2, -2, 1] %}
  {% set signals = {"s1":s1, "s2":s2, "s3":s3} %}
  <g transform="translate(0,00)">
    {{ tmmacro.multi_signals(signals, unit_w=60, unit_h=50, v_gap=30,
                             stroke="blue", stroke_w=2,
                             guide_stroke="lightgray", synch_type=edge)|normalize_newlines }}
  </g>
</svg>
{% endfor %}

---

### Test of signal from list

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">
  <g transform="translate(120,20)">
    {{ tmmacro.signal_from_list([-1, 2, -2, 3, -1, 2], 60, 80, "blue", 3, var_name="Diga")|normalize_newlines }}
  </g>
</svg>


### Test of clock signals

**Dual**

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <g transform="translate(20,60)">
    {{ tmmacro.clock_signal(1, 5, 80, 60, "green", 3)|normalize_newlines }}
  </g>
</svg>


**Falling**

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <g transform="translate(20,60)">
    {{ tmmacro.clock_signal(1, 5, 80, 60, "green", 3, edge="falling")|normalize_newlines }}
  </g>
</svg>


**Rising**

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <g transform="translate(20,60)">
    {{ tmmacro.clock_signal(1, 5, 80, 60, "green", 3, edge="rising")|normalize_newlines }}
  </g>
</svg>


**High level**

<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <g transform="translate(20,60)">
    {{ tmmacro.clock_signal(1, 5, 80, 60, "green", 3, edge="high")|normalize_newlines }}
  </g>
</svg>


{% endif %}