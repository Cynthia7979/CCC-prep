import sys, os
import re
import subprocess


YEAR = 2020
LEVEL = 'j'
FILE = 'j3'


def name(filename):
    return re.search('^.*\.', filename).group(0)


def suffix(filename):
    try:
        return re.search('\.(in|out)$', filename).group(0)
    except AttributeError:
        raise ValueError('File extension of neither in nor out: '+filename)


def main():
    test_data_in = {}
    test_data_out = {}
    data_path = f'./{YEAR}/all_data/{"junior_data" if LEVEL == "j" else "senior_data"}/{FILE.lower()}/'
    code_path = f'./{YEAR}/{FILE}.py'
    for root, dirs, files in os.walk(data_path):
        for f in files:
            try:
                suf = suffix(f)
                if suf == '.in':
                    test_data_in[name(f)] = f
                elif suf == '.out':
                    test_data_out[name(f)] = f
            except ValueError:
                print(f'[NO SUFFIX] {f}')
    print('Files loaded.')

    for test_case in test_data_in.keys():
        try:
            with open(os.path.join(data_path, test_data_in[test_case])) as stdin:
                output = str(subprocess.run(
                    f'python {code_path}',
                    stdin=stdin,
                    capture_output=True
                ).stdout)
                output = output.strip("b").strip("'").replace('\\r\\n', '\n')
                if output.endswith('\n'): output = output[:-1]
            with open(os.path.join(data_path, test_data_out[test_case])) as outfile:
                supposed_output = outfile.read()
                if output == supposed_output:
                    print(f'[OK] {test_case}')
                else:
                    print(f'[ISSUE] {test_case}: \n{supposed_output}\n---------\n{output}')
        except KeyError:
            print(f'[KEYERROR] {test_case}')


if __name__ == '__main__':
    main()
