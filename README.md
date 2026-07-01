START
DECLARE age, numMedications AS INTEGER
DECLARE consultationType, insuranceStatus, choice AS STRING
DECLARE consultationFee, totalMedCost, subTotal, seniorDiscount, totalBill AS REAL

choice ← "RUN"
WHILE choice != "EXIT" DO
INPUT age, consultationType, insuranceStatus, numMedications, unitCost

IF consultationType == "General" THEN
consultationFee ← 3000
ELSE
consultationFee ← 5000
ENDIF

IF insuranceStatus == "Yes" THEN
consultationFee ← consultationFee - 1000
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
