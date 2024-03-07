# input the email address
email = input("Enter the emailaddress: ")

# Extract the domain name 
domain = email.split('@')[-1]

# print the domain name
print("Domain name:",domain)
