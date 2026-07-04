from src.validation import DataValidation


def main():

    validator = DataValidation()

    status = validator.validate_dataset()

    print(f"\nValidation Status : {status}")


if __name__ == "__main__":
    main()