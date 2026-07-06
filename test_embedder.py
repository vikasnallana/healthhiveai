from utils.password_utils import (
    hash_password,
    verify_password,
)

password = "vikas@123"

hashed = hash_password(password)

print("Hash:")
print(hashed)

print()

print("Correct Password:")
print(
    verify_password(
        "vikas@123",
        hashed,
    )
)

print()

print("Wrong Password:")
print(
    verify_password(
        "hello",
        hashed,
    )
)