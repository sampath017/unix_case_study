# To generate fake data

import csv
from faker import Faker
import random
import datetime

fake = Faker('en_IN')

vehicle_types = ["2-wheeler", "4-wheeler"]
insurance_types = ["Full Insurance", "Third Party"]

with open('vehicles.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the column headings
    writer.writerow(["Vehicle No", "VehicleType", "CustomerName", "EngineNo", "ChasisNo",
                    "Phone No", "PremiumAmount", "Type", "FromDate", "ToDate", "UnderwriterId"])

    # Generate 10 rows of fake data
    for _ in range(10):
        vehicle_no = fake.random_int(min=1000, max=9999)
        vehicle_type = random.choice(vehicle_types)
        customer_name = fake.name()
        engine_no = f"{random.randint(1000, 9999)}"
        chasis_no = f"{random.randint(1000, 9999)}"
        phone_no = fake.phone_number()
        premium_amount = round(random.uniform(5000, 20000), 2)
        insurance_type = random.choice(insurance_types)
        from_date = fake.date_between(start_date='-1y', end_date='today')
        to_date = from_date + datetime.timedelta(days=random.randint(1, 365))
        underwriter_id = fake.random_int(min=1, max=100)

        # Write the fake data to the CSV file
        writer.writerow([vehicle_no, vehicle_type, customer_name, engine_no, chasis_no,
                        phone_no, premium_amount, insurance_type, from_date, to_date, underwriter_id])

print("Fake data has been generated and saved to 'vehicles.csv'.")
