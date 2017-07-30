import operator

from src.customer import Customer
from src.gcd import GCD
from src.item_reader import file_line_stream


def find_nearby_customers(customers, base_lat, base_lon, distance):
    """
    finds customers who is within the distance to base latitude and longitude

    :param customers: list of customer objects
    :param base_lat:  float
    :param base_lon: float
    :param distance: float in meters
    :return: generator of nearby customers
    """
    gcd = GCD()
    gcd.set_base(base_lat, base_lon)

    for customer in customers:
        if gcd.is_nearby(customer.lat, customer.lon, distance):
            yield customer


def create_invitations(customer_file_path, base_lat, base_lon, distance):
    lines = file_line_stream(customer_file_path)
    customers = (Customer(i) for i in lines)
    customers = find_nearby_customers(
        customers, base_lat, base_lon, distance)
    return sorted(customers, key=operator.attrgetter("customer_id"), reverse=True)


