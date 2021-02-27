from django.shortcuts import render

def Home(request):
    return render(request,'Converter/Home.html')

def Converter(request):

    peso=float(request.GET.get('peso'))

    riyals = peso * 0.077
    yen = peso * 2.19
    us_dollar = peso * 0.041
    c_dollar = peso * 0.026
    dirhams = peso * 0.075

    return render(request,'Converter/Converter.html',{'riyals':riyals,'yen':yen,'us_dollar':us_dollar,'c_dollar':c_dollar,'dirhams':dirhams})
