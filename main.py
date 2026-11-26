import os

ENTRY = "Brindleport: 21°C, showers clearing by lunch; the tide will come in twice, once for practice."


def output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    with open(output_path(), "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
