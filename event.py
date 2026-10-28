class Venue:

    def __int__(self,venue_id,venue_name,capacity):
        self.venue_id= venue_id
        self.venue_name = venue_name
        self._capacity = capacity

    def __str__(self) -> str:
        return f"{self.venue_id}  ({self.venue_name}),capacity {self._capacity}"

class Event:
