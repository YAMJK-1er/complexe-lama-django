from django.shortcuts import redirect, render

# Create your views here.

def LamaPage(request) :
    if request.method == 'POST' :
        link = None

        if request.POST.get('categorie') == 'chambre' :
            nom = request.POST.get('nom')
            arrivee = request.POST.get('date-arrivee')
            depart = request.POST.get('date-depart')
            type = request.POST.get('type')

            phrase = "Bonjour, je suis {}. J'aimerais réserver une chambre {} dans votre hôtel pour la période du {} au {}.".format(nom, type, arrivee, depart)
            
            phrase = phrase.replace(' ', '%20')

            link = 'https://wa.me/22666904444?text={}'.format(phrase)

        if request.POST.get('categorie') == 'salle' :
            nom = request.POST.get('nom')
            debut = request.POST.get('date-debut')
            fin = request.POST.get('date-fin')
            type = request.POST.get('type')

            phrase = "Bonjour, je suis {}. J'aimerais réserver votre {} salle de conférence pour la période du {} au {}.".format(nom, type, debut, fin)
            
            phrase = phrase.replace(' ', '%20')

            link = 'https://wa.me/22666904444?text={}'.format(phrase) 

        return redirect(link)

    return render(request, 'index.html', {})