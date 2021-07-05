def backtrack(string, open, closed, max):
    if len(string) == 2*max:
        permute.append(string)
        return
    if open < max:
        backtrack(string+"(", open+1, closed, max)
    if closed < open:
        backtrack(string+")", open, closed+1, max)


permute = list()

backtrack("", 0, 0, 50)
print(permute)
