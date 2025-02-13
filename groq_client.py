import os
import groq
from dotenv import load_dotenv

load_dotenv()


class GroqClient:
    def __init__(self):
        self.client = groq.Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )

    def get_response(self, prompt, expertise, system_prompt=None, model="llama3-70b-8192"):
        try:
            full_system_prompt = f"""
            {system_prompt}
            {self._get_style_instructions(expertise)}
            """

            messages = [
                {"role": "system", "content": full_system_prompt},
                {"role": "user", "content": prompt}
            ]

            params = {
                "temperature": 0.3 if expertise == "Technical" else 0.7,
                "max_tokens": 1024,
                "top_p": 0.9 if expertise == "Technical" else 1.0
            }

            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=model,
                **params
            )
            return chat_completion.choices[0].message.content

        except Exception as e:
            return f"🚨 Error: {str(e)}. Please try again."

    def _get_style_instructions(self, expertise):
        if expertise == "Technical":
            return """
            Response must include:
            - Technical specifications in tables
            - Efficiency metrics (e.g., 22% efficiency)
            - Industry standards (IEC/NEC codes)
            - Comparative analysis
            """
        else:
            return """
            Response must:
            - Use simple language with emojis (⭐, 💡)
            - Include cost examples (e.g., $15k system)
            - Provide practical analogies
            - Avoid technical jargon
            """