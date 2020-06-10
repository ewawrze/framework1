# A complete test suite

This is a complete, simple test suite for the Polish version of Zalando webpage `https://www.zalando.pl`.

We're testing logging in to an account. The test suite we've prepared includes making screenshots when a test fails and saving detailed log info. One can choose a browser in which the test shall be held, e.g. `py.test -s -v tests\test_suite_demo.py --browser chrome`. There's no need to provide browser name as the default browser is set to Google Chrome.

The data in a csv file `testdata.csv` shall be changed. Before running the test suite it's recommended that an account was created and the file was filled with the login data. Provide both invalid and valid login details to see the magic of this test suite ;)
