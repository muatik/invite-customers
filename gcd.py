import math


class GCD:
    base_lat, base_lon = None, None

    def __init__(self, r=None):
        self.R = r or 6371000.0

    def calc_distance(self, lat1, lon1, lat2, lon2, round_digits=3):
        """
        calculate distance in meters between two latitude and longitude pairs.

        :param lat1: latitude of first point in float
        :param lon1: longitude of first point in float
        :param lat2: latitude of second point in float
        :param lon2: longitude of second point float
        :return: distance in meters rounded to, as default, 3 digits
        """
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # deltas
        dlat = lat2 - lat1
        dlong = lon2 - lon1

        a = (
            math.pow(math.sin(dlat / 2.0), 2)
            + math.cos(lat1) * math.cos(lat2)
            * math.pow(math.sin(dlong / 2.0), 2))
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = self.R * c

        return round(d, round_digits)

    def set_base(self, lat, lon):
        """
        sets base latitude and longtitude further operations will based on
        :param lat:
        :param lon:
        :return:
        """
        self.base_lat = lat
        self.base_lon = lon

    def distance_to(self, lat, lon):
        """
        calculates distance in meters between given point and base point
        :param lat:
        :param lon:
        :return:
        """
        if not self.base_lat or not self.base_lon:
            raise Exception("you need to set base lat and lon")
        return self.calc_distance(self.base_lat, self.base_lon, lat, lon)

    def is_nearby(self, lat, lon, distance):
        """
        checks whether given point is within the distance to base point
        :param lat:
        :param lon:
        :param distance: meters in float
        :return:
        """
        return self.distance_to(lat, lon) <= distance
