import json
import requests
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

chat_url = f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/chat/completions?api-version=2024-08-01-preview"

with open("scripts.json") as f:
    scripts = json.load(f)

scripts_summary = "\n".join([f" - {key}: {info['description']}" for key, info in scripts.items()])

def run_script(script_key, *args):
    script_info = scripts.get(script_key)
    if script_info:
        script_name = script_info["script_name"]
        prefixed_args = []
        for i, arg in enumerate(args):
            arg_name = f"--{script_info['args'][i]}"
            prefixed_args.extend([arg_name, arg])

        try:
            result = subprocess.run(['python', script_name] + prefixed_args, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error al ejecutar {script_name}: {result.stderr}"
        except Exception as e:
            return f"Error al intentar ejecutar el script: {str(e)}"
    else:
        return f"Script '{script_key}' no encontrado en la lista de scripts disponibles."

def send_chat_request(user_input):
    headers = {
        "api-key": azure_oai_key,
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": f"""Eres un asistente que interpreta comandos de usuario. Dispones de los siguientes scripts:\n{scripts_summary}\n
                Si el usuario solicita ejecutar un script específico, responde en formato JSON exacto con las siguientes claves:
                {{
                    "execute_script": true,
                    "script_key": "<nombre_del_script>",
                    "args": ["<argumento1>", "<argumento2>", ...]
                }}
                No incluyas otras palabras ni respuestas adicionales.
                """
            },
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    response = requests.post(chat_url, headers=headers, json=data)

    if response.status_code == 200:
        message = response.json()['choices'][0]['message']['content']
        
        try:
            parsed_message = json.loads(message)
            if parsed_message.get("execute_script"):
                script_key = parsed_message.get("script_key")
                args = parsed_message.get("args", [])
                if all(args):
                    return run_script(script_key, *args)
                else:
                    return "Error: uno o más argumentos están vacíos."
            else:
                return message
        except json.JSONDecodeError:
            return message  

    else:
        return f"Error en la solicitud al modelo: {response.status_code} - {response.json()}"
    
def main():
    user_input = input("Consulta: ")
    response_content = send_chat_request(user_input)
    print (response_content)

if __name__ == '__main__':
    main()
        