{% macro encode_decode(charlist=None, codes=None, mode="encode", scheme="ascii") %}
  {% if mode == "encode" %}
#### {{tr("Encode the following text into")}} {{ scheme|upper }}

  **{{tr("Text:")}}** "{{ charlist|escape_string|join }}"

| {{tr("Character")}} |{% for ch in charlist %} {{ ch if ch not in [" ", "\n", "\t"] else
    ("space" if ch==" " else "newline" if ch=="\n" else "tab") }} |{% endfor %}

|-----------|{% for ch in charlist %}-------------|{% endfor %}

| {{tr("{scheme} Code Point",scheme=scheme)}}  |{% for cp in codes %} {{ cp }} |{% endfor %}


  {% elif mode == "decode" %}
#### {{tr("Decode the following {scheme} codes into text", scheme=scheme|upper)}}

**{{tr("Codes:")}}** {{ codes }}

| {{tr("{scheme} Code Point",scheme=scheme|upper)}} |{% for code in codes %} {{ code }} |{% endfor %}

|-----------------------------------|{% for code in codes %}-------------|{% endfor %}

| {{tr("Character")}} |{% for ch in charlist %} {{ ch if ch not in [" ", "\n", "\t"] else
    ("space" if ch==" " else "newline" if ch=="\n" else "tab") }} |{% endfor %}

  {% endif %}
{% endmacro %}


{% if RENDER_MODE == "question" %}
  {% if method in ("encode", "both") %}
#### {{tr("Encode the following text into")}} {{ scheme|upper }}

**{{tr("Text:")}}** "{{ charlist|join }}"
  {% endif %}

  {% if method in ("decode", "both") %}
#### {{tr("Decode the following {scheme} codes into text", scheme=scheme|upper)}}

**{{tr("Codes:")}}** {{ charcodes }}
  {% endif %}

{% elif RENDER_MODE == "answer" %}
{% if method == "both" %}
{{ encode_decode(charlist=charlist, codes=charcodes, mode="encode", scheme=scheme) }}

{{ encode_decode(charlist=charlist, codes=charcodes, mode="decode", scheme=scheme) }}
{% else %}
{{ encode_decode(charlist=charlist, codes=charcodes, mode=method, scheme=scheme) }}
{% endif %}
{% endif %}
