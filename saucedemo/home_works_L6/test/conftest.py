def pytest_configure(config):
    # Actions to perform at the start of the test session
    print(f"\nStarting Pytest Testing Session...\n")

def pytest_runtest_setup(item):
    # Actions to perform before each test function
    print(f"")

def pytest_runtest_teardown(item, nextitem):
    # Actions to perform after each test function
    if nextitem:
        print(f"")