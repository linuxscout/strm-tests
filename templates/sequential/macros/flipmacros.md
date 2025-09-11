{# -----------------------
 draw a truth table for a flipflop (Markdown version)
-------------------#}
{% macro truth_table(type="D", edge="rising", customized=False, custom_vars=["X","Y"], custom_values=["1","Q","X","Q'"]) %}
### Truth table of {{ type }} flip-flop

{% set edge_symbol = "↑" if edge == "rising" else "↓" %}

{% if type.lower() in ("custom","customized") or customized %}
| Ck | {{custom_vars[0]}} | {{custom_vars[1]}} | Qₜ   |
|----|-------------------|-------------------|------|
| 0  | X                 | X                 | Qₜ₋₁ |
| {{edge_symbol}} | 0 | 0 | {{custom_values[0]}} |
| {{edge_symbol}} | 0 | 1 | {{custom_values[1]}} |
| {{edge_symbol}} | 1 | 0 | {{custom_values[2]}} |
| {{edge_symbol}} | 1 | 1 | {{custom_values[3]}} |


{% elif type.lower() == "d" %}
| Ck     | D | Qₜ   |
|--------|---|------|
| 0/1    | X | Qₜ₋₁ |
| {{edge_symbol}} | 0 | 0    |
| {{edge_symbol}} | 1 | 1    |


{% elif type.lower() == "dlatch" %}
| V | D | Qₜ   |
|---|---|------|
| 0 | X | Qₜ₋₁ |
| 1 | 0 | 0    |
| 1 | 1 | 1    |


{% elif type.lower() == "jk" %}
| Ck | J | K | Qₜ   | Remark   |
|----|---|---|------|----------|
| 0  | X | X | Qₜ₋₁ |          |
| {{edge_symbol}} | 0 | 0 | Qₜ₋₁ |          |
| {{edge_symbol}} | 0 | 1 | 0    |          |
| {{edge_symbol}} | 1 | 0 | 1    |          |
| {{edge_symbol}} | 1 | 1 | ¬Qₜ₋₁ | **Toggle** |

{% elif type.lower() == "jkasyn" %}
| Mode         | Pr | Cl | Ck | J | K | Q+   | Remark       |
|--------------|----|----|----|---|---|------|--------------|
| Asynchronous | 0  | 0  | X  | X | X | X    | **Forbidden**|
|              | 0  | 1  | X  | X | X | 1    | Set to 1     |
|              | 1  | 0  | X  | X | X | 0    | Set to 0     |
| Synchronous  | 1  | 1  | 0/1| X | X | Q    | Memory       |
|              | 1  | 1  | {{edge_symbol}} | 0 | 0 | Q | Memory |
|              | 1  | 1  | {{edge_symbol}} | 0 | 1 | 0 | Reset |
|              | 1  | 1  | {{edge_symbol}} | 1 | 0 | 1 | Set   |
|              | 1  | 1  | {{edge_symbol}} | 1 | 1 | ¬Q | **Toggle** |


{% elif type.lower() == "rs" %}
| R | S | Qₜ   | Remark       |
|---|---|------|--------------|
| 0 | 0 | Qₜ   | Memory       |
| 0 | 1 | 1    | Set          |
| 1 | 0 | 0    | Reset        |
| 1 | 1 | X    | **Forbidden**|


{% elif type.lower() == "rst" %}
| Ck | R | S | Qₜ   | ¬Qₜ  | Remark       |
|----|---|---|------|------|--------------|
| 0  | X | X | Qₜ₋₁ | ¬Qₜ₋₁ |              |
| {{edge_symbol}} | 0 | 0 | Qₜ₋₁ | ¬Qₜ₋₁ |              |
| {{edge_symbol}} | 0 | 1 | 1    | 0    |              |
| {{edge_symbol}} | 1 | 0 | 0    | 1    |              |
| {{edge_symbol}} | 1 | 1 | X    | X    | **Forbidden**|


{% else %}
**No table to display.** Please check the flip-flop type "{{ type }}". Use customized type if needed.
{% endif %}
{% endmacro %}
