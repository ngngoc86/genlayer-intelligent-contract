import os
from genlayer import gl

CONTRACT_ADDRESS = os.getenv("GENLAYER_CONTRACT_ADDRESS", "0x0000000000000000000000000000000000000000")

def run_dapp_lifecycle():
    print(f"Connecting to GenLayer Contract at: {CONTRACT_ADDRESS}")
    
    # 1. Gọi giao dịch write (process)
    test_url = "https://example.com"
    test_prompt = "Summarize content"
    print(f"Submitting transaction 'process' with URL: {test_url}")
    tx_result = gl.call_contract(CONTRACT_ADDRESS, "process", [test_url, test_prompt])
    print(f"Transaction execution result: {tx_result}")
    
    # 2. Gọi giao dịch read (get_result)
    print("Reading contract state via 'get_result'...")
    current_state = gl.call_contract(CONTRACT_ADDRESS, "get_result", [])
    print(f"Current contract state: {current_state}")

if __name__ == "__main__":
    run_dapp_lifecycle()
