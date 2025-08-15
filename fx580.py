import math

# Allowed names from math module for safe evaluation
ALLOWED_NAMES = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
ALLOWED_NAMES.update({"pi": math.pi, "e": math.e})


def evaluate(expr: str) -> float:
    """Evaluate a mathematical expression using allowed math functions."""
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"Use of {name} not allowed")
    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)


def main() -> None:
    """Simple REPL for the fx580 calculator."""
    print("Casio fx-580 calculator (simple emulator)")
    while True:
        expr = input("Enter expression (or 'quit'): ")
        if expr.strip().lower() in {"quit", "exit"}:
            break
        try:
            result = evaluate(expr)
            print(result)
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
