from django import forms
from .models import Booking, Text
from datetime import timezone
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
    YearPickerInput
    )


from django.utils import timezone

choice_schedule = [
    ('Mon2', 'Senin 2pm-4pm'),
    ('Mon4', 'Senin 4pm-6pm'),
    ('Mon8', 'Senin 8pm-10pm'),
    ('Tue2', 'Selasa 2pm-4pm'),
    ('Tue4', 'Selasa 4pm-6pm'),
    ('Tue8', 'Selasa 8pm-10pm'),
    ('Wed2', 'Rabu 2p-4pm'),
    ('Wed4', 'Rabu 4pm-6pm'),
    ('Wed8', 'Rabu 8pm-10pm'),
    ('Thu2', 'Kamis 2p-4pm'),
    ('Thu4', 'Kamis 4pm-6pm'),
    ('Thu8', 'Kamis 8pm-10pm'),
    ('Fri2', 'Jumat 2p-4pm'),
    ('Fri4', 'Jumat 4pm-6pm'),
    ('Fri8', 'Jumat 8pm-10pm'),
    ]
choice_class = [
    ('SD13', 'SD Kelas 1-3'),
    ('SD46', 'SD Kelas 4-6'),
    ('SM79', 'SMP Kelas 7-9'),
    ('SA10', 'SMA Kelas 10-12'),

    ]

class BookCreateForm(forms.ModelForm):

    fname = forms.CharField(label='Enter first name ',label_suffix=':', max_length=50)
    lname = forms.CharField(label='Last name ',label_suffix=':',max_length=50)
    phone = forms.CharField(label='Phone number ',label_suffix=':',max_length=12)
    klas = forms.ChoiceField(
        label='Choose a coding class ',
        label_suffix=':',
        choices = choice_class
        )

    time_schedule = forms.MultipleChoiceField(
        label='Choose one or more schedules ',
        label_suffix=':',
        choices = choice_schedule
        )
    date_started = DatePickerInput()
    class Meta:
        model = Booking
        fields = '__all__'
        #fields = ['fname','lname','phone','klas','time_schedule','date_started']

        widgets = {
           'date_started' :  forms.DateInput(attrs={'type':'date'})
        }

class TextCreateForm(forms.ModelForm):


    def clean(self):
        super(TextCreateForm, self).clean()

    class Meta:
        model = Text
        fields = '__all__'
        # widgets = {
        #     'date_teks': forms.DateInput(attrs={'type': 'date'})
        # }
