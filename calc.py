modules = [
    (lambda _, __, ___: _(_, __, ___))(
        lambda _, __, ___:
            chr(___ % __) + _(_, __, ___ // __) if ___ else
            chr(1 << 5)[:-1],
        1 << 8,
        545200826904043625543027),
    (lambda _, __, ___: _(_, __, ___))(
        lambda _, __, ___:
            chr(___ % __) + _(_, __, ___ // __) if ___ else
            chr(1 << 5)[:-1],
        1 << 8,
        7567731),
]
subprocess, sys = map(__import__, modules)


def main(expr):
    popen = getattr(subprocess, 'Popen')
    p = popen(['python3', '-c', getattr('print({})', 'format')(expr)],
              stdout=getattr(subprocess, 'PIPE'))
    result, _ = getattr(p, 'communicate')()
    return getattr(getattr(result, 'decode')('utf-8'), 'strip')()


x = main(getattr(sys, 'argv')[1])
try:
    float(x)
except ValueError:
    getattr(sys, 'exit')(1)
else:
    print(x)
