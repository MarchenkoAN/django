from django import forms
from django.forms import inlineformset_factory
from qwestion.models import Survey, Qwestion, Answer

class SurveyCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Survey
        fields = ['title', 'timedelta', 'public']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('user')
        super(SurveyCreateForm, self).__init__(*args, **kwargs)


class AddSurveyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Survey
        fields = ['title', 'timedelta', 'public']


QwestionFormset = inlineformset_factory(Survey, Qwestion, fields='__all__')
AnswerFormset = inlineformset_factory(Qwestion, Answer, fields='__all__')


class QwestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Qwestion
        fields = ['title', 'input']

class QwestionCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Qwestion
        fields = '__all__'


class AnswerCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Answer
        fields = '__all__'

