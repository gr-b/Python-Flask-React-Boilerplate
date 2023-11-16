import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

class OpenAIClient:

    @classmethod
    def single_prompt(cls, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {
                "role": "system",
                "content": prompt,
                }
            ],
            temperature=1,
        )
        return response["choices"][0]["message"]["content"]
    
    @classmethod
    def stream_single_prompt(cls, prompt):
        """
        Returns a generator that yields responses as they come in
        Of the form: choices[0]["delta"]["content"]
        With choices[0]["finish_reason"] == null until 
        the stream is finished, then it is "stop"
        """
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {
                "role": "system",
                "content": prompt,
                }
            ],
            temperature=1,
            stream=True,
        )

        for response in response:
            if response["choices"][0]["finish_reason"] == "stop":
                return
            yield response["choices"][0]["delta"]["content"]