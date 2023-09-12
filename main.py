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


