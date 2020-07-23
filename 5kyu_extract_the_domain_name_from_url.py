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


    return url


s = "http://github.com/carbonfive/raygun"
# s = "http://www.zombie-bites.com"
s.index("//")
domain_name(s)
