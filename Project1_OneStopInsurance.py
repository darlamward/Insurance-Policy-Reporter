#  One Stop Insurance Company's program to enter and calculate new insurance policy information for its customers
#  Completed by Darla Ward
#  Completed on Aug 3, 2022

import datetime

def FDollar2(DollarValue):

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr

def PaymentDateDsp(CurrentPolicyDate):

    if PolicyDate.day > 25:
        NextPaymentMonth = PolicyDate.month + 2
        if NextPaymentMonth == 13:
            NextPaymentMonth = 1
            NextPaymentYear = PolicyDate.year + 1
        elif NextPaymentMonth == 14:
            NextPaymentMonth = 2
            NextPaymentYear = PolicyDate.year + 1
        else:
            NextPaymentYear = PolicyDate.year
    if PolicyDate.day < 25:
        NextPaymentMonth = PolicyDate.month + 1
        if NextPaymentMonth == 13:
            NextPaymentMonth = 1
            NextPaymentYear = PolicyDate.year + 1
        elif NextPaymentMonth == 14:
            NextPaymentMonth = 2
            NextPaymentYear = PolicyDate.year + 1
        else:
            NextPaymentYear = PolicyDate.year

    PaymentDate = PolicyDate.strftime("%m/%d/%Y")
    # format 1 digit month with leading zeros.
    NextPaymentMonthDsp = "{:02d}".format(NextPaymentMonth)
    PaymentDate = PolicyDate.strftime(f"{NextPaymentMonthDsp}/01/{NextPaymentYear}")

    return PaymentDate

def FNumber2(DollarValue):

    DollarValueStr = "{:.2f}".format(DollarValue)

    return DollarValueStr


f = open('OSICDef.dat', 'r')
PolicyNum = int(f.readline())
BasicPremium = float(f.readline())
AddCarDiscountRate = float(f.readline())
ExtraLiabilityCoverageCost = float(f.readline())
GlassCoverageCost = float(f.readline())
LoanerCarCoverageCost = float(f.readline())
HSTRate = float(f.readline())
MonthlyProcessingFee = float(f.readline())
f.close()

