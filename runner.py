import argparse

import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', required=False, help="Browser where the test will run")
    parser.add_argument('--test_dir', required=True, help="Location of test file.")
    parser.add_argument('--behave_options', type=str, required=False,
                        help="String of behave options. For Example tags like '-t <tag name>'")

    args = parser.parse_args()
    browser = args.browser
    test_dir = args.test_dir
    behave_options = '' if not args.behave_options else args.behave_options

    command = f'behave -k --no-capture -f allure_behave.formatter:AllureFormatter ' \
              f'-o allure-results "{test_dir}"' \
              f'{behave_options} ' \
              f'-D browser={browser}'

print(f"Running command: {command}")

rs = subprocess.run(command, shell=True)
