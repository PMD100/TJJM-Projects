declare -A THEME=(
 ["tjjm-gym-websites.liquid"]="0a102f4828869f4a1d7921f6a4061eaa"
 ["tjjm-gym-websites-2.liquid"]="580c7d60101558a13bce974dae4adee1"
 ["tjjm-gym-websites-3.liquid"]="d949fc0edc0db67242e28d88f22a1fe0"
 ["tjjm-gym-websites-4.liquid"]="0ef65e0f5f60289380330224a5253b5d"
 ["tjjm-gym-websites-5.liquid"]="70fa4a3b8526024fe7e6431c3002b88e"
 ["tjjm-gym-websites-6.liquid"]="ab0156e700d6474e62313e194c0fe3ec"
)
for f in tjjm-gym-websites.liquid tjjm-gym-websites-2.liquid tjjm-gym-websites-3.liquid tjjm-gym-websites-4.liquid tjjm-gym-websites-5.liquid tjjm-gym-websites-6.liquid; do
  m=$(md5sum "$f" | cut -d' ' -f1); s=$(wc -c < "$f")
  if [ "$m" = "${THEME[$f]}" ]; then st=MATCH; else st="MISMATCH(theme=${THEME[$f]})"; fi
  printf "%-30s size=%5d headroom=%5d md5=%s %s\n" "$f" "$s" "$((24576-s))" "$m" "$st"
done
