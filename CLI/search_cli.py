import argparse

class CLI:
    def __init__(self, search_engine):
        self.engine = search_engine

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("mode")
        parser.add_argument("query")
        args = parser.parse_args()

        if args.mode == "find":
            results = self.engine.search(args.query)
            print(results)
