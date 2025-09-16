{{tr("Represent in 1's and 2's complement, the following number", mode="par")}}

**{{ number }}**

---

{% if RENDER_MODE == "answer" %}
- -{{ number }} = ( {{ binary|group4 }} )<sub>2</sub>  
- ( {{ cp1|group4 }} )<sub>c1</sub>  
- +1  
- ( {{ cp2|group4 }} )<sub>c2</sub>  
{% endif %}
