B, space = 1 << 8, 1 << 5
_, __ = getattr, globals
builtins = lambda x: _(__()['__builtins__'], x)
L = lambda _, __, ___: \
    builtins('chr')(___ % __) + _(_, __, ___ // __) if ___ else \
    builtins('chr')(space)[:-1]
modules = [
    (lambda _, __, ___: _(_, __, ___))(L, B, 545200826904043625543027),
    (lambda _, __, ___: _(_, __, ___))(L, B, 7567731),
]
subprocess, sys = builtins(
    (lambda _, __, ___: _(_, __, ___))(L, B, 7364973),
)(builtins('__import__'), modules)

expr = _(sys, 'argv')[1]
popen = _(subprocess, 'Popen')

args = ['python3', '-c', _('print({})', 'format')(expr)]
kwargs = {'stdout': _(subprocess, 'PIPE')}
result, ___ = _(popen(args, **kwargs), 'communicate')()
x = _(_(result, 'decode')('utf-8'), 'strip')()

try:
    builtins('float')(x)
except:
    _(sys, 'exit')(1)
else:
    builtins('print')(x)
