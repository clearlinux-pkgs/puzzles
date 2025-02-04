#!/usr/bin/bash
set -e -o pipefail # Fail the entire pipeline if any part of it fails

echo -n "Pulling package repo changes: "
git pull --ff-only

# Upstream website doesn't list the actual version; we only get it from the HTTP
# redirect
UPSTREAM_URL="https://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles.tar.gz"

NEW_URL=$(curl -sI "${UPSTREAM_URL}" | grep -i '^Location: ' | sed 's/Location://')

if [[ "" == "${NEW_URL}" ]]; then
	echo "Failed to get the new URL"
	exit 1
fi
echo "New URL: ${NEW_URL}"

echo "Updating Makefile."
sed -i "s|^URL=.*|URL = ${NEW_URL}|" Makefile

# Check whether anything changed. Should have been caught above, so this is
# probably a script failure.
if git diff-index --quiet HEAD --; then
	echo "Weird, nothing changed."
	exit 1
fi

# Build the new version
echo "Running autospec."
make autospec

echo "Sending to Koji."
make koji-nowait
