from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.urls import reverse

def home_page_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        print(name, email, comment)
        try:
            send_mail(
                f"Enquiry - {name}",
                f"{email} - {comment}",
                "syamprasad340@gmail.com",
                ["syam2400@gmail.com"],
                fail_silently=False,
            )
            request.session['message'] = 'Email sent successfully'
        except BadHeaderError:
            request.session['message'] = 'Invalid header found.'
        except SMTPException as e:
            request.session['message'] = f'SMTP error occurred: {e}'
        except Exception as e:
            request.session['message'] = f'An error occurred: {e}'
        return redirect(reverse('home'))  # Adjust to your URL name

    message = request.session.pop('message', '')
    return render(request, 'index.html', {"message": message})