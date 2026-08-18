from genlayer import gl

class IntelligentContract(gl.Contract):
    result: str

    def __init__(self, initial_text: str):
        self.result = initial_text

    @gl.public.write
    def process(self, url: str, prompt: str) -> str:
        web_data = gl.get_webpage(url)
        analysis = gl.exec_prompt(f"Data: {web_data}\nPrompt: {prompt}")
        self.result = analysis
        return analysis

    @gl.public.read
    def get_result(self) -> str:
        return self.result
