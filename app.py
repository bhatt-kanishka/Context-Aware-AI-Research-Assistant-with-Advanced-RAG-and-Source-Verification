import streamlit as st
import time


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Document Intelligence Hub",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background: #f6f7f9;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }


    /* ========================================================
       HEADER
       ======================================================== */

    .app-title {
        font-size: 30px;
        font-weight: 750;
        letter-spacing: -0.7px;
        color: #111827;
        margin-bottom: 2px;
    }

    .app-subtitle {
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .system-ready {
        background: #ecfdf3;
        color: #067647;
        border: 1px solid #abefc6;
        padding: 7px 13px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 650;
        display: inline-block;
    }


    /* ========================================================
       DOCUMENT HEADER
       ======================================================== */

    .document-header {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 20px;
    }

    .document-name {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
    }

    .document-meta {
        color: #6b7280;
        font-size: 13px;
        margin-top: 4px;
    }


    /* ========================================================
       CARDS
       ======================================================== */

    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
    }

    .card-title {
        font-size: 17px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }

    .card-description {
        color: #6b7280;
        font-size: 13px;
    }


    /* ========================================================
       INSIGHT CARDS
       ======================================================== */

    .insight-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 18px;
        min-height: 105px;
    }

    .insight-label {
        font-size: 11px;
        font-weight: 650;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: .5px;
    }

    .insight-value {
        font-size: 23px;
        font-weight: 750;
        color: #111827;
        margin-top: 8px;
    }


    /* ========================================================
       SUMMARY
       ======================================================== */

    .summary-text {
        font-size: 15px;
        line-height: 1.75;
        color: #374151;
    }


    /* ========================================================
       HIGHLIGHTS
       ======================================================== */

    .highlight {
        background: #fff1a8;
        padding: 2px 5px;
        border-radius: 4px;
        font-weight: 650;
    }


    /* ========================================================
       VERIFIED BADGE
       ======================================================== */

    .verified {
        background: #ecfdf3;
        border: 1px solid #abefc6;
        color: #067647;
        padding: 10px 14px;
        border-radius: 9px;
        font-size: 13px;
        font-weight: 650;
        margin: 12px 0;
    }

    .not-verified {
        background: #fff7ed;
        border: 1px solid #fed7aa;
        color: #c2410c;
        padding: 10px 14px;
        border-radius: 9px;
        font-size: 13px;
        font-weight: 650;
        margin: 12px 0;
    }


    /* ========================================================
       SOURCE CARDS
       ======================================================== */

    .source-card {
        background: #fafafa;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .source-title {
        font-size: 14px;
        font-weight: 700;
        color: #111827;
    }

    .source-page {
        color: #6b7280;
        font-size: 12px;
        margin-top: 4px;
    }

    .evidence {
        background: white;
        border-left: 3px solid #9ca3af;
        padding: 12px;
        margin-top: 10px;
        color: #4b5563;
        font-size: 13px;
        line-height: 1.6;
    }


    /* ========================================================
       PROCESSING
       ======================================================== */

    .processing-box {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 18px;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }


    /* ========================================================
       CHAT
       ======================================================== */

    .chat-answer {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 20px;
        line-height: 1.7;
        color: #374151;
    }


    /* ========================================================
       SECTION LABEL
       ======================================================== */

    .section-label {
        font-size: 11px;
        color: #6b7280;
        font-weight: 700;
        letter-spacing: .7px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "documents" not in st.session_state:
    st.session_state.documents = []

if "active_document" not in st.session_state:
    st.session_state.active_document = None

if "processed" not in st.session_state:
    st.session_state.processed = False

if "processing" not in st.session_state:
    st.session_state.processing = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sources" not in st.session_state:
    st.session_state.sources = []

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## ◈ Document Hub")

    st.caption("Research & Document Intelligence")

    st.divider()

    st.markdown(
        '<div class="section-label">UPLOAD DOCUMENT</div>',
        unsafe_allow_html=True
    )

    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_files:

        for file in uploaded_files:

            if file.name not in st.session_state.documents:

                st.session_state.documents.append(
                    file.name
                )

        st.session_state.active_document = uploaded_files[0].name

    st.divider()

    # ========================================================
    # DOCUMENT LIST
    # ========================================================

    st.markdown(
        '<div class="section-label">DOCUMENTS</div>',
        unsafe_allow_html=True
    )

    if st.session_state.documents:

        for document in st.session_state.documents:

            selected = (
                document ==
                st.session_state.active_document
            )

            if st.button(
                f"📄 {document}",
                key=f"doc_{document}",
                use_container_width=True
            ):

                st.session_state.active_document = document
                st.session_state.messages = []
                st.rerun()

    else:

        st.caption("No documents uploaded yet.")


    st.divider()

    # ========================================================
    # SEARCH SCOPE
    # ========================================================

    st.markdown(
        '<div class="section-label">SEARCH SCOPE</div>',
        unsafe_allow_html=True
    )

    if len(st.session_state.documents) > 1:

        search_scope = st.radio(
            "Search scope",
            [
                "Search all documents",
                "Selected document only"
            ],
            label_visibility="collapsed"
        )

    else:

        search_scope = "Selected document only"

        st.caption("Only one document available")


# ============================================================
# MAIN HEADER
# ============================================================

header_left, header_right = st.columns([6, 1])

with header_left:

    st.markdown(
        '<div class="app-title">Document Intelligence Hub</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="app-subtitle">
        Understand documents. Ask questions. Verify every answer.
        </div>
        """,
        unsafe_allow_html=True
    )

with header_right:

    st.markdown(
        '<span class="system-ready">● System Ready</span>',
        unsafe_allow_html=True
    )


# ============================================================
# NO DOCUMENT STATE
# ============================================================

if not st.session_state.documents:

    st.markdown("""
    <div class="card">

        <div class="card-title">
        Start with a document
        </div>

        <div class="card-description">
        Upload one or more PDF documents from the sidebar.
        The system will extract, index and analyse their content.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.stop()


# ============================================================
# ACTIVE DOCUMENT HEADER
# ============================================================

active_document = st.session_state.active_document

st.markdown(
    f"""
    <div class="document-header">

        <div class="document-name">
        📄 {active_document}
        </div>

        <div class="document-meta">
        PDF Document
        &nbsp; • &nbsp;
        AI analysis workspace
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROCESS DOCUMENT
# ============================================================

if not st.session_state.processed:

    st.markdown("### Process Document")

    st.info(
        "Your document is uploaded. Process it to generate "
        "the summary, insights and searchable knowledge base."
    )

    if st.button(
        "⚡ Process Document",
        type="primary",
        use_container_width=True
    ):

        st.session_state.processing = True

        progress = st.progress(0)

        status = st.empty()

        processing_steps = [
            ("Uploading document", 15),
            ("Extracting text", 30),
            ("Creating chunks", 50),
            ("Generating embeddings", 70),
            ("Indexing in vector database", 90),
            ("Ready", 100)
        ]

        for step, value in processing_steps:

            status.markdown(
                f"**{step}...**"
            )

            progress.progress(value)

            time.sleep(0.5)

        st.session_state.processing = False
        st.session_state.processed = True

        status.success(
            "Document processing completed successfully."
        )

        time.sleep(0.5)

        st.rerun()


# ============================================================
# WORKSPACE
# ============================================================

if st.session_state.processed:

    summary_tab, ask_tab, sources_tab = st.tabs(
        [
            "📊 Summary",
            "💬 Ask",
            "📚 Sources"
        ]
    )


    # ========================================================
    # SUMMARY TAB
    # ========================================================

    with summary_tab:

        st.markdown("### Document Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.markdown("""
            <div class="insight-card">

                <div class="insight-label">
                Document
                </div>

                <div class="insight-value">
                PDF
                </div>

            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown("""
            <div class="insight-card">

                <div class="insight-label">
                Status
                </div>

                <div class="insight-value">
                Ready
                </div>

            </div>
            """, unsafe_allow_html=True)

        with col3:

            st.markdown("""
            <div class="insight-card">

                <div class="insight-label">
                Search
                </div>

                <div class="insight-value">
                RAG
                </div>

            </div>
            """, unsafe_allow_html=True)

        with col4:

            st.markdown("""
            <div class="insight-card">

                <div class="insight-label">
                Sources
                </div>

                <div class="insight-value">
                Indexed
                </div>

            </div>
            """, unsafe_allow_html=True)


        st.markdown("### Generated Summary")

        st.markdown("""
        <div class="card">

            <div class="summary-text">

            This section will contain the automatically generated
            summary of the uploaded document. The summary will
            be generated from the extracted document content
            rather than from external knowledge.

            </div>

        </div>
        """, unsafe_allow_html=True)


        # ====================================================
        # KEY INSIGHTS
        # ====================================================

        st.markdown("### Key Insights")

        insight1, insight2, insight3 = st.columns(3)

        with insight1:

            st.markdown("""
            <div class="card">

            <strong>📌 Main Topic</strong>

            <p class="card-description">
            Automatically identified from document content.
            </p>

            </div>
            """, unsafe_allow_html=True)

        with insight2:

            st.markdown("""
            <div class="card">

            <strong>📈 Important Findings</strong>

            <p class="card-description">
            Important facts and findings extracted from the document.
            </p>

            </div>
            """, unsafe_allow_html=True)

        with insight3:

            st.markdown("""
            <div class="card">

            <strong>🎯 Key Entities</strong>

            <p class="card-description">
            Important products, people, organisations or concepts.
            </p>

            </div>
            """, unsafe_allow_html=True)


        # ====================================================
        # SUGGESTED QUESTIONS
        # ====================================================

        st.markdown("### Explore This Document")

        st.caption(
            "Suggested questions based on the uploaded document"
        )

        suggested_questions = [
            "What is the main topic of this document?",
            "What are the key findings?",
            "What strategies are discussed?",
            "Which product or entity is most important?",
            "What are the major conclusions?",
            "What important numbers or statistics are mentioned?"
        ]

        for question in suggested_questions:

            if st.button(
                question,
                key=f"suggest_{question}",
                use_container_width=True
            ):

                st.session_state.selected_question = question

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": question
                    }
                )

                # Switch user's attention toward Ask tab
                st.info(
                    "Question selected. Open the Ask tab to continue."
                )


    # ========================================================
    # ASK TAB
    # ========================================================

    with ask_tab:

        st.markdown("### Ask Your Document")

        if search_scope == "Search all documents":

            st.caption(
                "Searching across all uploaded documents"
            )

        else:

            st.caption(
                f"Searching: {active_document}"
            )


        # ----------------------------------------------------
        # CHAT HISTORY
        # ----------------------------------------------------

        for message in st.session_state.messages:

            with st.chat_message(
                message["role"]
            ):

                st.write(
                    message["content"]
                )


                # Show AI answer UI
                if message["role"] == "assistant":

                    st.markdown("""
                    <div class="verified">
                    ✓ Verified from document sources
                    </div>
                    """, unsafe_allow_html=True)


        # ----------------------------------------------------
        # QUESTION INPUT
        # ----------------------------------------------------

        question = st.chat_input(
            "Ask a question about your document..."
        )

        if question:

            # Add user question
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            # Temporary demonstration response
            answer = """
            Based on the uploaded document, the answer will be
            generated here using the RAG retrieval pipeline.

            Important information such as **key numbers,
            dates, products and findings** will be highlighted.
            """

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            # Temporary sources
            st.session_state.sources = [
                {
                    "document": active_document,
                    "page": 4,
                    "text": "Relevant evidence retrieved from the document."
                },
                {
                    "document": active_document,
                    "page": 5,
                    "text": "Additional supporting evidence retrieved from the document."
                }
            ]

            st.rerun()


    # ========================================================
    # SOURCES TAB
    # ========================================================

    with sources_tab:

        st.markdown("### Retrieved Sources")

        st.caption(
            "Document evidence used to support generated answers."
        )

        if not st.session_state.sources:

            st.info(
                "Sources will appear here after you ask a question."
            )

        else:

            for index, source in enumerate(
                st.session_state.sources
            ):

                st.markdown(
                    f"""
                    <div class="source-card">

                        <div class="source-title">
                        📄 {source["document"]}
                        </div>

                        <div class="source-page">
                        Page {source["page"]}
                        </div>

                        <div class="evidence">
                        {source["text"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"View citation {index + 1}",
                    key=f"citation_{index}"
                ):

                    st.session_state.selected_source = source


# ============================================================
# CITATION SIDE PANEL
# ============================================================

if "selected_source" in st.session_state:

    source = st.session_state.selected_source

    with st.sidebar:

        st.divider()

        st.markdown("### 🔎 Citation Evidence")

        st.markdown(
            f"""
            **Document**

            `{source["document"]}`

            **Page**

            `{source["page"]}`

            **Matched Evidence**

            > {source["text"]}
            """
        )

        if st.button(
            "Close Evidence",
            use_container_width=True
        ):

            del st.session_state.selected_source

            st.rerun()