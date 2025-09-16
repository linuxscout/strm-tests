{%macro draw_logigram() %}
{% include "bool/logigram/structured_logigram.html.j2"%}
{%endmacro%}

{{tr("Study the following function:")}}

`{{ sop_quest|normalize_formula }}`

{% if RENDER_MODE == "question" %}
{% endif %}

{% if RENDER_MODE == "answer" %}

$$
{{ function_name }} = {{ minterms }} 
$$

**Don't Care**  
$$
{{ function_name }} = {{ dontcares }} 
$$

** {{tr("Truth Table")}}**

| Num | {{ variables[0] }} | {{ variables[1] }} | {{ variables[2] }} | {{ variables[3] }} | F |
|-----|--------------------|--------------------|--------------------|--------------------|---|
{% for i in range(16) -%}
  {% set bits = '{:04b}'.format(i) %}
  {% set bit_list = bits | list %}
| {{ loop.index0 }} | {{ bit_list[0] }} | {{ bit_list[1] }} | {{ bit_list[2] }} | {{ bit_list[3] }} | {{ '1' if i in minterms else 'x' if i in dontcares else 0 }} |
{% endfor %}

** {{tr("Canonical Forms")}}  **

$$
{{ function_name }}({{ variables|join(", ") }}) = {{ dnf_dict.default|normalize_formula }} 
$$

$$
{{ function_name }}({{ variables|join(", ") }}) = {{ cnf_dict.default|normalize_formula }} 
$$

 $$
{{ function_name }}({{ variables|join(", ") }}) = Σ({{ minterms | join(", ") }}) 
$$

$$
{{ function_name }}({{ variables|join(", ") }}) = Π({{ maxterms | join(", ") }}) 
$$

---

### NAND forms <span dir="rtl">بوابات نفي الوصل</span>

$$
{{ function_name }} = {{ nand_sop_dict.default|normalize_formula }} 
$$

    {{tr("Explanation")}} :
   $$
   {{ function_name }} = {{ sop_dict.default|normalize_formula }}
   $$
   {% for explain in nand_sop_dict.explained %}
   $$
   {{ function_name }} = {{ explain|normalize_formula }}
   $$
   {% endfor %}

---

### NOR forms <span dir="rtl">بوابات نفي الفصل</span>
$$
{{ function_name }} = {{ nor_pos_dict.default|normalize_formula }} 
$$

    {{tr("Explanation")}} :
$$
{{ function_name }} = {{ pos_dict.default|normalize_formula }} 
$$
   {% for explain in nor_pos_dict.explained %}
$$ 
{{ function_name }} = {{ explain|normalize_formula }} 
$$
   {% endfor %}

---

** {{tr("Karnaugh map")}}**

{% import "bool/map/kmap_macros.html" as kmap %}
{{ kmap.kmap4svg(minterms, dontcares, groups=simplification, ab=ab, cd=cd)|normalize_newlines }}

-  {{tr("Simplified Sum of products")}} : 
$$ 
{{ sop_dict.default|normalize_formula }} 
$$
-  {{tr("Simplified product of sums")}} : 
$$ 
 {{ pos_dict.default|normalize_formula }} 
$$

---

** {{tr("Logic diagram")}}  **

{{draw_logigram()|normalize_newlines }}

{% endif %}
