from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()



master_pass = input("What is the master password: ")
key = load_key() + master_pass.bytes
fer = Fernet(key=key)

def view():
    with open("Password.txt", mode="r") as f:
        for line in f.readlines():  # noqa: FURB129
            data = line.rstrip()
            user, pass_ = data.split("|")

            print(f"Username: {user}, Password: {pass_}")


def new():
    user_name = input("Enter Username: ")
    password = input("Enter password: ")

    with open("Password.txt", mode="a") as f:
        f.write(user_name + "|" + password + "\n")


while True:
    mode = input('View or new?("q" for exit): ').lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "new":
        new()
    else:
        print("Invalid Choice!")
        continue
