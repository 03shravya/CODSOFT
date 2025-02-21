import random
import string
import time


def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generate a strong random password with customization options."""
    if length < 4:
        print("⚠️ Password length should be at least 4 characters for security!")
        return None

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password


def get_user_preferences():
    """Get user preferences for password generation."""
    try:
        print("✨ Let's craft a powerful password for you! ✨")
        time.sleep(1)
        length = int(input("📏 Enter desired password length (minimum 4): "))
        use_digits = input("🔢 Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("🔣 Include special characters? (y/n): ").strip().lower() == 'y'
        return length, use_digits, use_special_chars
    except ValueError:
        print("❌ Oops! That doesn't look like a number. Try again!")
        return None, None, None


def display_loading():
    """Simulate a fun loading animation."""
    print("⏳ Generating your secure password...", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✅")


if __name__ == "__main__":
    print("🔐 Welcome to the Ultimate Password Generator! 🔐")
    length, use_digits, use_special_chars = get_user_preferences()
    if length:
        display_loading()
        new_password = generate_password(length, use_digits, use_special_chars)
        if new_password:
            print(f"🎉 Your ultra-secure password: \033[1;32m{new_password}\033[0m")
            print("🔒 Keep it safe and secure!")


