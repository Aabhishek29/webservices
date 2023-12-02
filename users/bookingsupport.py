import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import base64


def base64_to_pdf(base64_data, file_path):
    try:
        # Remove the header from base64 string if present (e.g., 'data:application/pdf;base64,')
        data = base64_data.split(",")[1] if "," in base64_data else base64_data

        # Decode base64 string to binary
        binary_data = base64.b64decode(data)

        # Write binary data to a PDF file
        with open(file_path, 'wb') as file:
            file.write(binary_data)

        print("PDF file created successfully at:", file_path)
        return True  # Indicate success
    except Exception as e:
        print("An error occurred:", str(e))
        return False  # Indicate failure


@api_view(["POST"])
def contactUs(request):
    try:
        data = request.data
        print(data)
        name = data["name"]
        email = data["email"]
        issue = data["issue"]
        phone = data["phoneNumber"]
        msg = data["msg"]
        htmlgen = f'''
                    <h1>BookingSupport.in Contact Us Request</h1>
                    <br/>
                    <h2><p><b>Name</b> : <span style="color: #666666">{name}<span> </p></h2>           
                    <h2><p><b>Email</b> : <span style="color: #666666">{email}<span> </p></h2>
                    <h2><p><b>Issue</b> : <span style="color: #666666">{issue}<span> </p></h2>
                    <h2><p><b>Phone Number</b> : <span style="color: #666666">{phone} <span></p></h2>
                    <h2>Message :-<h2/> 
                    <p style="color: #666666; font-size: 18px"><b>{msg}</b></p> <br/>
                    '''
        # reciptent_email = ["sigupbooking@gmail.com", "bookingnoc@gmail.com"]
        reciptent_email = ["starkabhishek29@gmail.com", "satyamshady005@gmail.com"]
        send_mail('Booking Support Contact Us Request', email, 'indzzwebservices@gmail.com', reciptent_email,
                  fail_silently=False,
                  html_message=htmlgen)
        return Response({"status": "success", "data": "mail send successfully"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"status": "success", "msg": "something went wrong", "data": e},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sendFormToBookingSupport(request):
    try:
        data = request.data
        # print(data)
        # Decode the Base64 string, making sure that it contains only valid characters
        b64 = data["base64"]  # Replace with your actual base64 data
        print(b64)
        file_path = './your_file.pdf'  # Replace with the desired file path

        base64_to_pdf(b64, file_path)
        return Response({"status": "success", "data": "pass"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "success", "authenticated": "false", "data": e}, status=status.HTTP_400_BAD_REQUEST)
