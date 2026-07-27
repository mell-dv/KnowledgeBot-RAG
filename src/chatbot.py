import os

from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_core.prompts import PromptTemplate


load_dotenv()



def obtener_vectorstore():

    modelo_embeddings = CohereEmbeddings(
        model="embed-multilingual-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    vector_db = FAISS.load_local(
        "vectorstore",
        modelo_embeddings,
        allow_dangerous_deserialization=True
    )


    return vector_db



def preguntar_documento(pregunta):

    vector_db = obtener_vectorstore()


    resultados = vector_db.similarity_search_with_score(
        pregunta,
        k=5
    )


    contexto = ""


    for documento, score in resultados:

        contexto += documento.page_content
        contexto += "\n\n"



    prompt = PromptTemplate(
        template="""

Eres KnowledgeBot RAG, un agente experto en recuperación de conocimiento.

Reglas del agente:
- Analiza únicamente el contexto proporcionado.
- Genera respuestas relacionadas con el documento.
- Mantén claridad en la explicación.
- No supongas información que no esté presente.
- Si no encuentras datos suficientes responde:
"No encuentro esa información en el documento."

CONTEXTO RECUPERADO:
{contexto}

PREGUNTA:
{pregunta}

RESPUESTA:
""",
        input_variables=[
            "contexto",
            "pregunta"
        ]
    )


    modelo = ChatCohere(
        model="command-r-plus-08-2024",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    resultado = modelo.invoke(
        prompt.format(
            contexto=contexto,
            pregunta=pregunta
        )
    )


    return resultado.content