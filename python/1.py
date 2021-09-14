list1 = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]

def min_jumps(l):
  def find(ls, n):
    n += 1
    if len(ls) <= 1: 
      return ls
    m = max(ls)
    if m >= len(ls):
      return n
    el = int(ls[m])
    ls_next = ls[m:el]
    return find(ls_next, n)
  el = int(l[0])
  ls_next = l[1:el]
  n = find(ls_next, 1)
  return n

minj = min_jumps(list1)
print(f'min jumps: {minj}')
