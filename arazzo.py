import argparse


def main():
    parser = argparse.ArgumentParser(
            description="Arazzo, a wallpaper generator"
            )
    parser.add_argument(
        "filename",
        nargs="?",
        help="Path to the input file (required for ASCII mode)"
    )
    parser.add_argument(
        "--mode",
        choices=["ascii", "geometric"],
        default="ascii",
        help="Creation mode (default: %(default)s)"
    )
    args = parser.parse_args()
    if args.mode == "ascii" and not args.filename:
        parser.error("Input file is required for ASCII mode.")
    if args.filename:
        print(f"Processing file: {args.filename}")
    print(f"Mode: {args.mode}")
    if args.mode == "ascii":
        print(f"Using ASCII mode to process {args.filename}...")
    elif args.mode == "geometric":
        if args.filename:
            print(f"Using geometric mode to process {args.filename}...")
        else:
            print("Using geometric mode (no file needed)...")


if __name__ == "__main__":
    main()
