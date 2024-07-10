import requests

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 404  # True if username is available, False otherwise

def read_usernames_from_file(filename):
    with open(filename, 'r') as file:
        usernames = file.read().splitlines()
    return usernames

def write_available_usernames_to_file(usernames, filename):
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(f"{username}\n")

def main():
    input_filename = "usernames.txt"  # Name of your input file
    output_filename = "available_usernames.txt"  # Name of your output file
    usernames_to_check = read_usernames_from_file(input_filename)

    available_usernames = []
    for username in usernames_to_check:
        if check_username(username):
            print(f"The username '{username}' is available.")
            available_usernames.append(username)
        else:
            print(f"The username '{username}' is taken.")

    write_available_usernames_to_file(available_usernames, output_filename)
    print(f"Available usernames have been saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
