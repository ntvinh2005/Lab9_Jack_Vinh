from encoder import Encoder

def main():
    while True:
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")    
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            Encoder.encode(password)
        elif choice == "3":
            break

if __name__ == "__main__":
    main() 