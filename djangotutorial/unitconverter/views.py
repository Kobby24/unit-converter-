from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def format_num(num, u):
    if num > 1:
        num = round(num, 3)
    if num >= 1000:
        return f"{num:,.2f}" + u
    return str(num) + u

# def check_input(inp,tem):
#     try:
#         inp = float(inp)
#     except ValueError:


def index(request):
    return render(request, 'index.html')


def answer(request, ans):
    print(ans)
    return render(request, 'answer.html', ans)


def length(request):
    if request.method == 'POST':
        len_num = request.POST.get("len-num")
        o_unit = request.POST.get("ounit")
        n_unit = request.POST.get("nunit")

        def convert(num, o_, n_):
            num1 = float(num)
            num = float(num)
            sym = ''
            if o_ == "Millimeters(mm)":
                if n_ == "Millimeters(mm)":
                    num = num
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num /= 10
                    sym = 'cm'
                elif n_ == "Decimetres(dm)":
                    num /= 100
                    sym = 'dm'
                elif n_ == "Metres(m)":
                    num /= 1000
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num /= 1000000
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'mm')
            elif o_ == "Centimetres(cm)":
                if n_ == "Millimeters(mm)":
                    num *= 10
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num = num
                    sym = 'cm'
                elif n_ == "Decimetres(dm)":
                    num /= 10
                    sym = 'dm'
                elif n_ == "Metres(m)":
                    num /= 100
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num /= 100000
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'cm')
            elif o_ == "Decimetres(dm)":
                if n_ == "Millimeters(mm)":
                    num *= 100
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 10
                    sym = 'cm'
                elif n_ == "Decimetres(dm)":
                    num = num
                    sym = 'dm'
                elif n_ == "Metres(m)":
                    num /= 10
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num /= 10000
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'dm')
            elif o_ == "Metres(m)":
                if n_ == "Millimeters(mm)":
                    num *= 1000
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 100
                    sym = 'cm'
                elif n_ == "Decimetres(dm)":
                    num *= 10
                    sym = 'dm'
                elif n_ == "Metres(m)":
                    num = num
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num /= 1000
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'm')
            elif o_ == "Kilometres(km)":
                if n_ == "Millimeters(mm)":
                    num *= 1000000
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 100000
                    sym = 'cm'
                elif n_ == "Decimetres(dm)":
                    num *= 10000
                    sym = 'dm'
                elif n_ == "Metres(m)":
                    num *= 1000
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num = num
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'km')

        ans = convert(len_num, o_unit, n_unit)
        return answer(request, {'ans': ans[0], "num": ans[1], 'path': 'length'})
    return render(request, 'length.html')


def temp(request):
    if request.method == 'POST':
        temp_num = request.POST.get("temp-num")
        o_unit = request.POST.get('ounit')
        n_unit = request.POST.get('nunit')

        def convert(num, o_, n_):
            sym = ''
            num1 = float(num)
            num = float(num)
            if o_ == "Kelvin(K)":
                if n_ == 'Kelvin(K)':
                    sym = "K"
                    num = num

                elif n_ == "Celsius(C)":
                    sym = "°C"
                    num -= 273.15

                elif n_ == "Fahrenheit(F)":
                    num = (9 / 5) * (num - 273.15) + 32
                    sym = "°F"
                return format_num(num, sym), format_num(num1, 'K')
            elif o_ == "Celsius(C)":
                if n_ == "Kelvin(K)":
                    num += 273.15
                    sym = 'K'

                elif n_ == "Celsius(C)":
                    num = num
                    sym = '°C'
                elif n_ == "Fahrenheit(F)":
                    num = (9 / 5) * num + 32
                    sym = '°F'
                return format_num(num, sym), format_num(num1, '°C')
            elif o_ == "Fahrenheit(F)":
                if n_ == "Fahrenheit(F)":
                    num = num
                    sym = '°F'
                elif n_ == "Celsius(C)":
                    num = (num - 32) * (5 / 9)
                    sym = '°C'
                elif n_ == "Kelvin(K)":
                    num = (num - 32) * (5 / 9) + 273.15
                    sym = 'K'
                return format_num(num, sym), format_num(num1, "°F")

        ans = convert(temp_num, o_unit, n_unit)
        return answer(request, {'ans': ans[0], "num": ans[1], 'path': 'temp'})
    return render(request, 'temp.html')


def weight(request):
    if request.method == 'POST':
        weight_num = request.POST.get("weight-num")
        o_unit = request.POST.get("ounit")
        n_unit = request.POST.get("nunit")

        def convert(num, o_, n_):
            sym = ''
            num1 = float(num)
            num = float(num)
            if o_ == "Kilogramme(kg)":
                if n_ == "Kilogramme(kg)":
                    num = num
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num *= 1000
                    sym = 'g'
                elif n_ == "Tonnes(t)":
                    num *= 0.001
                    sym = 't'

                return format_num(num, sym), format_num(num1, "kg")
            elif o_ == "Grammes(g)":
                if n_ == "Kilogramme(kg)":
                    num *= 0.001
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num = num
                    sym = 'g'
                elif n_ == "Tonnes(t)":
                    num *= 0.000001
                    sym = 't'

                return format_num(num, sym), format_num(num1, 'g')
            elif o_ == "Tonnes(t)":
                if n_ == "Kilogramme(kg)":
                    num *= 1000
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num *= 1000000
                    sym = 'g'
                elif n_ == "Tonnes(t)":
                    sym = 't'
                    num = num

                return format_num(num, sym), format_num(num1, 't')

        ans = convert(weight_num, o_unit, n_unit)

        return answer(request, {'ans': ans[0], "num": ans[1],'path':'weight'})
    return render(request, 'weight.html')
