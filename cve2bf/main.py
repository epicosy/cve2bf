import argparse


def main():
    print("Hello, World!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for converting CVE reports to Bugs Framework specifications.')
    subparsers = parser.add_subparsers(dest='subparser')
    collect_parser = subparsers.add_parser('collect')

    args = parser.parse_args()

    main()
