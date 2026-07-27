import streamlit as st

from src.loader import PDFLoader
from src.embeddings import crear_vectorstore
from src.chatbot import preguntar_documento


st.set_page_config(
    page_title="KnowledgeBot RAG",
    page_icon="🚀"
)


st.title(
    "🚀 KnowledgeBot RAG"
)


st.caption(
    "Agente inteligente con arquitectura Retrieval Augmented Generation"
)


st.divider()



archivo = st.file_uploader(
    "📂 Subir fuente de conocimiento",
    type="pdf"
)



if archivo:


    ruta = "data/documento.pdf"


    with open(
        ruta,
        "wb"
    ) as f:

        f.write(
            archivo.getbuffer()
        )


    if st.button(
        "Crear memoria del documento"
    ):


        with st.status(
            "Procesando información..."
        ):


            loader = PDFLoader(
                ruta
            )


            texto = loader.extraer_texto()


            crear_vectorstore(
                texto
            )


        st.success(
            "Base vectorial creada correctamente"
        )



    st.divider()


    st.subheader(
        "Consulta al agente"
    )


    pregunta = st.text_area(
        "Pregunta:"
    )


    if st.button(
        "Enviar consulta"
    ):


        if pregunta:


            respuesta = preguntar_documento(
                pregunta
            )


            st.markdown(
                "### 🤖 Respuesta"
            )


            st.write(
                respuesta
            )