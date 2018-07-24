from sexpdata import loads, Symbol

def parse_pkg(pkg):
    meta = {}
    sexp = loads(pkg)
    for i in range(len(sexp)):
        e = sexp[i]
        if type(e) == Symbol:
            v = e.value()[-1]
            if v == ':':
                meta[e.value()] = sexp[i+1].value() if type(sexp[i+1]) == Symbol else sexp[i+1]
    return meta
