class Embedder:
    def __init__(self, adapter):
        self.adapter = adapter

    def embed(self, text):
        return self.adapter.embed(text)
