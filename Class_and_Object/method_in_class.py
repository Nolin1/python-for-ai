class Validator:
    def __init__(self):
        self.error = []

    def validate_email(self,email):
        if "@" not in email:
            self.error.append(f"Invalid Email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.error.append(f"Invalid Age: {age}")
            return False
        return True

    def get_error(self):
        return self.error

validator = Validator()

validator.validate_email(email="bad-email")
validator.validate_age(age= 200)

validator.validate_email(email="another-bad-email")
validator.validate_age(age= 150)

validator.validate_email(email="good-email@gmail.com")
validator.validate_age(age= 35)

validator.get_error()