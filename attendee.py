from datetime import date


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

    def __str__(self):
        """Return the attendee information as text."""

        attendee_details = (
            "Attendee ID: " + str(self._attendee_id) + "\n"
            + "Name: " + self.name + "\n"
            + "Email: " + self.email
        )

        return attendee_details


class Booking:
    """Stores one booking for an attendee and an event."""

    def __init__(self, booking_id, attendee, event, booking_date):
        """Create a booking and check its details."""

        self._booking_id = booking_id
        self._attendee = attendee
        self._event = event
        self._booking_date = booking_date
        self.cancelled = False

        if attendee is None:
            print("Error: You must provide an attendee.")
        elif event is None:
            print("Error: You must provide an event.")
        elif booking_date > date.today():
            print("Error: The booking date cannot be in the future.")

    def change_attendee(self, new_attendee):
        """Change the attendee if a new attendee was provided."""

        if new_attendee is None:
            print("No attendee was provided.")
            return False
        else:
            self._attendee = new_attendee
            return True

    def cancel(self):
        """Mark the booking as canceled."""

        self.cancelled = True

    def get_cancelled(self):
        """Return whether the booking is canceled."""

        return self.cancelled

    def __str__(self):
        """Return the booking information as text."""

        if self.cancelled:
            status = "Cancelled"
        else:
            status = "Active"

        booking_details = (
            "Booking ID: " + str(self._booking_id) + "\n"
            + "Attendee: " + str(self._attendee) + "\n"
            + "Event: " + str(self._event) + "\n"
            + "Booking date: " + str(self._booking_date) + "\n"
            + "Status: " + status
        )

        return booking_details