class Venue:

    def __int__(self,venue_id : int ,venue_name: str,capacity:int ):
        """

        :param venue_id:
        :param venue_name:
        :param capacity:
        :return:
        """
        self.venue_id= venue_id
        self.venue_name = venue_name
        self._capacity = capacity






    def get_venue_id(self)-> int:
        """

        :return:
        """
        return self.venue_id

    def get_venue_name(self)-> str:
        """

        :return:
        """

        return self.venue_name

    def get_venue_capacity(self)-> int:
        """

        :return:
        """
        return self._capacity


    def __str__(self) -> str:
        return f"{self.venue_id}  ({self.venue_name}),capacity {self._capacity}"








class Event:

    allowed_events = ["workshop","conference","open day","convention"]


