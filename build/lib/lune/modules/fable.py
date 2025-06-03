import random
from rich import print
from rich.table import Table
from faker import Faker

fake = Faker()

def run():
    print("[bold magenta]🧙 FABLE — Synthetic Identity & Persona Fabricator[/bold magenta]")

    num = input("[cyan]Number of personas to generate (default 1): [/cyan]").strip()
    try:
        count = max(1, int(num))
    except:
        count = 1

    print()
    for _ in range(count):
        persona = {
            "Name": fake.name(),
            "Email": fake.email(),
            "Phone": fake.phone_number(),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "SSN": fake.ssn(),
            "Username": fake.user_name(),
            "DOB": fake.date_of_birth(minimum_age=21, maximum_age=55),
            "Location": f"{fake.city()}, {fake.country()}"
        }

        table = Table(title="Fake Persona", header_style="bold green")
        for key, val in persona.items():
            table.add_row(key, str(val))

        print(table)
        print()

def main(args=None):
    print("[fable] Generating synthetic persona (stub)...")

if __name__ == "__main__":
    main()
