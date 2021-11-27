tuple = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
def sort_list_last(t):
  def end(n): 
    return n[-1]
  return sorted(t, key=end)
print(sort_list_last(tuple))
