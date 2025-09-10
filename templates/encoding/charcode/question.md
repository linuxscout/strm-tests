{% macro encode_decode(charlist=None, codes=None, mode="encode", scheme="ascii") %}
  {% if mode == "encode" %}
#### Encode the following text into {{ scheme|capitalize }}

  **Text:** "{{ charlist|escape_string|join }}"

| Character |{% for ch in charlist %} {{ ch if ch not in [" ", "\n", "\t"] else
    ("space" if ch==" " else "newline" if ch=="\n" else "tab") }} |{% endfor %}

|-----------|{% for ch in charlist %}-------------|{% endfor %}

| {{ scheme|capitalize }} Code Point |{% for cp in codes %} {{ cp }} |{% endfor %}


  {% elif mode == "decode" %}
#### Decode the following {{ scheme|capitalize }} codes into text

**Codes:** {{ codes }}

| {{ scheme|capitalize }} Code Point |{% for code in codes %} {{ code }} |{% endfor %}

|-----------------------------------|{% for code in codes %}-------------|{% endfor %}

| Character |{% for ch in charlist %} {{ ch if ch not in [" ", "\n", "\t"] else
    ("space" if ch==" " else "newline" if ch=="\n" else "tab") }} |{% endfor %}

  {% endif %}
{% endmacro %}


{% if RENDER_MODE == "question" %}
  {% if method in ("encode", "both") %}
#### Encode the following text into {{ scheme|capitalize }}

**Text:** "{{ charlist|join }}"
  {% endif %}

  {% if method in ("decode", "both") %}
#### Decode the following {{ scheme|capitalize }} codes into text

**Codes:** {{ charcodes }}
  {% endif %}

{% elif RENDER_MODE == "answer" %}
{% if method == "both" %}
{{ encode_decode(charlist=charlist, codes=charcodes, mode="encode", scheme=scheme) }}

{{ encode_decode(charlist=charlist, codes=charcodes, mode="decode", scheme=scheme) }}
{% else %}
{{ encode_decode(charlist=charlist, codes=charcodes, mode=method, scheme=scheme) }}
{% endif %}
{% endif %}
