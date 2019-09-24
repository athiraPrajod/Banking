from django.shortcuts import render,redirect
from .models import Accounts
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
user = None
def Home(request):
	return render(request, 'Home.html')

def login(request):
	#user = User.objects.create_user('sample1', 12345, 1, 'Sample User', 10000, 'sample@lenzbank.com')
	if(request.method == "POST"):
		data = request.POST
		username = request.POST['username']
		password = request.POST['password']
		info = Accounts.objects.all()
		print(username, password)
		index = 0
		
		for i in range(0, len(info)):
			print(info[i].UserName, info[i].Password, "\n")
			if(username == info[i].UserName and password == info[i].Password):
				index = i

		

		#user = authenticate(username=info[0].UserName, password=info[0].Password)			
		
		#if user is not None:
		if(username == info[index].UserName and password == info[index].Password):
			global user
			user = username
			print("Success")
			return render(request, 'Home.html')
		else:
			#print(Accounts.UserName, username)
			print("Invalid username or password.")
			return render(request, 'Login.html')

	else:
		return render(request, 'Login.html')
	


def Sign_Up2(request):
	if(request.method == "POST"):
		data = request.POST
		username = request.POST['username']
		password = request.POST.get('password')
		full_name = request.POST.get('FullName')
		email = request.POST.get('E_ID')
		print(username, password, full_name, email)
		info = Accounts(UserName = username, Password = password, Account_No = 2, Customer_Name = full_name, Curr_Balance = 10000, email = email)
		info.save()
		global user 
		user = username
		return render(request, 'Home.html')

	else:
		return render(request, 'Sign_Up2.html')

def transaction(request):
	if(request.method == "POST"):
		
		data = request.POST
		#print(data, "\n")
		payee=data["payee"]
		acc_no=data["acc_no"]
		amount=data["amount"]
		info = Accounts.objects.all()
		#print(info, "\n")
		index1, index2 = 0, 0
		for i in range(0, len(info)):
			#print(info[i].UserName, "\n")
			if(payee == info[i].UserName):
				index1 = i
		global user
		print(user)
		for i in range(0, len(info)):
			#print(info[i].UserName, "\n")
			
			if(user == info[i].UserName):
				index2 = i
	
		#adding the same amount in the second account
		info[index1].Curr_Balance = int((info[index1].Curr_Balance)) + int(amount)
		print(info[index1].Curr_Balance, "\n")
		#subtracting the amount from tne account 1
		info[index2].Curr_Balance = int((info[index2].Curr_Balance)) - int(amount)
		print(info[index2].Curr_Balance, "\n")
		return render(request, 'personal_banking.html')
	else:
		return render(request, 'Transactions.html')
        #return render(request, 'personal_banking.html')
	
def personal_bank(request):
        info=Accounts.objects.all()
        return render(request, 'personal_banking.html', {'details':info})
