from genlayer import *

@gl.contract
class DataVerifierContract:
    verified_sources: dict[str, str]

    def __init__(self):
        self.verified_sources = {}

    @gl.public.write
    def verify_authoritative_source(self, source_url: str) -> bool:
        # Step 1: Fetch live web content directly from authoritative source
        web_data = gl.web.get(source_url)
        
        # Step 2: Query LLM engine to perform consensus verification on live data
        prompt = f"Verify whether the following live data from {source_url} is authoritative and accurate: {web_data[:1000]}"
        verification_result = gl.llm.query(prompt)
        
        # Step 3: State transition approved by validators
        if "APPROVED" in verification_result.upper() or "TRUE" in verification_result.upper():
            self.verified_sources[source_url] = "VERIFIED"
            return True
        else:
            self.verified_sources[source_url] = "INVALID"
            return False

    @gl.public.read
    def read_verification_state(self, source_url: str) -> str:
        # Client read path to inspect contract state
        return self.verified_sources.get(source_url, "UNVERIFIED")
