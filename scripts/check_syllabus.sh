#!/usr/bin/env bash
# Usage: scripts/check_syllabus.sh FROM TO
# Fails if any week file is missing, too short, or contains placeholder text.
set -uo pipefail
from=${1:-1}; to=${2:-20}; fail=0
for w in $(seq "$from" "$to"); do
  d=$(printf "03-syllabus/week-%02d" "$w")
  for f in README lessons concepts exercises hints quiz gate retro; do
    p="$d/$f.md"
    if [ ! -f "$p" ]; then echo "MISSING $p"; fail=1; continue; fi
    n=$(wc -w < "$p")
    min=40; [ "$f" = README ] && min=80
    [ "$n" -lt "$min" ] && { echo "THIN $p ($n words, need $min)"; fail=1; }
    grep -qi "placeholder\|TODO: write" "$p" && { echo "PLACEHOLDER TEXT $p"; fail=1; }
  done
done
[ "$fail" -eq 0 ] && echo "OK weeks $from-$to"
exit "$fail"
