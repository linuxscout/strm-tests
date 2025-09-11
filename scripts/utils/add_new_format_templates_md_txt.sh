#!/bin/bash
# Usage: ./make_question.sh md
# This will create question.md next to each question.html

ext="$1"

if [ -z "$ext" ]; then
  echo "Usage: $0 <extension>"
  exit 1
fi

find . -type f -name "question.md" -exec sh -c '
  for f; do
    dir=$(dirname "$f")
    outfile="$dir/question.'$ext'"
    mdfile="$dir/question.md"    
    [ -f "$outfile" ] || cp  "$mdfile" "$outfile"
    echo "Created: $outfile"
  done
' sh {} +
