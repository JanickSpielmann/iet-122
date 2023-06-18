import re
print("write your eMail")
email = input()
if re.search('(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})', email):
    print("Your email is valid: " + email)
else:
    print("this is not a valid eMail-address: " + email)

print("zip: ")

zip = input()
if re.match('(\d{4})',zip):
    print("This zip is correct " + zip)

url = input()
if re.match('^(https?:\/\/)?[\w\-]+(\.[\w\-]+)+[/#?]?.*$',url):
    print("This url is correct " + url)