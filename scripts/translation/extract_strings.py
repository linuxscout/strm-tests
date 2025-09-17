import re
import glob
import json
import os
import argparse

# Regex to catch tr("...") calls in Jinja templates
# pattern = re.compile(r'tr\(\s*[\'"](.+?)[\'"]\s*\)')
pattern = re.compile(r'tr\(\s*[\'"](.+?)[\'"]')
# pattern = re.compile(
#     r'tr\(\s*[\'"](.+?)[\'"]\s*(?:,.*)?\)',
#     re.DOTALL
# )
import itertools


def extract_strings(template_dir, output):
    strings = set()

    # --- Step 1: collect all keys from templates ---
    extensions = ["html", "tex", "txt", "md"]

    files = list(
        itertools.chain.from_iterable(
            glob.glob(os.path.join(template_dir, f"**/*.{ext}"), recursive=True)
            for ext in extensions
        )
    )
    for fname in files:
        with open(fname, encoding="utf-8") as f:
            text = f.read()
        matches = pattern.findall(text)
        strings.update(matches)

    # --- Step 2: load existing translations if file exists ---
    if os.path.exists(output):
        with open(output, encoding="utf-8") as f:
            translations = json.load(f)
    else:
        translations = {}

    # --- Step 3: merge new keys ---
    updated = False
    for key in sorted(strings):
        if key not in translations:
            translations[key] = {"en": f"{key}", "ar": ""}
            updated = True

    # --- Step 4: warn about missing translations ---
    missing = []
    for key in strings:
        for lang in ("en", "ar"):
            if lang not in translations[key] or not translations[key][lang].strip():
                missing.append((key, lang))

    if missing:
        print("⚠️ Missing translations:")
        for key, lang in missing:
            print(f"  - {key} [{lang}] is empty")

    # --- Step 5: save back ---
    if updated:
        with open(output, "w", encoding="utf-8") as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)
        print(f"✅ Updated {output} with {len(strings)} keys")
    else:
        print("ℹ️ No new keys found. Translations file unchanged.")


def main():
    parser = argparse.ArgumentParser(
        description="Extract translatable strings (tr('...')) from Jinja templates into a JSON file"
    )
    parser.add_argument(
        "--templates",
        "-t",
        default="templates",
        help="Path to the templates directory (default: ./templates)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="translations.json",
        help="Path to the translations JSON file (default: ./translations.json)",
    )

    args = parser.parse_args()
    extract_strings(args.templates, args.output)


if __name__ == "__main__":
    main()
