import os

CONTRACT_ADDRESS = os.getenv("GENLAYER_CONTRACT_ADDRESS", "0x0000000000000000000000000000000000000000")

def main():
    print(f"Connecting to GenLayer Contract at: {CONTRACT_ADDRESS}")
    print("Application entry point executed successfully.")

if __name__ == "__main__":
    main()
