import sys, os
import re
import subprocess


YEAR = 2019
LEVEL = 'j'
FILE = 'J5'


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
    data_path = f'./{YEAR}/all_data/{"junior_data" if LEVEL == "j" else "senior_data"}/{FILE.lower()}/'  # For 2020
    if not os.path.exists(data_path):
        data_path = f'./{YEAR}/all_data/{FILE.lower()}/'  # 2019,
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

    passed = 0
    total = 0

    for test_case in test_data_in.keys():
        try:
            with open(os.path.join(data_path, test_data_in[test_case])) as stdin:
                output = str(subprocess.check_output(
                    f'python {code_path}',
                    stdin=stdin
                ))
                output = output.strip("b").strip("'").replace('\\r\\n', '\n')
                if output.endswith('\n'): output = output[:-1]
            with open(os.path.join(data_path, test_data_out[test_case])) as outfile:
                supposed_output = outfile.read()
                if supposed_output.endswith('\n'): supposed_output = supposed_output[:-1]
                total += 1
                if output == supposed_output:
                    print(f'[OK] {test_case}')
                    passed += 1
                else:
                    print(f'[ISSUE] {test_case}: \nSupposed: {supposed_output}\n---------\nGot: {output}')
        except KeyError:
            print(f'[KEYERROR] {test_case}')
    print(f"""
---------
Passed: {passed} ({round((passed/total)*100, 2)}%)
Not Passed: {total-passed} ({round(((total-passed)/total)*100, 2)}%)
Total: {total}""")


if __name__ == '__main__':
    main()
