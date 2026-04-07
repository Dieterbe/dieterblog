#!/usr/bin/env bash
set -euo pipefail

# copy all files/directories from $1 to $2, normalizing the content

NORMALIZE_RULES=(
  's#(src="/[^"]*_hu_)[[:xdigit:]]+(\.webp")#\1HASH\2#g' # hashes in image
  's#meta name="generator" content="Hugo 0\.[0-9]+\.[0-9]+">#meta name="generator" content="Hugo VERSION">#g'
  's#src.dieter.plaetinck.be#HOST#g'
  's#dieter.plaetinck.be#HOST#g'
  's#dieter-dev.plaetinck.be#HOST#g'
  's#<link href="/style.min\.[a-z0-9]+\.css" rel="stylesheet">#<link href="/style.min.CSSHASH.css" rel="stylesheet">#g'
)

normalize_stream() {
  local sed_args=()
  local rule
  for rule in "${NORMALIZE_RULES[@]}"; do
    sed_args+=(-e "$rule")
  done
  sed -E "${sed_args[@]}"
}

is_text_file() {
  # Returns success for text files, failure for binary files.
  grep -Iq . "$1"
}

normalize_tree() {
  local src_dir=$1
  local dst_dir=$2
  local src_abs file rel out

  src_abs=$(realpath "$src_dir")
  mkdir -p "$dst_dir"

  # First, create all directories (including empty ones)
  find "$src_abs" -type d -print0 |
    while IFS= read -r -d '' dir; do
      if [ "$dir" != "$src_abs" ]; then
        rel=${dir#"$src_abs"/}
        mkdir -p "$dst_dir/$rel"
      fi
    done

  # Then copy all files
  find "$src_abs" -type f -print0 |
    while IFS= read -r -d '' file; do
      rel=${file#"$src_abs"/}
      out="$dst_dir/$rel"

      #if is_text_file "$file"; then
      #  normalize_stream < "$file" > "$out"
      #else
      #  cp -p -- "$file" "$out"
      #fi
      case "$rel" in
      *.html | *.css | *.js | *.xml | *.txt | *.md)
        normalize_stream <"$src_dir/$rel" >"$dst_dir/$rel"
        ;;
      *)
        cp -p "$src_dir/$rel" "$dst_dir/$rel"
        ;;
      esac
    done
}

normalize_tree "$1" "$2"
