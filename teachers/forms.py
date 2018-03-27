from django import forms
from .models import ExamMark

class ExamMarkForm(forms.ModelForm):
    class Meta:
        
        model=ExamMark
        fields=[
            'student_number',
            'subject_name',
            'Total_Mark',
            'comment',
            'paper1_Mark',
            'paper2_Mark',
            'paper3_Mark',
            'paper4_Mark',
            'paper5_Mark',
            'paper6_Mark',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(ExamMarkForm,self).__init__(*args,**kwargs)
         
    

                