while True:
    CustFirstName = input("Enter customer's first name: ").upper()
    FirstInitial = CustFirstName[0]
    CustLastName = input("Enter customer's last name: ").upper()
    LastInitial = CustLastName[0]
    CustStAdd = input("Enter customer's street address: ").upper()
    CustCity = input("Enter customer's city address: ").upper()
    CustProv = input("Enter customer's province: ").upper()
    CustPostCode = input("Enter customer's postal code: ").upper()
    CustPhoneNum = input("Enter customer's phone number:")
    NumOfCars = int(input("Enter the number of cars being insured: "))
    ExtraLiabilityCoverage = input("Is there extra liability coverage up to $1,000,000(Y or N): ").upper()
    ExtraGlassCoverage = input("Is there optional glass coverage(Y or N): ").upper()
    OptionalLoanCar = input("Is there an optional loaner car(Y or N): ").upper()
    PaymentOption = input("Paying Monthly(M) or in Full(F): ").upper()
    PolicyDate = datetime.datetime.today()
    PolicyDateDsp = PolicyDate.strftime("%m/%d/%Y")
    ReportDateDsp = PolicyDate.strftime("%d-%b-%y")

    if NumOfCars == 1:
        InsurancePremiumCost = BasicPremium
    else:
        InsurancePremiumCost = BasicPremium + ((NumOfCars - 1) * (BasicPremium - (BasicPremium * AddCarDiscountRate)))
    if ExtraLiabilityCoverage == "Y":
        ExtraLiabilityCost = ExtraLiabilityCoverageCost * NumOfCars
    else:
        ExtraLiabilityCost = 0.00
    if ExtraGlassCoverage == "Y":
        ExtraGlassCost = GlassCoverageCost * NumOfCars
    else:
        ExtraGlassCost = 0.00
    if OptionalLoanCar == "Y":
        OptionalLoanerCost = LoanerCarCoverageCost * NumOfCars
    else:
        OptionalLoanerCost = 0.00

    TotalExtraCosts = ExtraLiabilityCost + ExtraGlassCost + OptionalLoanerCost
    TotalInsurancePremium = InsurancePremiumCost + TotalExtraCosts
    HST = TotalInsurancePremium * HSTRate
    TotalCost = HST + TotalInsurancePremium

    if PaymentOption == "M":
        TotalAmountDue = (MonthlyProcessingFee + TotalCost)
        MonthlyPayment = TotalAmountDue / 12
    else:
        PaymentAmount = TotalCost

    print()
    print("{:^60s}".format("One Stop Insurance"))
    print("-" * 60)
    print(f"Policy #: {PolicyNum}-{FirstInitial}{LastInitial}                           Date: {PolicyDateDsp}")
    print(f"    {CustFirstName:<10s} {CustLastName:<10s}                       {CustPhoneNum:>12s}")
    print(f"    {CustStAdd}")
    print(f"    {CustCity}, {CustProv:<2s}  {CustPostCode:<6s}")
    print("-" * 60)
    print(f"Number of Cars insured: {NumOfCars:>3d}")
    if ExtraLiabilityCoverage == "Y":
        print(f"Extra Liability Coverage:                         {FDollar2(ExtraLiabilityCost):>9s}")
    if ExtraGlassCoverage == "Y":
        print(f"Optional Glass Coverage:                          {FDollar2(ExtraGlassCost):>9s}")
    if OptionalLoanCar == "Y":
        print(f"Loaner Car Coverage:                              {FDollar2(OptionalLoanerCost):>9s}")
    print("=" * 60)
    print(f"                              Extra Costs Total:  {FDollar2(TotalExtraCosts):>9s}")
    print(f"                              Premium Cost Total: {FDollar2(InsurancePremiumCost):>9s}")
    print("                                              --------------")
    print(f"                              Subtotal:           {FDollar2(TotalInsurancePremium):>9s}")
    print(f"                              HST:                {FDollar2(HST):>9s}")
    print("                                              --------------")
    print(f"                              Total:             {FDollar2(TotalCost):>10s}")
    print("=" * 60)
    if PaymentOption == "M":
        print("{:^60s}".format("Monthly Payment Plan"))
        print(f"Total:            {FDollar2(TotalCost):>10s}")
        print(f"Processing Fee:   {FDollar2(MonthlyProcessingFee):>10s}")
        print("                --------------")
        print(f"Total Amount Due: {FDollar2(TotalAmountDue):>10s}")
        print(f"                          Monthly Payment Amount: {FDollar2(MonthlyPayment):>10s}")
        print()
        print(f"                 {FDollar2(MonthlyPayment):^9s} due by {PaymentDateDsp(PolicyDate):^10s}")
    else:
        print(f"                {FDollar2(TotalCost):^9s} due up front.")
    print("=" * 60)
    print()

    PolicyNum += 1

    f = open('Policies.dat', 'a')
    f.write("{}, ".format(PolicyNum))
    f.write("{}, ".format(PolicyDateDsp))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(CustStAdd))
    f.write("{}, ".format(CustCity))
    f.write("{}, ".format(CustProv))
    f.write("{}, ".format(CustPostCode))
    f.write("{}, ".format(CustPhoneNum))
    f.write("{}, ".format(NumOfCars))
    f.write("{}, ".format(ExtraLiabilityCoverage))
    f.write("{}, ".format(ExtraGlassCoverage))
    f.write("{}, ".format(OptionalLoanCar))
    f.write("{}, ".format(PaymentOption))
    f.write("{}\n".format(FDollar2(TotalCost)))
    f.close()

    FNumInsurancePremiumCost = FNumber2(InsurancePremiumCost)
    FNumTotalExtraCosts = FNumber2(TotalExtraCosts)
    FNumTotalInsurancePremium = FNumber2(TotalInsurancePremium)
    FNumHST = FNumber2(HST)
    FNumTotalCost = FNumber2(TotalCost)

    f = open('PolicyCostsPerCustomer.dat', 'a')
    f.write("{}, ".format(PolicyNum))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(FNumInsurancePremiumCost))
    f.write("{}, ".format(FNumTotalExtraCosts))
    f.write("{}, ".format(FNumTotalInsurancePremium))
    f.write("{}, ".format(FNumHST))
    f.write("{}, ".format(FNumTotalCost))
    f.write("{}, ".format(PaymentOption))
    if PaymentOption == 'M':
        FNumMonthlyPayment = FNumber2(MonthlyPayment)
        f.write("{}\n".format(FNumMonthlyPayment))
    else:
        f.write("{}\n".format("Paid."))
    f.close()

    print("Policy processed and saved!")
    print()

    AnotherPolicy = input("Would you like to enter another policy(Y/N)? ").upper()
    if AnotherPolicy == "Y":
        print()
        print()
        continue
    else:
        print()
        print()
        break

f = open('OSICDef.dat', 'w')
f.write("{}\n".format(int(PolicyNum)))
f.write("{}\n".format(float(BasicPremium)))
f.write("{}\n".format(float(AddCarDiscountRate)))
f.write("{}\n".format(float(ExtraLiabilityCoverageCost)))
f.write("{}\n".format(float(GlassCoverageCost)))
f.write("{}\n".format(float(LoanerCarCoverageCost)))
f.write("{}\n".format(float(HSTRate)))
f.write("{}\n".format(float(MonthlyProcessingFee)))
f.close()

