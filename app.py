import argparse
import tomllib  # Usa tomllib para Python 3.11+, se incluye 'toml' en requirements para compatibilidad
from pathlib import Path

from openai import OpenAI

__all__ = ["get_chat_completion"]


# Conexión al servidor local de Ollama.
# - base_url: Apunta al servidor que Ollama crea por defecto en tu máquina.
# - api_key: Puede ser cualquier valor, 'ollama' es una convención común.
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',
)


# Carga el archivo de configuración settings.toml
# Este archivo es crucial para definir los prompts y el comportamiento del modelo.
try:
    settings_path = Path("settings.toml")
    with settings_path.open("rb") as settings_file:
        SETTINGS = tomllib.load(settings_file)
except FileNotFoundError:
    print("Error: El archivo 'settings.toml' no se encontró. Asegúrate de que exista en el mismo directorio.")
    exit()


def parse_args() -> argparse.Namespace:
    """Parsea los argumentos de la línea de comandos (el archivo de entrada)."""
    parser = argparse.ArgumentParser(
        description="Procesa una consulta de cliente usando un LLM local con Ollama."
    )
    parser.add_argument("file_path", type=Path, help="Ruta al archivo .txt que contiene la consulta del cliente.")
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    """Función principal del script."""
    try:
        file_content = args.file_path.read_text("utf-8")
        print("--- Consulta del Cliente ---")
        print(file_content)
        print("\n--- Respuesta de EcoAsistente ---")
        
        # Llama a la función que se comunica con el LLM
        response = get_chat_completion(file_content)
        print(response)

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{args.file_path}' no fue encontrado.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        print("\nAsegúrate de que Ollama se esté ejecutando y que el modelo especificado en settings.toml esté descargado.")


def get_chat_completion(content: str) -> str:
    """Envía la solicitud al endpoint de chat compatible con OpenAI (en este caso, Ollama)."""
    
    # Asegúrate de que el nombre del modelo en 'settings.toml' coincida
    # con el modelo que descargaste con Ollama (ej: "llama3").
    model_name = SETTINGS["general"]["model"]
    
    response = client.chat.completions.create(
        model=model_name,
        messages=_assemble_chat_messages(content),
        temperature=SETTINGS["general"]["temperature"],
        # El parámetro 'seed' puede no ser compatible con todos los modelos de Ollama.
        # Se mantiene por compatibilidad con la estructura original.
    )
    return response.choices[0].message.content


def _assemble_chat_messages(content: str) -> list[dict]:
    """
    Combina los prompts de 'settings.toml' con el contenido del archivo de entrada
    para crear la lista de mensajes que se enviará al modelo.
    
    Esta estructura permite aplicar técnicas como Few-Shot-Prompting,
    definiendo ejemplos directamente en tu archivo de configuración.
    """
    # La estructura de mensajes puede ser tan simple o compleja como necesites.
    # Para el caso de EcoMarket, una estructura simple puede ser suficiente.
    # Ejemplo simple:
    messages = [
        {"role": "system", "content": SETTINGS["prompts"]["role_prompt"]},
        {"role": "user", "content": SETTINGS["prompts"].get("instruction_prompt", "")},
        {"role": "user", "content": f"Aquí está la consulta del cliente:\n\n---\n{content}\n---"}
    ]
    
    """
    messages = [
        {"role": "system", "content": SETTINGS["prompts"]["role_prompt"]},
        {"role": "user", "content": SETTINGS["prompts"]["negative_example"]},
        {"role": "system", "content": SETTINGS["prompts"]["negative_reasoning"]},
        {"role": "assistant", "content": SETTINGS["prompts"]["negative_output"]},
        {"role": "user", "content": SETTINGS["prompts"]["positive_example"]},
        {"role": "system", "content": SETTINGS["prompts"]["positive_reasoning"]},
        {"role": "assistant", "content": SETTINGS["prompts"]["positive_output"]},
        {"role": "user", "content": f">>>>>\n{content}\n<<<<<"},
        {"role": "user", "content": SETTINGS["prompts"]["instruction_prompt"]},
    ]
    """
    return messages


if __name__ == "__main__":
    main(parse_args())