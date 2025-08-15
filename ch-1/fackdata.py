from faker import Faker # fake data gerat using python librery
import random

fake = Faker()

users = []

for _ in range(20):  # Generate 20 users
    user = {
        'id': fake.name(),
        'email': fake.unique.email(),
        'gender': random.choice(['male', 'female', 'other']),
        'date_of_birth': fake.date_of_birth(minimum_age=20, maximum_age=40).isoformat(),
        'salary': round(random.uniform(40000, 70000), 2),
        'password': fake.password(),
    }
    users.append(user)

# Print the list
for user in users:
    print(user)
