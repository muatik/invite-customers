from src.invitation import create_invitations
import logging

if __name__ == "__main__":
    # The GPS coordinates for our Dublin office are 53.3393, -6.2576841
    logger = logging.getLogger(__name__)

    try:
        invitations = create_invitations(
            customer_file_path="customers.json",
            base_lat=53.3393,
            base_lon=-6.2576841,
            distance=100 * 1000)  # converting 100km into meters
    except FileNotFoundError as e:
        logger.error("customers.json not found")
        raise

    """
    according to the customers in customers.json file, we are going to invite
    Obama, Trudeau and Macron but not Trump.

    Expected output:
    - (id=53, name=Justin Trudeau, lat=53.12893, lon=-6.27699)
    - (id=12, name=H. Obama, lat=52.986375, lon=-6.043701)
    - (id=1, name=Emmanuel Macron, lat=52.52893, lon=-6.27699)

    """
    for customer in invitations:
        print(customer)
