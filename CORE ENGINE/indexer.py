class MindScriptIndexer:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store

    def index_document(self, doc_id, text):
        vectors = self.embedder.embed(text)
        self.store.add(doc_id, vectors, text)

    def index_batch(self, docs):
        for doc_id, text in docs.items():
            self.index_document(doc_id, text)
