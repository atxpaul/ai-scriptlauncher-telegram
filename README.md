
# AI Script Launcher con OpenAI y Telegram 🤖

Este proyecto muestra cómo automatizar la ejecución de scripts utilizando **OpenAI** y **Telegram**. La integración permite que OpenAI interprete comandos de usuario y lance scripts personalizados en Python. Además, con la integración de Telegram, puedes ejecutar scripts desde cualquier parte con un simple mensaje.

## 📂 Estructura del Proyecto

```plaintext
.
├── scripts/              # Carpeta con los scripts personalizados a ejecutar
├── .gitignore            # Archivos y carpetas excluidos del repositorio
├── assistant.py          # Lógica principal para la interacción con OpenAI
├── scripts.json          # Configuración de los scripts disponibles
├── telegram-bot.py       # Integración con Telegram
```

### Archivos principales:

- **`assistant.py`**: Maneja la interacción con OpenAI para interpretar comandos y ejecutar scripts según lo solicitado.
- **`telegram-bot.py`**: Configura un bot de Telegram para recibir mensajes y ejecutar comandos a través del sistema OpenAI.
- **`scripts.json`**: Define los scripts disponibles, sus descripciones y los argumentos requeridos.
- **`scripts/`**: Carpeta donde puedes agregar tus scripts personalizados para automatizar tareas.

---

## 🚀 Cómo Configurar el Proyecto

### 1. Clona el repositorio:
```bash
git clone https://github.com/atxpaul/ai-scriptlauncher-telegram.git
cd ai-scriptlauncher-telegram
```

### 2. Crea un entorno virtual y activa:
```bash
python -m venv .venv
source .venv/bin/activate   # En Linux/Mac
.venv\Scripts\activate      # En Windows
```

### 3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno:
Crea un archivo `.env` con las siguientes claves:
```env
AZURE_OAI_ENDPOINT=<tu_endpoint_de_openai>
AZURE_OAI_KEY=<tu_clave_de_openai>
AZURE_OAI_DEPLOYMENT=<nombre_del_despliegue_de_openai>
BOT_TOKEN=<token_de_tu_bot_de_telegram>
```

### 5. Configura los scripts en `scripts.json`:
Ejemplo:
```json
{
    "health_check": {
        "script_name": "scripts/health_check.py",
        "description": "Comprueba el estado de un servidor",
        "args": ["names"]
    }
}
```

---

## 🛠 Cómo Usar el Proyecto

### Ejecución con OpenAI:
Ejecuta `assistant.py` y escribe un comando en el terminal. Por ejemplo:
```bash
python assistant.py
```
Consulta de ejemplo:
```
Consulta: Comprobar el estado del servidor server1
```

### Ejecución con Telegram:
1. Configura tu bot en [BotFather](https://telegram.me/BotFather).
2. Ejecuta el bot:
```bash
python telegram-bot.py
```
3. Envía comandos al bot desde Telegram.

---

## 🌟 Funcionalidades Principales

- **Automatización con OpenAI**: Lanza scripts interpretando comandos escritos en lenguaje natural.
- **Control Remoto con Telegram**: Ejecuta scripts desde cualquier lugar a través de mensajes de Telegram.
- **Fácil Configuración de Scripts**: Define nuevos scripts y sus argumentos en `scripts.json`.

---

## 📌 Recursos

- **BotFather para crear tu bot**: [https://telegram.me/BotFather](https://telegram.me/BotFather)
- **Documentación de OpenAI API**: [https://platform.openai.com/docs/](https://platform.openai.com/docs/)

---

## 🤝 Contribuciones

Si tienes ideas o encuentras errores, ¡no dudes en abrir un issue o un pull request! 

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

¡Gracias por visitar este repositorio! 😊
