START
DECLARE age, numMedications AS INTEGER
DECLARE consultationType, insuranceStatus, choice AS STRING
DECLARE consultationFee, totalMedCost, subTotal, seniorDiscount, totalBill AS REAL

choice ← "RUN"
WHILE choice != "EXIT" DO
INPUT age, consultationType, insuranceStatus, numMedications, unitCost

IF consultationType == "General" THEN m
consultationFee ← 3000
ELSE
consultationFee ← 5000
ENDIF

IF insuranceStatus == "Yes" THEN
consultationFee ← consultationFee - 1000T
ENDIF

totalMedCost ← numMedications * unitCost
subTotal ← consultationFee + totalMedCost

IF age >= 60 THEN
seniorDiscount ← subTotal * 0.10
ELSE
seniorDiscount ← 0
ENDIF

totalBill ← subTotal - seniorDiscount

PRINT consultationFee, totalMedCost, seniorDiscount, totalBill
INPUT choice
ENDWHILE
END

| Test Case | age | consultationType | insuranceStatus | numMedications | unitCost | consultationFee | totalMedCost | subTotal | seniorDiscount | totalBill | choice |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Setup** | - | - | - | - | - | - | - | - | - | - | "RUN" |
| **Pass 1**| 65 | "General" | "Yes" | 3 | 500 | 2000 | 1500 | 3500 | 350 | 3150 | "RUN" |
| **Pass 2**| 30 | "Specialist"| "No" | 2 | 1000 | 5000 | 2000 | 7000 | 0 | 7000 | "EXIT"|
