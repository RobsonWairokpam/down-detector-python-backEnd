
def web_name():
    fname = "demo.txt"
    d = {}
    with open(fname) as f:
        for line in f:
            (key, *val) = line.strip().split(',')
            d[key] = val
            
    return d

"""
fname = "demo.txt"
d = {}
with open(fname) as f:
    for line in f:
        (key, *val) = line.strip().split(',')
        d[key] = val
            
for web in d:
    webname = d[web]
    print(webname[1])
"""