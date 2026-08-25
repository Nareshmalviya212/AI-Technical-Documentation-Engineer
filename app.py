import streamlit as st

from src.rag_pipeline import RAGPipeline


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Technical Documentation Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.caption("🚀 CI/CD Deployment v1.0")


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666;
        margin-bottom: 25px;
    }

    .source-card {
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# RAG PIPELINE
# ============================================================

@st.cache_resource
def load_rag_pipeline():

    return RAGPipeline()


try:

    rag = load_rag_pipeline()

except Exception as e:

    st.error("Failed to initialize the RAG pipeline.")

    st.exception(e)

    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("⚙️ System Information")

    st.markdown("---")

    st.subheader("📚 Knowledge Base")

    st.write("FastAPI Technical Documentation")

    st.markdown("---")

    st.subheader("🧠 AI Components")

    st.write("**LLM:** Groq")
    st.write("**Embedding:** BGE")
    st.write("**Vector DB:** FAISS")
    st.write("**Framework:** LangChain")

    st.markdown("---")

    st.subheader("🔎 Retrieval")

    st.write("**Search:** Semantic Search")
    st.write("**Top-K:** 3")
    st.write("**Threshold:** 0.60")

    st.markdown("---")

    st.subheader("📄 Dataset")

    st.write("Technical documentation")
    st.write("Format: Markdown")

    st.markdown("---")

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🤖 AI Technical Documentation Engineer'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about the technical documentation '
    'using Retrieval-Augmented Generation (RAG).'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

if not st.session_state.messages:

    st.info(
        "💡 Try asking: "
        "**How does dependency injection work in FastAPI?**"
    )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Display sources for assistant messages
        if (
            message["role"] == "assistant"
            and message.get("sources")
        ):

            st.markdown("---")

            st.markdown("### 📚 Sources")

            for i, source in enumerate(
                message["sources"],
                start=1
            ):

                with st.expander(
                    f"Source {i}: {source['filename']}"
                ):

                    st.write(
                        f"**Source:** "
                        f"{source['source_name']}"
                    )

                    st.write(
                        f"**Topic:** "
                        f"{source['topic']}"
                    )

                    st.write(
                        f"**Category:** "
                        f"{source['category']}"
                    )

                    st.write(
                        f"**Similarity:** "
                        f"{source['score']:.4f}"
                    )

                    st.write(
                        f"**Documentation:** "
                        f"{source['source_url']}"
                    )


# ============================================================
# USER INPUT
# ============================================================

question = st.chat_input(
    "Ask a technical documentation question..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner(
            "🔎 Searching documentation and generating answer..."
        ):

            try:

                result = rag.ask(question)

                answer = result["answer"]
                sources = result["sources"]

                # Display answer
                st.markdown(answer)

                # Display sources
                if sources:

                    st.markdown("---")

                    st.markdown("### 📚 Sources")

                    for i, source in enumerate(
                        sources,
                        start=1
                    ):

                        with st.expander(
                            f"Source {i}: {source['filename']}"
                        ):

                            st.write(
                                f"**Source:** "
                                f"{source['source_name']}"
                            )

                            st.write(
                                f"**Topic:** "
                                f"{source['topic']}"
                            )

                            st.write(
                                f"**Category:** "
                                f"{source['category']}"
                            )

                            st.write(
                                f"**Similarity:** "
                                f"{source['score']:.4f}"
                            )

                            st.write(
                                f"**Documentation:** "
                                f"{source['source_url']}"
                            )

                else:

                    st.info(
                        "📭 No relevant documentation "
                        "was found for this question."
                    )

                # Save assistant message
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong "
                    "while processing your question."
                )

                st.error(error_message)

                st.exception(e)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "sources": []
                    }
                )