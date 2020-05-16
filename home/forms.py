from django.forms import *
from .models import Course, CourseFile


class CourseForm( ModelForm ):
    class Meta:
        model = Course
        fields = '__all__'
        
        exclude = ['instructor', 'like', 'rate']
        labels = {
            'title': '',
            'pdf': '',
            'description': '',
            'doc_file': '',
            'duration': '',
            'amount': '',
            'department': '',
            'cover_pic': ''
        }
        help_texts = {
            'pdf': 'please select attachments for material',
            'doc_file': 'Select all the file to upload(videos) for this course',
            'cover_pic': 'Upload the display image for your course',
            'description': 'Give details of the course, this must include how the is scheduled',
            'duration': 'How many hours is the course 1-30 or minutes 1-59',
            'department': 'Specify the department that can take this course form ',
            'amount': ' Price for this course in numbers within ₦500-₦5000',
            'title': 'Specify the title for this course more that 5 character'
        }

        widgets = {

            'description':  Textarea(attrs={'cols': 100, 'rows': 5, 'class': 'form-control', 'placeholder':'Details of this course'} ),
            'title': TextInput( attrs={'class': 'form-control', 'placeholder':'short descriptive title'} ),
            'doc_file': FileInput(attrs={ 'hidden': 'hidden', 'multiple': True} ),
            'pdf': FileInput( attrs={ 'hidden': 'hidden'} ),
            'duration': NumberInput( attrs={'class': 'form-control', 'placeholder':'duration in number','min':'1', 'max':'60'} ),
            'amount': NumberInput(attrs={'class': 'form-control', 'placeholder':'Price for this course', 'min':'500', 'max':'5000'}  ),
            'department': TextInput( attrs={'class': 'form-control', 'placeholder':'E.g computer science'} ),
            'cover_pic': FileInput(attrs={'class': 'custom-file form-control', 'hidden': 'hidden'} ),


        }
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CourseForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields[ 'title'].required = False
        self.fields[ 'description'].required = False
        self.fields[ 'department'].required = False
        self.fields[ 'duration'].required = False
        self.fields[ 'amount'].required = False
        self.fields[ 'doc_file'].required = False
        self.fields[ 'pdf'].required = False
        self.fields[ 'cover_pic'].required = False
        
