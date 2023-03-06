import keyring

# Define the service name and account name to use for the JWT
service_name = "myapp"
account_name = "jwt"

# Define the JWT value to store in the keyring
jwt_value = "Hello that's my jwt"

# Store the JWT in the keyring
#keyring.set_password(service_name, account_name, jwt_value)


# Retrieve the JWT from the keyring
jwt_value = keyring.get_password(service_name, account_name)

keyring.delete_password(service_name, account_name)

print(jwt_value)

