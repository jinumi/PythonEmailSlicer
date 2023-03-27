# A python script that can fetch the username and domain name from the email.

# Get the user's email address
email = input("What is your email address :").strip()

# Slice out the username
user_name = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@") + 1:]

# Format Message
res = f"Your username is '{user_name}' and your domain is '{domain_name}'"

# Display the result message
print(res)
