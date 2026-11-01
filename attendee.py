class Attendee:
    """Stores information about one person attending an event."""

    def __init__(self, attendee_id, name, email):
        """Create an attendee and check the email."""

        self._attendee_id = attendee_id
        self.name = name

        if "@" in email and "." in email:
            self.email = email
        else:
            print("Invalid email address.")
            self.email = ""

    def update_email(self, new_email):
        """Update the email if it looks valid."""

        if "@" in new_email and "." in new_email:
            self.email = new_email
            return True
        else:
            print("Invalid email address. Email was not changed.")
            return False