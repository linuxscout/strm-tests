Let the function be given by its canonical form, Draw the Karnaugh table and simplify.  
<span dir="rtl">لتكن الدالة المعطاة بشكلها القانوني، ارسم جدول كارنو وبسطها</span>  

{% if "fr" in languages %}
Soit la fonction donnée par sa forme canonique, Tracer la table de karnaugh et simplifier.  
{% endif %}

{% if RENDER_MODE == "question" %}
{% for data in data_list %}
- 
$$
 F{{ loop.index }}(A,B,C,D) = {{ data.dnf_dict.default|normalize_formula }} 
$$

{% endfor %}
{% endif %}

{% if RENDER_MODE == "answer" %}
{% for data in data_list %}

$$
 F{{ loop.index }}(A,B,C,D) = {{ data.dnf_dict.default|normalize_formula }} 
$$
  

{% import "bool/map/kmap_macros.html" as kmap %}

{{ kmap.kmap4svg(data.minterms, data.dontcares, groups=data.simplification, ab=data.ab, cd=data.cd)|normalize_newlines }}


- Simplified Sum of products : 
$$
 {{ data.sop_dict.default|normalize_formula }} 
$$

- Simplified product of sums : 
$$
 {{ data.pos_dict.default|normalize_formula }} 
$$


{% endfor %}
{% endif %}
