from transformers import pipeline

class GPTModel:
    def __init__(self, model_name='gpt-3.5-turbo'):
        self.model_name = model_name
        self.text_generator = pipeline('text-generation', model=model_name)

    def generate_response(self, prompt):
        response = self.text_generator(prompt)[0]
        return response['generated_text']

    def get_code_from_prompt(self, prompt):
        code_prompt = f"Python solution:\n{prompt}"
        response = self.generate_response(code_prompt)
        return self.extract_code(response)

    def extract_code(self, text):
        # Simple function to extract code block from text
        start_index = text.find('', start_index + 1)
        
        if start_index != -1 and end_index != -1:
            return text[start_index:end_index].strip()
        return "Code not found."

    def get_explanation(self, prompt):
        response = self.generate_response(prompt)
        return response

# Example usage:
gpt = GPTModel()

# Generate code for a task
code_prompt = "Task: Generate a function to validate a BTC address."
generated_code = gpt.get_code_from_prompt(code_prompt)
print(generated_code)

# Get an explanation for a process
explanation_prompt = "Explain the process of recovering a Bitcoin private key."
explanation = gpt.get_explanation(explanation_prompt)
print(explanation)