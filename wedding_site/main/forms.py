from django import forms

class InfoForm(forms.Form):
    name = forms.CharField(label='Имя', #имя предстаялется формой класса Charfield - однострочное текстовое поле, заданы 2 необязательных аргумента
        help_text='Укажите пожалуйста Ваше имя',
        max_length = 60, # имеет ограничение по максимальному количеству символов - 60 символов
        widget = forms.TextInput(attrs={ #имеет виджет Textinput соответсвующий однострочному текстовому полю. Виджету задан аргумент attrs, которому передаются свойства которыми будет наделен HTML элемент
            'placeholder': 'Введите Ваше имя', #  и подсказака в виде фразы "Ваше имя"
            'width': 600
        })
    )
    surname = forms.CharField(label='Фамилия',
        help_text='Укажите пожалуйста Вашу фамилию',
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите Вашу фамилию',
        })
    )
    alkhogol_preferens = forms.CharField(label='Предпочтения в акоголе',
                              help_text='Укажите пожалуйста что предпочитаете пить (первый день). Если вино - то уточните пожалуйста какое. Если не употребляете алкоголь - так и пишите. Поле обязательно для заполнения',
                              max_length=250,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'например - вино белое, полусухое',
                              })
                              )

    other_important_information = forms.CharField(label='Другая ВАЖНАЯ информация',
                                        help_text='Поле не обязательно для заполнения. Но если есть важная информация, которую нужно учесть при организации или может быть генератором проблем в процессе - то просьба её указать здесь. Например - "Я не ем мясо" или "Аллергия на клубнику"',
                                        required=False, # атрибут, делающий поле необязательным для заполнения
                                        widget=forms.Textarea(attrs={
                                             'placeholder': 'например - я вегетарианец',
                                        })
                                        )

    second_day = forms.CharField(label='Второй день',
                              help_text='Укажите пожалуйста планируете ли вы приехать на второй день',
                              max_length=60,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'да или нет',
                              })
                              )

    sauna = forms.CharField(label='Баня',
                                 help_text='Укажите пожалуйста поёдете ли вы в баню',
                                 max_length=60,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'да или нет',
                                 })
                                 )

    beer_preferens = forms.CharField(label='Предпочтения в пиве',
                                         help_text='Укажите пожалуйста какое пиво предпочитаете. Можно указывать такие пивные напитки как Garage, или другие слабоалкогольные напитки. Если не употребляете алкоголь - так и пишите. Поле обязательно для заполнения',
                                         max_length=250,
                                         widget=forms.TextInput(attrs={
                                             'placeholder': 'например - пиво светлое, нефильтрованное',
                                         })
                                         )

    other_information = forms.CharField(label='Прочая информация',
                                        help_text='Поле не обязательно для заполнения. Тут можно указать что вы можете прихватить с собой, чем помочь или что интересного предложить',
                                        required=False, # атрибут, делающий поле необязательным для заполнения
                                        widget=forms.Textarea(attrs={
                                             'placeholder': 'например - я возьму мяч',
                                        })
                                        )

    assept=forms.BooleanField(label=' Подтверждение',
                            help_text='Проставляя данною галочку Вы подтверждаете своё присутсвие 06.09.2024, а также то что Вы прочли всю информацию выше',
                            widget = forms.CheckboxInput(attrs={
                            'class': 'checkbox',
                            })
                            )
