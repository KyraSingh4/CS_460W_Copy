from Bill import Bill

bill = Bill(1)

bill.createCharge(100, "Test", "Annual")
bill.createCharge(250, "Test", "Annual")
bill.createCharge(10, "Test", "Extra")
bill.createCharge(20, "Test", "B")
bill.createCharge(36.5, "Test", "A")

print(bill.getBill())
print(bill.getTotal())
bill.resetBill()