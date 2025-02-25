import random

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Silly", "Clever", "Mighty", "Swift", "Charming"]
nouns = ["Tiger", "Dragon", "Panda", "Eagle", "Shark", "Lion", "Wolf", "Fox"]

def generate_username(include_numbers=False, include_special_chars=False, length=8):
    # Generate a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine them to form a base username
    username = f"{adjective}{noun}"
    
    # Add numbers if specified
    if include_numbers:
        username += str(random.randint(0, 99))  # Add a random number
    
    # Add special characters if specified
    if include_special_chars:
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
        username += random.choice(special_chars)  # Add a random special character
    
    # Ensure the username does not exceed the specified length
    if len(username) > length:
        username = username[:length]
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(username + '\n')

def main():
    print("Welcome to the Random Username Generator!")
    
    # User preferences
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    length = int(input("Enter the desired length of the username (default is 8): ") or 8)
    
    # Generate usernames based on user preferences
    usernames = []
    for _ in range(10):  # Generate 10 usernames
        username = generate_username(include_numbers, include_special_chars, length)
        usernames.append(username)
    
    # Display generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    # Save to file
    save_to_file = input("\nDo you want to save the usernames to a file? (yes/no): ").strip().lower() == 'yes'
    if save_to_file:
        save_usernames_to_file(usernames)
        print("User names saved to 'usernames.txt'.")

if __name__ == "__main__":
    main()
