import qrcode as qr

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa+UPI_ID&pn=Name&mc=Message&tid=Transaction_ID&am=Amount&cu=Currency&url=URL

#defining the UPI URL format
#You can customize the parameters as needed

phonepe_url = f"UPI://pay?pa={upi_id}&pn=Name&mc=Message&tid=Transaction_ID&am=Amount&cu=Currency&url=URL"
Google_pay_url = f"UPI://pay?pa={upi_id}&pn=Name&mc=Message&tid=Transaction_ID&am=Amount&cu=Currency&url=URL"
paytm_url = f"UPI://pay?pa={upi_id}&pn=Name&mc=Message&tid=Transaction_ID&am=Amount&cu=Currency&url=URL"

#Creating QR codes for each payment app
phonepe_url = qr.make(phonepe_url)
Google_pay_url = qr.make(Google_pay_url)
paytm_url = qr.make(paytm_url)

#Saving the QR codes as images
phonepe_url.save("phonepe_qr.png")  
paytm_url.save("paytm_qr.png")
Google_pay_url.save("google_pay_qr.png")

#Displaying the QR codes
phonepe_url.show()
paytm_url.show()    
Google_pay_url.show()