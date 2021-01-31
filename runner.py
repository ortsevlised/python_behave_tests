import argparse
import os
import pathlib
import platform
import subprocess


def add_drivers_to_path():
    print("Adding web drivers to path.")
    curr_file_path = pathlib.Path(__file__).parent.absolute()

    if platform.system() == 'Darwin':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'mac')
    elif platform.system() == 'Windows':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'wimdows')
    elif platform.system() == 'Linux':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'linux')
    else:
        raise Exception("Unknown platform. Unable to add webdrivers to path.")

    current_path = os.environ.get('PATH')
    new_path = webdriver_path + ':' + current_path
    os.environ['PATH'] = new_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=True, help="Location of test file.")
    parser.add_argument('--behave_options', type=str, required=False,
                        help="String of behave options. For Example tags like '-t <tag name>'")

    args = parser.parse_args()
    test_dir = args.test_dir
    behave_options = '' if not args.behave_options else args.behave_options

    command = f'behave -k --no-capture -f allure_behave.formatter:AllureFormatter ' \
              f'-o %allure_result_folder% "{test_dir}"' \
              f'{behave_options} '

print(f"Running command: {command}")

rs = subprocess.run(command, shell=True)
