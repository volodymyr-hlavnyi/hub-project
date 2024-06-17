import unittest

loader = unittest.TestLoader()

suite = loader.discover('unittest', pattern='*_unittest.py')

runner = unittest.TextTestRunner(verbosity=0)

result = runner.run(suite)

for test, reason in result.errors:
    print(f'Error in test {test}: {reason}')

for test, reason in result.skipped:
    print(f'Skipped test {test}'
          f'\n{reason}')