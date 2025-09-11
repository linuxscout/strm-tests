Give the intervals which can be represented in **positive numbers**, **absolute value**, **1's complement**, and **2's complement** on **{{ number }} bits**.  

<span dir="rtl">
حدد المجالات التي يمكن تمثيلها لأعداد الموجبة والتمثيل بالقيمة المطلقة والمتمم إلى 1 و 2 على {{ number }} بت
</span>  

{% if "fr" in languages %}
Donner les intervalles qu'on peut représenter en **nombres positifs**, **valeur absolue**, **complément à 1** et **complément à 2** sur **{{ number }} bits**.  
{% endif %}

---

{% if RENDER_MODE == "answer" %}
| Representation       | Formula Range                                                                 | Evaluated Range                                      |
|----------------------|-------------------------------------------------------------------------------|------------------------------------------------------|
| Positives            | [0; 2<sup>{{ number }} - 1</sup>]                                            | [0; {{ 2**number - 1 }}]                             |
| Unsigned value       | [-(2<sup>{{ number - 1 }}</sup> - 1); 2<sup>{{ number - 1 }}</sup> - 1]      | [{{ - (2**(number-1) - 1) }}, {{ 2**(number-1) - 1 }}] |
| One's complement     | [-(2<sup>{{ number - 1 }}</sup> - 1); 2<sup>{{ number - 1 }}</sup> - 1]      | [{{ - (2**(number-1) - 1) }}, {{ 2**(number-1) - 1 }}] |
| Two's complement     | [-2<sup>{{ number - 1 }}</sup>; 2<sup>{{ number - 1 }}</sup> - 1]            | [{{ - (2**(number-1)) }}, {{ 2**(number-1) - 1 }}]   |
{% endif %}
