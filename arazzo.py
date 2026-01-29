import argparse


def main():
    parser = argparse.ArgumentParser(description="Arazzo, a wallpaper generator")
    parser.add_argument("--mode", help="Your name", default="ascii")
    args = parser.parse_args()
    print(f"Mode selected: {args.mode}")


if __name__ == "__main__":
    main()
