import random

def generate_product_number():
    return random.randint(10000, 99999)

def generate_upc(company_prefix, product_number):
    # Ensure the company prefix and product number have the correct lengths
    company_prefix = str(company_prefix).zfill(6)[:6]
    product_number = str(product_number).zfill(5)[:5]

    # Concatenate the company prefix and product number
    upc_without_check_digit = company_prefix + product_number

    # Calculate the check digit
    total = sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(upc_without_check_digit))
    check_digit = (10 - (total % 10)) % 10

    # Concatenate the check digit to the UPC
    upc = upc_without_check_digit + str(check_digit)

    return upc