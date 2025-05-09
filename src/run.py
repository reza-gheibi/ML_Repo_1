import argparse
from train import train_model

def main():
    parser = argparse.ArgumentParser(description="Train ML model")
    parser.add_argument("--data", type=str, required=True, help="Path to your CSV file")
    args = parser.parse_args()

    train_model(args.data)

if __name__ == "__main__":
    main()
