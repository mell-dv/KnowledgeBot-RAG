# 🚀 KnowledgeBot RAG

Agente inteligente basado en arquitectura **RAG (Retrieval Augmented Generation)** capaz de convertir documentos PDF en una fuente de conocimiento consultable mediante lenguaje natural.

El sistema combina recuperación de información mediante bases vectoriales con generación de respuestas utilizando inteligencia artificial de Cohere.

---

# 🎯 Objetivo

Crear un asistente capaz de responder preguntas sobre documentos utilizando únicamente la información disponible dentro del archivo cargado.

---

# 🚀 Características

- 📄 Lectura y procesamiento de documentos PDF.
- 🧠 Generación de embeddings semánticos.
- 🗂 Almacenamiento vectorial utilizando FAISS.
- 🔎 Recuperación de fragmentos relevantes del documento.
- 🤖 Generación de respuestas mediante Cohere.
- 🌐 Aplicación web desarrollada con Streamlit.
- 📚 Respuestas basadas en el contenido recuperado.

---

# 🏛 Arquitectura RAG

```text
Pregunta del usuario
        |
        ↓
Aplicación Streamlit
        |
        ↓
FAISS Vector Search
        |
        ↓
Contexto relevante
        |
        ↓
Modelo Cohere
        |
        ↓
Respuesta final
```

---

# 🛠 Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje principal |
| Streamlit | Desarrollo de la aplicación web |
| Cohere API | Modelo de inteligencia artificial |
| LangChain | Framework para arquitectura RAG |
| FAISS | Motor de búsqueda vectorial |
| PyPDF | Extracción de información desde PDF |

---

# ⚙ Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto:

```bash
cd KnowledgeBot-RAG
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🔐 Variables de entorno

Crear un archivo:

```text
.env
```

Agregar:

```env
COHERE_API_KEY=tu_api_key
```

---

# ▶ Ejecutar proyecto

Iniciar la aplicación:

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

---

# 💬 Ejemplos

### Pregunta:

```text
¿Cuáles son los puntos principales del documento?
```

### Respuesta:

```text
El agente identifica los fragmentos más importantes y genera una respuesta basada en la información recuperada.
```

---

### Pregunta:

```text
Explica la información encontrada.
```

### Respuesta:

```text
La respuesta se genera mediante recuperación aumentada con generación utilizando el contenido del documento PDF.
```

---

# 📂 Estructura del proyecto

```text
KnowledgeBot-RAG
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
│
├── data
│   └── documento.pdf
│
└── src
    ├── loader.py
    ├── embeddings.py
    └── chatbot.py
```

---

# 👨‍💻 Autor

Proyecto de inteligencia artificial aplicado al procesamiento documental, utilizando recuperación aumentada de información y modelos generativos.