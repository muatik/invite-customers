import json


class Customer:
    customer_id = None
    name = None
    lat = None
    lon = None

    def __init__(self, serialized=None):
        if serialized:
            o = json.loads(serialized)
            self.customer_id = int(o["user_id"])
            self.name = o["name"]
            self.lat = float(o["latitude"])
            self.lon = float(o["longitude"])

    def __str__(self, *args, **kwargs):
        return "(id={customer_id}, name={name}, lat={lat}, lon={lon})"\
            .format(**self.__dict__)
