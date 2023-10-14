def longest_common_prefix(strs):
  prefix = []
  while len(prefix) < len(strs[0]):
    prefix_len = len(prefix)
    ch = strs[0][prefix_len]

    for s in strs:
      if prefix_len >= len(s) or s[prefix_len] != ch:
        return ''.join(prefix)

    prefix.append(ch)

  return ''.join(prefix)


print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''