import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        potential_emails = re.split(r"[,\s]+", self.text)

        valid_emails = [email for email in potential_emails if re.fullmatch(email_regex, email)]

        return sorted(valid_emails)
