#coding: utf-8
from django.shortcuts import render

from issem.models import Departamento
from issem.forms import DepartamentoForm


def index(request):
    departamento = Departamento.objects.all()
    context_dict = {'departamento': departamento}
    return render(request, 'issem/index.html', context_dict)

def add_departamento(request):
    # A HTTP POST?
    #return HttpResponseRedirect('Funcionou')
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = DepartamentoForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'issem/cadastro_departamento.html', {'form': form})

def add_cid(request):
    # A HTTP POST?
    #return HttpResponseRedirect('Funcionou')
    if request.method == 'POST':
        form = CidForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CidForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'issem/cadastro_cid.html', {'form': form})