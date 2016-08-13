import subprocess
import sys


def main(expr):
    stmt = 'print({})'.format(expr)
    p = subprocess.Popen(['python3', '-c', stmt],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result, _ = p.communicate()
    return result.decode('utf-8').strip()


if __name__ == '__main__':
    x = main(sys.argv[1])
    try:
        float(x)
    except ValueError:
        sys.exit(1)
    else:
        print(x)
