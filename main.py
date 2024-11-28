from pathlib import Path
import sys
from scanner import Scanner

class Plox:
    had_error = False 

    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            Plox.run_file(sys.argv[1])
            print("Run file")
        else:
            Plox.run_prompt()
            print("REPL")

    @staticmethod
    def run_file(file_path):
        path = Path(file_path)
        data = path.read_bytes()


        Plox.run(data)
        if Plox.had_error:
            sys.exit(65)

    @staticmethod
    def run_prompt():
        while True:
            line = input("> ")

            if line.lower() == "exit":
                sys.exit(64)
            
            if line.lower() == "error":
                Plox.error(1, "Error Test")

            Plox.run(line)
            Plox.had_error = False

    @staticmethod
    def run(source):
        scanner = Scanner(source, Plox.error)
        tokens = scanner.scan_tokens() 

        for token in tokens:
            print(token)

    @staticmethod
    def error(line,message):
        Plox.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[{line}] Error {where}: {message}")
        Plox.had_error = True

if __name__ == "__main__":
   Plox.main()
