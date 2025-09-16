{{tr("Simpilfy the following expression")}}

$$
{{ function_name }} = {{ sop_quest|normalize_formula }}  
$$

{% if RENDER_MODE == "question" %}
{% endif %}

{% if RENDER_MODE == "answer" %}

{% import "bool/map/kmap_macros.html" as kmap %}

<div>
{{ kmap.kmap4svg(minterms, dontcares, groups=simplification, ab=ab, cd=cd) | normalize_newlines}}
</div>

-  {{tr("Simplified Sum of products")}} :
 $$
 {{ sop_dict.default |normalize_formula }} 
 $$

-  {{tr("Simplified product of sums")}} :
$$
 {{ pos_dict.default |normalize_formula }}
$$

{% endif %}
