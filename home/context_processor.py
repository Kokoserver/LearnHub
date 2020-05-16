from .models import College, Department

def nav_data(request):
     
    humanity = Department.objects.filter(college_faculty_id=1)
    engineering = Department.objects.filter(college_faculty_id=3)
    law = Department.objects.filter(college_faculty_id=4)
    pap= Department.objects.filter(college_faculty_id=6)
    education = Department.objects.filter(college_faculty_id=5)
    ict= Department.objects.filter(college_faculty_id=2)
    context = {
        'edu': education,
        'law':law,
        'pap':pap,
        'ict':ict,
        'humanity':humanity,
        'engineering':engineering
    }
    return  context