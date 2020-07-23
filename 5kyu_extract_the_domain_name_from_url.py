def domain_name(url):
    if 'www.' in url:
        www_index = url.index('www.')
        url = url[www_index + 4:]
        dot_index = url.index('.')
        url = url[:dot_index]

    elif '//' in url:
        backslash_index = url.index('//')
        url = url[backslash_index + 2:]
        dot_index = url.index('.')
        url = url[:dot_index]

    elif '.' in url:
        dot_index = url.index('.')
        url = url[:dot_index]

    return url

def domain_name_one_liner(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

s = "http://github.com/carbonfive/raygun"
# s = "http://www.zombie-bites.com"
s.index("//")
%timeit domain_name(s)

%timeit domain_name_one_liner(s)
