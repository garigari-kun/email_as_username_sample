from custom_user.forms import EmailUserCreationForm
from django.contrib.auth import(
	authenticate,
	login,
	logout,
	get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmailUserLoginForm
from dashboard.forms import BasicInfoForm
from dashboard.models import BasicInfo, GlobalInfo

from dashboard.utils import d



def home(request):
	template = 'accounts/index.html'
	return render(request, template, {})

def signin(request):
	template = 'accounts/signin.html'
	form = EmailUserCreationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data['password1']
		user.save()
		new_user = authenticate(email=user.email, password=password)
		login(request, new_user)
		return redirect('top')

	context = {
		'form': form,
	}
	return render(request, template, context)


def top(request):
	if not request.user.is_authenticated():
		return render(request, 'accounts/index.html', {})


	# BasicInfoモデルにデータがない、もしくはis_filledがfalseの場合、welcomeを表示し続ける
	try:
		basic_info = BasicInfo.objects.get(user=request.user)
	except BasicInfo.DoesNotExist:
		return redirect('welcome')

	template = 'accounts/top.html'
	return render(request, template, {})


def welcome(request):
	template = 'accounts/welcome.html'
	form = BasicInfoForm(request.POST or None)
	if request.POST:
		if form.is_valid():
			basic_info = form.save(commit=False)
			basic_info.user = request.user
			basic_info.is_filled = True
			# welcomeページの初期設定とともに、GlobalInfoのモデル作成。
			global_info = GlobalInfo(user=basic_info.user)

			basic_info.save()
			global_info.save()


			return redirect('dashboard')
	context = {
		'form': form,
	}
	return render(request,template, context)

def dashboard(request):
	template = 'accounts/dashboard.html'
	basicinfo = BasicInfo.objects.get(user=request.user)
	globalinfo = GlobalInfo.objects.get(user=request.user)
	# フリープランの期限を確認
	if globalinfo.trial_expired is False:
		created_date = globalinfo.created_date
		# フリープランの期限を確認し、この先の表示を分岐させる
		# return redirect('expired')


	context = {
		'basicinfo': 'basicinfo',
		'user': request.user,
	}
	return render(request, template, context)


def login_user(request):
	template = 'accounts/login.html'
	form = EmailUserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		authenticated_user = authenticate(email=email, password=password)
		login(request, authenticated_user)
		return redirect('top')

	context = {
		'form': form,
	}
	return render(request, template, context)
