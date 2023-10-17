import timeit

def generate_brackets(n):
    return add_brackets('', n * 2)

def add_brackets(line, m):
    if m == 0:
        return [line]
    depth = 0
    for char in line:
        if char == '(':
            depth += 1
        if char == ')':
            depth -= 1
    lines = []
    if depth == m:
        line += ')' * m
        return [line]
    elif depth == 0:
        line += '('
        lines = add_brackets(line, m-1)
        return lines
    elif depth > 0:
        line1 = line + '('
        line2 = line + ')'
        lines = add_brackets(line1, m-1) + add_brackets(line2, m-1)
        return lines
    
def generate_brackets_alt(n):
  brackets_list = [set() for _ in range(n+1)]

  brackets_list[1].add("()")

  for i in range(2, n + 1):
    for s in brackets_list[i - 1]:
      brackets_list[i].add("(" + s + ")")

    for j in range(1, i):
      for s1 in brackets_list[j]:
        for s2 in brackets_list[i - j]:
          brackets_list[i].add(s1 + s2)

  return list(brackets_list[-1])

  
print(generate_brackets(1))
# ['()']

start = timeit.timeit()
print(generate_brackets(3))
end = timeit.timeit()
print (end - start)
start = timeit.timeit()
print(generate_brackets_alt(3))
end = timeit.timeit()
print (end - start)
# ['((()))', '(()())', '()(())', '()()()', '(())()']
