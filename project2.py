from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(payee_name, transc_amt, payment_type):
    receipt = canvas.Canvas(payee_name+".pdf", pagesize=letter)               # Create a canvas (PDF document)
    
    receipt.setFont("Helvetica", 12)                                               # Set font and size
    
    receipt.drawString(50, 750, "Payment Receipt")                                     # Write text to the PDF
    receipt.drawString(50, 730, "---------------------")
    receipt.drawString(50, 700, f"Customer Name: {payee_name}")
    receipt.drawString(50, 680, f"Amount Paid: ${transc_amt}")
    receipt.drawString(50, 660, f"Payment Method: {payment_type}")
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                       # Print current date and time
    receipt.drawString(50, 640, f"Issued on: {now}")
    
    receipt.save()                                                                    # Save the PDF document
    print("Payment receipt created successfully!")


create_receipt("XYZ_person", 100.00, "Credit Card")
