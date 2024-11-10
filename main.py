from pathlib import Path
import sys

class Plox:
    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            Plox.run_file(sys.argv[1])
            print("Run file")
        else:
            print("REPL")

    @staticmethod
    def run_file(file_path):
        path = Path(file_path)
        data = path.read_bytes()


        Plox.run(data)

    @staticmethod
    def run(source):
        tokens = source # Prints out numbers.

        for token in tokens:
            print(token)

if __name__ == "__main__":
   Plox.main()
