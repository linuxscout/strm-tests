# Question
**{{ question }}**

---

{% if RENDER_MODE.lower() == "answer" %}
## Given
{% for key, val in given.items() %}
- {{ key|capitalize }} = {{ "%.2f"|format(val.value) }} {{ val.unit }}
{% endfor %}

---

## Step-by-step solution

| Step | Operation | Expression |
|------|-----------|------------|
{% for step in solution %}
| {{ step.step }} | {{ step.operation }} | {{ step.expression }} |
{% endfor %}

---

## Final Answer
**{{ answer }}**
{% endif %}
