# Automation Framework [![Build Status](https://travis-ci.com/ortsevlised/python_behave_tests.svg?token=x5Quo4yeKYWSC7Yayepw&branch=main)](https://travis-ci.com/github/ortsevlised/python_behave_tests/)

### This is a proof of concept for Table.co using a BDD approach with the following tools:

- Selenium for UI tests.
- Behave for BDD.
- Selenoid to run the test remotely.
- Allure to generate rich reports.
- Docker to spin up Selenoid and Allure instances.

### Test are defined in the features files using the Gherkin syntax:

`'Given, When, Then'`

- It uses **Travis-CI** for continuous testing, triggering a new test execution after each commit pushed.


- By default, tests run remotely on a **Selenoid** instance. However, it can be set up to run locally depending on the
  arguments passed to the runner, have a look at the `environment.py` file for the options available.


- Reports are generated and sent to an **Allure** server, `docker-compose.yml` is on the project root if you want to
  start the server locally.


- There's a `runner.py` script that can be used to execute the tests.

  You can pass the following arguments:

  `'--test_dir'` Location of test files

  `'--behave_options'` String of behave options. For Example if you want to run test by tags like '-t tag_name'

### URLs

| Service       | URL      |
| ---------- | -------- |
| Reports    | https://orange-snail-57.loca.lt |
| Selenoid UI| https://lovely-deer-85.loca.lt  |

### Todo:
- Add more tests
- Add DB integration
- Mocks
- Choose a good Selenium wrapper and add it


