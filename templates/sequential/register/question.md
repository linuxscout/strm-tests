{% set debug = False %}
{% import "sequential/macros/flipmacros.html" as flpmacro%}
{% import "sequential/macros/flipmacros.md" as flpmacromd%}
{% import "sequential/macros/timingmacros.html" as tmmacro%}

## {{tr("Register")}}

{% if RENDER_MODE == "question" %}

 {{tr("Let have the following setup")}}   


{{flpmacro.draw_register_generic(        flips_list=register_data.flip_type_list,
        outputs=register_data.outputs,
        size=register_data.nbits,
        shift=register_data.shift
    )|normalize_newlines}}


 {{tr("Cite the truth table of flipflop")}}  {{register_data.flip_type_list[0]}}.  


 {{tr("Complete the following timing diagram, according to the given setup.")}}   

{{tmmacro.draw_timing_diagram(data, mode="question")|normalize_newlines}}

{% endif %}

---

{% if RENDER_MODE == "answer" %}

 {{tr("Cite the truth table of flipflop")}}  {{register_data.flip_type_list[0]}}.  

<div class="arabic">
اذكر جدول الحقيقة للقلاب <span class="lr">{{register_data.flip_type_list[0]}}</span>.
</div>

{{flpmacromd.truth_table(
    type=register_data.flip_type_list[0],
    edge="rising"
)}}

{{tmmacro.draw_timing_diagram(data, mode="answer")|normalize_newlines}}

{% endif %}

---

{% if debug and RENDER_MODE == "answer" %}
**Register**

{{flpmacro.draw_register_generic(flips_list=["D","JK","RST"], outputs=["Q0","Q1","Q2"], size=3)|normalize_newlines}}


**Register n bits**

{{flpmacro.draw_register(flip="D", register_type="", size=6)|normalize_newlines}}


**Register n bits JK**

{{flpmacro.draw_register(flip="JK", register_type="", size=6)|normalize_newlines}}


Test inverse connection  

{{flpmacro.draw_register_generic(
        flips_list=register_data.flip_type_list,
        outputs=register_data.outputs,
        size=register_data.nbits,
        shift=register_data.shift,
        link_type="inverse",
    )|normalize_newlines}}


Test clock connection  


{{flpmacro.draw_register_generic(
        flips_list=register_data.flip_type_list,
        outputs=register_data.outputs,
        size=register_data.nbits,
        shift=register_data.shift,
        link_type="clock",
    )|normalize_newlines}}


Test inverse clock connection  

{{flpmacro.draw_register_generic(
        flips_list=register_data.flip_type_list,
        outputs=register_data.outputs,
        size=register_data.nbits,
        shift=register_data.shift,
        link_type="inverse_clock",
)|normalize_newlines}}


{% endif %}
