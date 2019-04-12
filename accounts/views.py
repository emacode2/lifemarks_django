from django.shortcuts import render

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mark_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
