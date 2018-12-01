import modules
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--email", help="Gathering information of spicific email address.")
args = parser.parse_args()


if args.email:
    email_addr = args.email
    getData(email_addr)
    exit()
