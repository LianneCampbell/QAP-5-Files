#The One Stop Insurance Companynow needs a program(s) to process the data file and create a couple of reports. 
#There is a Defaults file (OSICDef.dat) that you can make use of. 
d=open("OSICDef.dat", "a")
for defaults in d:
    DefLst = defaults.split(",")
    #Assign variables to each item in the list required.
    DefPolNum = defaults[0].strip()
    DefPremCar = defaults[1].strip()
    DefDscRate = defaults[2].strip()
    ExtLiabilityCost = defaults[3].strip()
    GlassCovCost = defaults[4].strip()
    LoanCarCost = defaults[5].strip()
    HstRate = defaults[6].strip()
    ProcessFee = defaults[7].strip()

#It includes the next policy number, the premium for the first car, the discount rate for additional cars, the costs are $130.00 per car for extra liability, 
#$86.00 per car for glass coverage, and $58.00 per car for the loaner car option, the HST rate, and finally the processing fee for monthly payments.  
#2032 869.00 0.25 130.00 86.00 58.0 0.15 39.99
# Set up the loop to process all the records in the file.

f=open("Policies 2.dat", "a")
for Policies in f:      
    # Input - read the first record and split into a list.
    PolLst = Policies.split(",")
   
    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    PolNum = Policies[0].strip()
    PolDate = Policies[1].strip()
    CustFirstName = Policies[2].strip()
    CustLastName = Policies[3].strip()
    CustAdd = Policies[4].strip()
    CustCity = Policies[5].strip()
    CustProv = Policies[6].strip()
    CustPost = Policies[7].strip()
    Phone = Policies[8].strip()
    NumCars = int(Policies[9].strip())
    ExtraLiabilityYN = Policies[10].strip()
    GLassCovYN = Policies[11].strip()
    LoanerYN = Policies[12].strip()
    PayType = Policies[13].strip()
    DownPayAmt =float(Policies[14].strip())

#it will be 0 if the option is Monthly or Full.I have the first record only here, but there are 10 records in the file.
#1944, 2023-03-10, John, Smith, 12 Main St., St. John’s, NL, A1A8H4, 123-123-1234, 2, Y, N, Y, Full, 0.00

1234567890123456789012345678901234567890123456789012345678901234567890123
print(f"ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF dd-Mon-yy")
print(f"POLICYCUSTOMER              POLICY     INSURANCE   EXTRA      TOTAL")
print(f"NUMBERNAME                  DATE       PREMIUM     COSTS     PREMIUM")
print(f"=========================================================================")
print(f"XXXX  XXXXXXXXXXXXXXXXXXXX  yyyy-mm-dd  $#,###.## $#,###.##  $#,###.##")
print(f"")
print(f"XXXX  XXXXXXXXXXXXXXXXXXXX  yyyy-mm-dd  $#,###.## $#,###.##  $#,###.##")
print(f"=========================================================================")
print(f"Total policies: ###      $##,###.## $##,###.## $##,###.##")

#The second report is an exception report. Include only the customers who make payments Monthly or 
#Down Pay as the exception. The Total Premium is calculated as the last report. HST is calculated at 15% 
#on the Total Premium, and the Total Cost is the total premium plus the HST. Calculate the monthly 
#payment by adding a processing fee of $39.99 to the total cost and dividing by 12 – subtract the 
#downpayment first if there is one.


1234567890123456789012345678901234567890123456789012345678901234567890123
print(f"ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF dd-Mon-yy")
print(f"POLICY CUSTOMER TOTAL TOTAL DOWN MONTHLY")
print(f"NUMBER NAME PREMIUM HST COST PAYMENT PAYMENT")
print(f"=========================================================================")
print(f"XXXX XXXXXXXXXXXXXXXXXXXX $#,###.## $###.## $#,###.## $#,###.## $#,###.##")
print(f"")
print(f"XXXX XXXXXXXXXXXXXXXXXXXX $#,###.## $###.## $#,###.## $#,###.## $#,###.##")
print(f"=========================================================================")
print(f"Total policies: ### $#,###.## $###.## $#,###.## $#,###.## $#,###.##")
