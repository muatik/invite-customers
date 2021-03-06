import operator

from customer import Customer
from gcd import GCD
from item_reader import file_line_stream
import logging

logger = logging.getLogger(__name__)


def find_nearby_customers(customers, gcd, distance):
    """
    finds customers who is within the distance to base latitude and longitude

    :param customers: list of customer objects
    :param gcd:  GCD instance with base lat long initialized
    :param distance: float in meters
    :return: generator of nearby customers
    """

    for customer in customers:
        if gcd.is_nearby(customer.lat, customer.lon, distance):
            yield customer


def convert_to_customers(lines):
    """
    converts the each element of the given iterable to a customer object
    :param lines: list of string json
    :return: generator of customers
    """
    for json_line in lines:
        try:
            yield Customer(json_line)
        except ValueError:
            # there may be an error related to an individual record,
            # that should not affects others. so after logging,
            # it continues with the next line
            logger.error("not valid customer json: " + json_line)


def create_invitations(customer_file_path, base_lat, base_lon, distance):
    """
    Here, customer ingestion pipeline is established.
    By streaming the content of the file, without loading all the content into
    memory, this application can choose who to invite. In other words, only the
    customer line will be loaded into the memory and inserted into the invitation
    list if she or he satisfy the conditions.

    There steps:
    1. customer.json -> a single line -> a customer object -> filtering -> populating invitation list
    2. sorting invitation list
    3. printing invitation list

    """
    gcd = GCD()
    gcd.set_base(base_lat, base_lon)
    lines = file_line_stream(customer_file_path)
    customers = convert_to_customers(lines)  # generator of customer objects)
    customers = find_nearby_customers(
        customers, gcd, distance)  # generator of invitation list

    return sorted(
            set(customers),  # to get rid of duplicate customers
            key=operator.attrgetter("customer_id"),
            reverse=True)

