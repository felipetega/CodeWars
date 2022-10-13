def domain_name(url):
    name = ""
    start = 0
    if "www." in url:
        start += 4
    if "http://" in url:
        start += 7
    if "https://" in url:
        start += 8
    i = start
    while True:
        if url[i] != ".":
            name += url[i]
            i += 1
        else:
            break
    return name
