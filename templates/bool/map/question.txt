Simplify the following Karnaugh table  
<span dir="rtl">بسّط الدوال الآتية باستعمال جدول كارنوف.</span>  

{% if "fr" in languages %}
Simplifier le tableau de Karnaugh suivant:  
{% endif %}

{% if RENDER_MODE == "question" %}
{% endif %}

{% for data in data_list %}

{% import "bool/map/kmap_macros.html" as kmap %}

{% if RENDER_MODE == "question" %}
{{ kmap.kmap4svg(data.minterms, data.dontcares, groups=[], ab=data.ab, cd=data.cd)|normalize_newlines }}
 {% endif %}
{% if RENDER_MODE == "answer" %}
{{ kmap.kmap4svg(data.minterms, data.dontcares, groups=data.simplification, ab=data.ab, cd=data.cd)|normalize_newlines }}
 {% endif %}

{% if RENDER_MODE == "answer" %}
- Simplified Sum of products : 
$$ 
{{ data.sop_dict.default|normalize_formula }} 
$$
- Simplified product of sums :
$$ 
{{ data.pos_dict.default|normalize_formula }} 
$$
{% endif %}

{% endfor %}
