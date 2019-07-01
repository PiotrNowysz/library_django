from django.shortcuts import render
from django.views import View


# Create your views here.
class UserCreateView(View):
    def get(self, request):
        user_form = forms.UserCreateForm()

        return render(request, 'registration/user_create.html', {'user_form': user_form, })

    def post(self, request):
        user_form = forms.UserCreateForm(request.POST)
        details_form = forms.UserDetailsForm(request.POST)
        if user_form.is_valid() and details_form.is_valid():
            user = user_form.save()
            UserDetails.objects.create(user=user)
            return redirect('/login/')
        else:
            return render(request, 'registration/user_create.html', {'user_form': user_form,
                                                                     'details_form': details_form})