#  Reports

Reports = input("Would you like to print a report(Y/N)?").upper()
if Reports == 'Y':
    print("{:^60s}".format("Policy Listing Report"))
    print()
    print("ONE STOP INSURANCE COMPANY")
    print(f"POLICY LISTING AS OF {ReportDateDsp}")
    print()
    print("POLICY CUSTOMER               INSURANCE    EXTRA      TOTAL")
    print("NUMBER NAME                    PREMIUM     COSTS     PREMIUM")
    print("=" * 61)
    TotalNumPolicies = 0
    InsurancePremiumAcc = 0.00
    ExtraCostsAcc = 0.00
    TotalPremiumAcc = 0.00

    f = open("PolicyCostsPerCustomer.dat", "r")
    for DataLine in f:
        Info = DataLine.split(",")
        PolicyNumReport = int(Info[0].strip())
        CustFirstNameReport = Info[1].strip()
        CustLastNameReport = Info[2].strip()
        InsurancePremiumCostReport = float(Info[3].strip())
        TotalExtraCostsReport = float(Info[4].strip())
        TotalInsurancePremiumReport = float(Info[5].strip())

        print(f" {PolicyNumReport:4d}  {CustFirstNameReport:10s} {CustLastNameReport:10s}  "
              f"{FDollar2(InsurancePremiumCostReport):>9s}  {FDollar2(TotalExtraCostsReport):>9s}  "
              f"{FDollar2(TotalInsurancePremiumReport):>9s}")

        TotalNumPolicies += 1
        InsurancePremiumAcc += InsurancePremiumCostReport
        ExtraCostsAcc += TotalExtraCostsReport
        TotalPremiumAcc += TotalInsurancePremiumReport
    f.close()
    print("=" * 61)
    print(f"Total Policies: {TotalNumPolicies:^3d}          {FDollar2(InsurancePremiumAcc):>10s}  "
          f"{FDollar2(ExtraCostsAcc):>10s}  {FDollar2(TotalPremiumAcc):>10s}")
    print()
    print()
    print("{:^70s}".format("Monthly Payment Listing"))
    print()
    print("ONE STOP INSURANCE COMPANY")
    print(f"MONTHLY PAYMENT LISTING AS OF {ReportDateDsp}")
    print()
    print("POLICY CUSTOMER               TOTAL                TOTAL       MONTHLY")
    print("NUMBER NAME                  PREMIUM      HST      COST        PAYMENT")
    print("=" * 70)
    MonthlyTotalNumPolicies = 0
    MonthlyTotalPremiumAcc = 0.00
    TotalHSTAcc = 0.00
    TotalCostAcc = 0.00
    TotalMonthlyPaymentAcc = 0.00
    f = open("PolicyCostsPerCustomer.dat", "r")
    for DataLine in f:
        Info = DataLine.split(', ')
        PolicyNum = int(Info[0].strip())
        CustFirstName = Info[1].strip()
        CustLastName = Info[2].strip()
        MTotalInsurancePremiumReport = float(Info[5].strip())
        MHSTReport = float(Info[6].strip())
        MTotalCostReport = float(Info[7].strip())
        MPaymentOptionReport = Info[8].strip()

        if MPaymentOptionReport == "M":
            MMonthlyPaymentReport = float(Info[9].strip())
            print(f" {PolicyNum:4d}  {CustFirstName:10s} {CustLastName:10s} {FDollar2(MTotalInsurancePremiumReport):>9s}"
                f"  {FDollar2(MHSTReport):>7s}  {FDollar2(MTotalCostReport):>9s}  {FDollar2(MMonthlyPaymentReport):>9s}")
            MonthlyTotalNumPolicies += 1
            MonthlyTotalPremiumAcc += MTotalInsurancePremiumReport
            TotalHSTAcc += MHSTReport
            TotalCostAcc += MTotalCostReport
            TotalMonthlyPaymentAcc += MMonthlyPaymentReport
        else:
            continue
    f.close()
    print("=" * 70)
    print(f"Total Policies: {MonthlyTotalNumPolicies:^3d}       {FDollar2(MonthlyTotalPremiumAcc):>10s} "
          f"{FDollar2(TotalHSTAcc):>9s}  {FDollar2(TotalCostAcc):>10s} {FDollar2(TotalMonthlyPaymentAcc):>10s}")
print("{:^60s}".format("Program Finished"))
