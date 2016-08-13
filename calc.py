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
_ = getattr


def main(expr):
    popen = _(subprocess, 'Popen')
    p = popen(['python3', '-c', _('print({})', 'format')(expr)],
              stdout=_(subprocess, 'PIPE'))
    result, __ = _(p, 'communicate')()
    return _(_(result, 'decode')('utf-8'), 'strip')()


x = main(_(sys, 'argv')[1])
try:
    float(x)
except ValueError:
    _(sys, 'exit')(1)
else:
    print(x)
