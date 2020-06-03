from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage



# Create your views here.
class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):    
        return render(request, self.template_name,{'Titulo':'Texto de titulo'})
      
def contacto(request):
    formContact = ContactForm()

    #validar la peticion post
    if request.method == "POST":
        formContact = ContactForm(data=request.POST)    
        if formContact.is_valid():
            nombre = request.POST.get('nombre', '') #trael el atributo con lo
            correo = request.POST.get('correo', '') #lo que estaba por el metodo POST lo pasa a get
            telefono = request.POST.get('telefono', '')
            mensaje = request.POST.get('mensaje', '')

            #creamos el objeto con variable del formulario
            email = EmailMessage( #objeto email

                "Tienes un nuevo mensaje",  #el format trae los datos del formulario
                "De {} <{}>\n\nEscribio:\n\n{}\n\nTelefono :{}".format(nombre,correo,mensaje,telefono),
                "no-contestar@inbox.mailtrap.io",
                ["jecastiblanco14@misena.edu.co","jhoneinsteing@gmail.com"], #lista donde se va enviar el correo
                reply_to=[correo],
                
            )
            #enviar correo
            try:
                email.send()
                return redirect(reverse('contacto')+"?okay")
            except:
            #envia mensaje
                return redirect(reverse('contacto')+"?fallido")

    return render(request, 'contacto.htm', {'formulario':formContact})