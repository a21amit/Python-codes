import phonenumbers
from phonenumbers import geocoder

phoneNum = phonenumbers.parse("+91____")

print("\nPhone Number Location\n ")
print(geocoder.description_for_number(phoneNum, "en"))
