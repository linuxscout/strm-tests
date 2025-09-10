#!/bin/bash
# Usage: ./make_question.sh md
# This will create question.md next to each question.html

ext="$1"

if [ -z "$ext" ]; then
  echo "Usage: $0 <extension>"
  exit 1
fi

find . -type f -name "question.html" -exec sh -c '
  for f; do
    dir=$(dirname "$f")
    outfile="$dir/question.'$ext'"
    [ -f "$outfile" ] || touch "$outfile"
    echo "Created: $outfile"
  done
' sh {} +
