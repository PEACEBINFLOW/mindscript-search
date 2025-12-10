class LocalVectorAdapter:
    def embed(self, text):
        return [hash(text) % 1000] * 64
