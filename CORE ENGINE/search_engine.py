class MindScriptSearchEngine:
    def __init__(self, store):
        self.store = store

    def search(self, query, top_k=5):
        q_vec = self.store.embedder.embed(query)
        return self.store.query(q_vec, top_k)
