# Wellness Plus Pharmacy & Clinic - SBA Billing Program

choice = "RUN"

while choice.upper() != "EXIT":
print("\n--- Wellness Plus Patient Billing System ---")

# Input data from user
age = int(input("Enter patient's age: "))
consultation_type = input("Enter consultation type (General / Specialist): ").strip()
insurance_status = input("Does the patient have insurance? (Yes / No): ").strip()
num_medications = int(input("Enter number of medications: "))
unit_cost = float(input("Enter unit cost per medication ($): "))

# Calculate consultation fee
if consultation_type.lower() == "general":
consultation_fee = 3000.0
else:
consultation_fee = 5000.0

# Apply insurance discount
if insurance_status.lower() == "yes":
consultation_fee = consultation_fee - 1000.0

# Calculate total medication cost and subtotal
total_med_cost = num_medications * unit_cost
sub_total = consultation_fee + total_med_cost

# Apply senior citizen discount if age is 60 or older
if age >= 60:
senior_discount = sub_total * 0.10
else:
senior_discount = 0.0

# Calculate final total bill
total_bill = sub_total - senior_discount

# Output the results
print("\n----- BILLING SUMMARY -----")
print(f"Consultation Fee: ${consultation_fee:.2f}")
print(f"Total Medication Cost: ${total_med_cost:.2f}")
print(f"Senior Discount Applied: ${senior_discount:.2f}")
print(f"TOTAL BILL: ${total_bill:.2f}")
print("----------------------------")

# Ask user to continue or exit
choice = input("\nType 'RUN' to bill another patient or 'EXIT' to quit: ").strip()

print("\nProgram exited successfully. Thank you!")
