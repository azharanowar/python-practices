def test_function():
    print('Hello from a test function from my module...')


def greet_user(user_name):
    print(f"Hello {user_name.title()}! How are you doing today?")


if __name__ == "__main__":
    test_function()