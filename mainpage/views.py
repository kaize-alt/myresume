from weasyprint import HTML

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import PersonalInfo


def resume_detail(request, pk):
    personal_info = get_object_or_404(PersonalInfo, pk=pk)
    return render(request, 'myown/resume_detail.html', {'personal_info': personal_info})

def generate_pdf(request, pk):
    personal_info = PersonalInfo.objects.get(pk=pk)
    html_content = render_to_string('myown/resume_detail.html', {'personal_info': personal_info})
    pdf = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{personal_info.full_name}.pdf"'
    return response
