from Customer_Churn.src.Components.data_validation import DataValidation

def main():

    validator = DataValidation()

    status = validator.validate_dataset()

    print(f"\nValidation Status : {status}")


if __name__ == "__main__":
    main()