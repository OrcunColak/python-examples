def hello_format(name):
    hello_message = "Hello, {}!".format(name)
    print(hello_message)

def hello_fstring(name):
    hello_message = f"Hello, {name}!"
    print(hello_message)

def hello_join(name):
    hello_message = "".join(["Hello, ", name, "!"])
    print(hello_message)

if __name__ == "__main__":
    your_name = "Orcun"
    hello_format(your_name)
    hello_fstring(your_name)
    hello_join(your_name)
