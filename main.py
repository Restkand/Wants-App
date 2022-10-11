from cashFunction import cashFunc

print('Wants App')
cashFunc = cashFunc()
if(cashFunc.sisa >= 20):
  print("Boleh banget nih buat menuhin wants kamu sesekali")
elif(cashFunc.sisa >= 10):
  print("Coba kamu pertimbangin lagi")
elif(cashFunc.sisa >= 1):
  print("Waduh mending ditahan dulu beli barangnya")
else:
  print("Big No! Udah melebihi budget kamu ni!")