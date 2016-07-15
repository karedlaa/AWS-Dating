s='dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif'

d = s.split('\n')
print s
k={}
for each_line in d:
    print each_line, "-----"
    if "." not in each_line:
        len_diff = len(each_line) - len(each_line.strip())
        if len_diff == 0:
            path="/"
        if len_diff == 1:
            path = "/" + each_line.strip()
        if len_diff == 2:
            path += '/' + each_line.strip()
            print path
    elif ".jpeg" in each_line or ".png" in each_line or ".gif" in each_line:
        print path
        k[each_line]=("image", path)


print k