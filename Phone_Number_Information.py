
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

a=input("enter youur phone number : ")
phone_number=phonenumbers.parse(a)

print(geocoder.description_for_number(phone_number,"en"))

print(carrier.name_for_number(phone_number,"en"))





















