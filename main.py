# from Customer_Churn.src.Components.data_validation import DataValidation

# def main():

#     validator = DataValidation()

#     status = validator.validate_dataset()

#     print(f"\nValidation Status : {status}")


# if __name__ == "__main__":
#     main()

import numpy as np

np_ar = np.load(r'Customer_Churn\artifacts\data_transformation\test.npy')

print(np_ar)