import os
import sys


def gen_pyside2(ui_dir):
    names = os.listdir(ui_dir)

    for name in names:
        if name.endswith('.py'):
            os.remove(f'{ui_dir}/{name}')

    for name in names:
        if name.endswith(".ui"):
            cmd = f'pyside2-uic {ui_dir}/{name} -o {ui_dir}/{name[0:-3]}.py'
            print(f'cmd = {cmd}')
            os.system(cmd)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('no dir')
        exit(1)

    print(f'dir = {sys.argv[1]}')
    gen_pyside2(sys.argv[1])
