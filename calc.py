import importlib

modules = ['subprocess', 'sys']
subprocess, sys = map(getattr(importlib, 'import_module'), modules)


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
