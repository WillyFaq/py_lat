from faker import Faker
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Dump Data Generator!!")

print("===================================================")
print(ascii_banner)
print("===================================================")

fake = Faker()
#print(fake.text())
print("Choose to generate : ")
print("\t1) Email")

