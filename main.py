def parse(query: str) -> dict:
    if query == "":
        return {}

    parsed = {}
    params = query.partition("?")[2]

    if params == "":
        return {}

    params = params.split("&")

    for p in params:

        if p == "":
            continue

        key, value = p.split("=")
        parsed[key] = value

    return parsed


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if query == "":
        return {}

    cookies = {}
    params = query.split(";")

    for p in params:
        if p == '':
            continue
        temp = p.partition("=")
        cookies[temp[0]] = temp[2]

    return cookies

