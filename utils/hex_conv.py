# Function to convert 10-digit number to hexadecimal UID
def convert_to_hex(uid_10_digit):
    # Convert the 10-digit number to hexadecimal
    # Removing '0x' prefix from hex representation
    hex_uid = hex(uid_10_digit)[2:]
    # Optionally, pad the hexadecimal UID if it's shorter than expected
    # Assuming 8 characters (32 bits) hexadecimal UID
    hex_uid = hex_uid.zfill(8)

    return hex_uid

# Function to generate little-endian representation


def generate_little_endian(uid_10_digit):
    # Convert the 10-digit number to hexadecimal
    hex_uid = convert_to_hex(uid_10_digit)

    # Convert hexadecimal to big-endian bytes and then reverse it to get little-endian bytes
    big_endian_bytes = bytes.fromhex(hex_uid)
    little_endian_bytes = bytes(reversed(big_endian_bytes))

    # Convert little-endian bytes back to hexadecimal
    little_endian_hex = little_endian_bytes.hex()

    return little_endian_hex


# Example 10-digit number
uid_10_digit = 2093129433

# Get the little-endian representation as hexadecimal
little_endian_hex = generate_little_endian(uid_10_digit)

# Print the result
print("Little-endian representation (in hexadecimal):", little_endian_hex)
