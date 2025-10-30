import hashlib


def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        lines = input_file.readlines()

    with open(output_file_name, "w") as output_file:
        for line in lines:
            name, password_hash = line.strip().split(",")
            for number in range(1, 10000):
                number_str = str(number)
                hashed_number = hashlib.sha256(number_str.encode()).hexdigest()
                if password_hash == hashed_number:
                    output_file.write(f"{name},{number}\n")


# hash_password_hack("input.csv", "output.csv")
