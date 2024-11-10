import sys
class Plox:
    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            print("Run file")
        else:
            print("REPL")

if __name__ == "__main__":
   Plox.main()
