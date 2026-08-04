import ollama

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Read README.md",
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "read_text_file",
                "description": "Read a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "path"
                    ]
                }
            }
        }
    ]
)

print(response)