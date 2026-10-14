#!/usr/bin/env bash
# Install or remove DevReach skills for Claude Code.
#
#   ./install.sh                      install all skills to ~/.claude/skills
#   ./install.sh project-to-post      install selected skills
#   ./install.sh --project ...        install to ./.claude/skills (current project)
#   ./install.sh --uninstall ...      remove installed DevReach skills
#   ./install.sh --list               list available skills
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)/skills"
DEST="${HOME}/.claude/skills"
MODE=install
NAMES=()

for arg in "$@"; do
  case "$arg" in
    --project) DEST="$(pwd)/.claude/skills" ;;
    --uninstall) MODE=uninstall ;;
    --list) MODE=list ;;
    -h|--help) sed -n '2,8p' "$0"; exit 0 ;;
    -*) echo "unknown option: $arg" >&2; exit 2 ;;
    *) NAMES+=("$arg") ;;
  esac
done

AVAILABLE=()
for dir in "$SRC"/*/; do AVAILABLE+=("$(basename "$dir")"); done

if [ "$MODE" = list ]; then printf '%s\n' "${AVAILABLE[@]}"; exit 0; fi
[ ${#NAMES[@]} -eq 0 ] && NAMES=("${AVAILABLE[@]}")

for name in "${NAMES[@]}"; do
  # Only ever touch directories that are DevReach skills.
  if [[ "$name" == */* || "$name" == .* || ! -f "$SRC/$name/SKILL.md" ]]; then
    echo "not a DevReach skill: $name (see ./install.sh --list)" >&2
    exit 1
  fi
done

mkdir -p "$DEST"
for name in "${NAMES[@]}"; do
  if [ "$MODE" = uninstall ]; then
    if [ -d "$DEST/$name" ]; then rm -rf "${DEST:?}/$name"; echo "removed   $DEST/$name"; fi
  else
    rm -rf "${DEST:?}/$name"
    cp -R "$SRC/$name" "$DEST/$name"
    echo "installed $DEST/$name"
  fi
done

[ "$MODE" = install ] && echo "Start a new Claude Code session to load the skills."
exit 0
