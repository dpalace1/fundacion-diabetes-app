from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_qPunB5U6MDR8K1JTroREOgdr00vzCeVNzK"



def donation(request):
	return render(request, 'donation/donation.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'donation/success.html', {'amount':amount})
