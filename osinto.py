from modules import find_email
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--email", help="Gathering information of spicific email address.")
args = parser.parse_args()


if args.email:
    email_addr = args.email
    find_email.getData(email_addr)
    exit()
