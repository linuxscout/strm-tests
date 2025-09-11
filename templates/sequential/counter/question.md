{% set debug = True %}
{% import "sequential/macros/flipmacros.html" as flpmacro%}
{% import "sequential/macros/flipmacros.md" as flpmacromd%}
{% import "sequential/macros/timingmacros.html" as tmmacro%}


## Counter


{% if RENDER_MODE == "question" %}

Let have the following setup  
<span dir="rtl" lang="ar">إليك هذا التركيب</span>

drawn by draw counter  

{{ flpmacro.draw_counter(flip="JKA", counter_type="", size=counter_data.nbits)|normalize_newlines }}



Cite the truth table of flipflop {{ counter_data.flip_type_list[0] }}.  
<span dir="rtl" lang="ar">
  اذكر جدول الحقيقة للقلاب <span dir="ltr">{{ counter_data.flip_type_list[0] }}</span>.
</span>

Complete the following timing diagram, according to given flipflop.  
<span dir="rtl" lang="ar">
  أكمل المخطط المنطقي الآتي، حسب القلاب المعطى.
</span>

{{ tmmacro.draw_timing_diagram(data, mode="question")|normalize_newlines }}

{% endif %}

{% if RENDER_MODE == "answer" %}

Cite the truth table of flipflop {{ counter_data.flip_type_list[0] }}.  
<span dir="rtl" lang="ar">
  اذكر جدول الحقيقة للقلاب <span dir="ltr">{{ counter_data.flip_type_list[0] }}</span>.
</span>

{{ flpmacromd.truth_table(type=counter_data.flip_type_list[0], edge="rising") }}

{{ tmmacro.draw_timing_diagram(data, mode="answer")|normalize_newlines }}

{% endif %}

{% if debug and RENDER_MODE == "answer" %}
**Counter n bits Jk**  

{{ flpmacro.draw_counter(flip="JKA", counter_type="", size=4)|normalize_newlines }}

**Flipflop syn/asyn Jk**  

<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">{{ flpmacro.place_flip(id="JKA", name="jk4", xpos=5, ypos=4)|normalize_newlines }}</svg>

{% endif %}
