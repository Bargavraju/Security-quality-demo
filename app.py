import os
secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY not set")
    print("Application running securely")

if __name__ == "__main__":
    main()
