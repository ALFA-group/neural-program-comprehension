File "test.py", line 15, in <module>
    print(find_lowest(a))
File "test.py", line 12, in find_lowest
  return lowest(lst[0], lst[1:])
File "test.py", line 9, in lowest
  return lowest(rest[0], rest[1:])
File "test.py", line 9, in lowest
  return lowest(rest[0], rest[1:])
File "test.py", line 13, in lowest
  return lowest(first, rest)
File "test.py", line 13, in lowest
  return lowest(first, rest)
[Previous line repeated 993 more times]
File "test.py", line 6, in lowest
  if len(rest) == 0:
RecursionError: maximum recursion depth exceeded in comparison