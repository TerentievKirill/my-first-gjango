from django.shortcuts import render
def device_list(request):
    return render(request, 'info/device_list.html', {})
