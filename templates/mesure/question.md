# {{tr("Question")}}
**{{ question }}**

---

{% if RENDER_MODE.lower() == "answer" %}
## {{tr("Given:")}}
{% for key, val in given.items() %}
- {{ key|capitalize }} = {{ "%.2f"|format(val.value) }} {{ val.unit }}
{% endfor %}

---

## {{tr("Solution steps")}}

| {{tr("Step")}} | {{tr("Operation")}} | {{tr("Expression")}} |
|------|-----------|------------|
{% for step in solution %}
| {{ step.step }} | {{ step.operation }} | {{ step.expression }} |
{% endfor %}

---

## {{tr("Final Answer")}}
**{{ answer }}**
{% endif %}
