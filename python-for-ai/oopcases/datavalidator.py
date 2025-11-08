class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            self.errors.append(f"Invalid email format: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

validator = DataValidator()

emails = ["test@example.com", "mickey-mouse", "user@domain.com"]
processed_emails = [email for email in emails if not validator.validate_email(email)]

ages = [25, -5, 200, 30]
processed_ages = [age for age in ages if not validator.validate_age(age)]

# Print each validation error on a separate line using list comprehension
for error in [print(err) for err in validator.get_errors()]:
    pass
