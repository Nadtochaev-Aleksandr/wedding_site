from django.shortcuts import render
from django.http import HttpResponse
from .models import WeddingInfo
from .forms import InfoForm
wedinfo=WeddingInfo.objects.all()

# Create your views here.
def wedding(request):
    wedinfo = WeddingInfo.objects.all()
    userform = InfoForm()
    if request.method=='POST':
        userform = InfoForm(request.POST) # Передача данных из формы методом POST
        if userform.is_valid(): # Проверка на валидность данных из формы
            data=WeddingInfo( # создание объекта класса модели WeddingInfo и передача ему следующих атрибутов:
                name=userform.cleaned_data['name'], #Каждый атрибут соответсвует имени полей модели иберется из формы методам cleaned_data
                surname = userform.cleaned_data['surname'],
                alkhogol_preferens = userform.cleaned_data['alkhogol_preferens'],
                other_important_information = userform.cleaned_data['other_important_information'],
                second_day = userform.cleaned_data['second_day'],
                sauna = userform.cleaned_data['sauna'],
                beer_preferens = userform.cleaned_data['beer_preferens'],
                other_information = userform.cleaned_data['other_information']
            )
            data.save() #сохранение данных

#Второй вариант - получение данных просто через метод request.get Работает как с is_valid, так и без него
        # data = WeddingInfo(  # создание объекта класса модели WeddingInfo и передача ему следующих атрибутов:
        #     name=request.POST.get("name"),
        #     surname = request.POST.get("surname"),
        #     alkhogol_preferens = request.POST.get("alkhogol_preferens"),
        #     other_important_information = request.POST.get("other_important_information"),
        #     second_day = request.POST.get("second_day"),
        #     sauna = request.POST.get("sauna"),
        #     beer_preferens = request.POST.get("beer_preferens"),
        #     other_information = request.POST.get("other_information"),
        # )
        # data.save()  # сохранение данных

        name = request.POST.get("name")
        surname = request.POST.get("surname")
        alkhogol_preferens = request.POST.get("alkhogol_preferens")
        other_important_information = request.POST.get("other_important_information")
        second_day = request.POST.get("second_day")
        sauna = request.POST.get("sauna")
        beer_preferens = request.POST.get("beer_preferens")
        other_information = request.POST.get("other_information")

        return render(request, 'main/wedding_page.html', {'form':userform, 'name':name, 'surname':surname, 'drink':alkhogol_preferens,
                                                          's_day':second_day, 'sauna':sauna, 'beer':beer_preferens})
    else:
        userform = InfoForm()
        return render(request, 'main/wedding_page.html', {'form': userform})
