{%macro draw_logigram() %}
{% include "bool/logigram/structured_logigram.html.j2"%}
{%endmacro%}

{% set debug = False %}
{% import "bool/map/kmap_macros.html" as kmap %}

{{tr("Study the following circuit:")}}

- {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = {{ data.minterms }} 
$$

  {% endfor %}

** {{tr("Don't Care")}} **  
- {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = {{ data.dontcares }} 
$$

  {% endfor %}


$$
 F(A,B,C,D) = {{ sop_quest|normalize_formula }} 
$$


{% if RENDER_MODE == "answer" %}

** {{tr("Inputs and Outputs")}}  <span dir="rtl">المداخل والمخارج</span>**

- Inputs  
  {% for var in variables %}
  - {{ var }} = 0 / 1
  {% endfor %}

- Outputs  
  {% for funct_name in function_name_list %}
  - {{ funct_name }} = 0 / 1
  {% endfor %}

** {{tr("Truth Table")}}**

| Num | {{ variables[0] }} | {{ variables[1] }} | {{ variables[2] }} | {{ variables[3] }} {% for funct_name in function_name_list %} | {{ funct_name }} {% endfor %} |
|-----|--------------------|--------------------|--------------------|--------------------{% for funct_name in function_name_list %}|--------------------{% endfor %}|
{% for i in range(16) %}
{% set bits = '{:04b}'.format(i) %}
{% set bit_list = bits | list %}
| {{ loop.index0 }} | {{ bit_list[0] }} | {{ bit_list[1] }} | {{ bit_list[2] }} | {{ bit_list[3] }} {% for idx in range(data_list | length) %}{% set minterms = minterms_list[idx] %}{% set dontcares = dontcares_list[idx] %}| {{ '1' if i in minterms else 'x' if i in dontcares else 0 }} {% endfor %} |
{% endfor %}

** {{tr("Canonical Forms")}}  **

- ** {{tr("First Canonical Forms")}}  **  
  {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = {{ data.dnf_dict.default|normalize_formula }} 
$$

  {% endfor %}

- ** {{tr("Second Canonical Forms")}}  **  
  {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = {{ data.cnf_dict.default|normalize_formula }} 
$$

  {% endfor %}

- ** {{tr("First Canonical Forms")}}  **  
  {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = ∑({{ data.minterms | join(", ") }}) 
$$

  {% endfor %}

- ** {{tr("Second Canonical Forms")}}  **  
  {% for data in data_list %}
  - 
$$
 {{ data.function_name }} = ∏({{ data.maxterms | join(", ") }}) 
$$

  {% endfor %}

{% if debug or method.lower() == "nand" %}
** {{tr("NAND forms")}} **

{% for data in data_list %}
1. 
$$
 {{ data.function_name }} = {{ data.nand_sop_dict.default|normalize_formula }} 
$$


    {{tr("Explanation")}} :  
   - 
$$
 {{ data.function_name }} = {{ data.sop_dict.default|normalize_formula }} 
$$
  
   {% for explain in data.nand_sop_dict.explained %}
   - 
$$
 {{ data.function_name }} = {{ explain|normalize_formula }} 
$$

   {% endfor %}
{% endfor %}
{% endif %}

{% if debug or method.lower() == "nor" %}
** {{tr("NOR forms")}} **

{% for data in data_list %}
1. 
$$
 {{ data.function_name }} = {{ data.nor_pos_dict.default|normalize_formula }} 
$$


    {{tr("Explanation")}} :  
   - 
$$
 {{ data.function_name }} = {{ data.pos_dict.default|normalize_formula }} 
$$
  
   {% for explain in data.nor_pos_dict.explained %}
   - 
$$
 {{ data.function_name }} = {{ explain|normalize_formula }} 
$$

   {% endfor %}
{% endfor %}
{% endif %}

** {{tr("Karnaugh map")}}  **

{% for data in data_list %}
{{ kmap.kmap4svg(minterms=data.minterms, dontcares=data.dontcares, groups=data.simplification, ab=data.ab, cd=data.cd)|normalize_newlines }}

-  {{tr("Simplified Sum of products")}} : 
$$
 {{ data.function_name }} = {{ data.sop_dict.default|normalize_formula }} 
$$

-  {{tr("Simplified product of sums")}} : 
$$
 {{ data.function_name }} = {{ data.pos_dict.default|normalize_formula }} 
$$

{% endfor %}

** {{tr("Logic diagram")}}  **

{{draw_logigram()|normalize_newlines}}

{% endif %}

