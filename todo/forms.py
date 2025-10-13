from django import forms
from . models import Todo


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description']
        
    def clean_title(self):
        title :str = self.cleaned_data["title"]
        if not title[0].islower():
            raise forms.ValidationError("faqat katta  hatrfi bolishi kerak")
        return title
        

# class TodoForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     description = forms.CharField()
#     # startdate = forms.DateField(widget=forms.DateInput)
#     # enddate = forms.DateField()
    
#     def clean_title(self):
#         title = self.cleaned_data["title"]
#         print("title : ",title)
#         if not title.startswith("a"):
#             raise forms.ValidationError("Title a dan boshlanishi kerak")  
#         return title
    
    
    
    # def clean(self):
    #     cleaned_data = super().clean()
        
        
    #     if cleaned_data["stardate"] > cleaned_data["enddate"]:
    #         raise forms.ValidationError("date xato")
        
    #     return cleaned_data
    
    
    