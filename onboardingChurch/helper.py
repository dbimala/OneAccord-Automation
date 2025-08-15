import random
import string
from faker import Faker


def selectRandom(options):
    total_options = len(options)
    random_index = random.randint(0, total_options - 1)
    options[random_index].click()


def generate_random_church_name():
    adjectives = ["Grace", "Holy", "Living", "Peaceful", "Faithful", "New", "Evergreen", "Hopeful"]
    nouns = ["Hope", "Faith", "Spirit", "Light", "Promise", "Mission", "Community", "Joy"]
    church_types = ["Church", "Chapel", "Ministry", "Fellowship", "Assembly"]

    # Pick one from each category randomly
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    ctype = random.choice(church_types)

    # Add a random 2-digit number to make it unique
    unique_number = ''.join(random.choices(string.digits, k=2))

    # Combine to form the church name
    church_name = f"{adj} {noun} {ctype} {unique_number}"
    return church_name

fake = Faker()
def generate_random_user(random_details):
    firstname = fake.first_name()
    lastname = fake.last_name()
    number = random.randint(1, 9999)
    email = f"{firstname.lower()}.{lastname.lower()}{number}@yopmail.com"
    return firstname, lastname, email


