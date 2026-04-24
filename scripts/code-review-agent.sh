#!/bin/bash

echo "Running code review agent..."

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.java$')

if [ -z "$FILES" ]; then
  exit 0
fi

WARNING_FOUND=0

for file in $FILES; do
  if grep -n "System.out.println" "$file"; then
    echo "WARNING: $file contains System.out.println. Use a logger instead."
    WARNING_FOUND=1
  fi

  if grep -n "RestTemplate" "$file"; then
    echo "WARNING: $file uses RestTemplate. Consider WebClient for newer Spring apps."
    WARNING_FOUND=1
  fi
done

if [ "$WARNING_FOUND" -eq 1 ]; then
  echo ""
  echo "Code review warning found."
  echo "Commit will continue, but please review the warnings above."
fi

exit 0