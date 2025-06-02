# ShadowPass: A Themed Password Generator

## 🐍 shadowpass.py File

# Make a new file named `shadowpass.py`, then paste this Python code inside:


import random
import string

def generate_password(length=12, use_symbols=True, theme="default"):
    base = string.ascii_letters + string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if use_symbols:
        base += symbols

    password = ''.join(random.choice(base) for _ in range(length))

    if theme == "matrix":
        return f"💚☠️ {password} ☠️💚"
    elif theme == "cyberpunk":
        return f"⚡[CYPHER]→ {password} ←[NEON]⚡"
    elif theme == "memelord":
        return f"😂🔥P@ssw0rd: {password}🔥😂"
    else:
        return password

if __name__ == "__main__":
    print("🛡️ Welcome to ShadowPass 🛡️")
    length = int(input("Enter password length: "))
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    theme = input("Pick a theme (default/matrix/cyberpunk/memelord): ").lower()
    
    print("\nGenerated Password:")
    print(generate_password(length, use_symbols, theme))
