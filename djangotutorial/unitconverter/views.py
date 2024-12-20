
from django.shortcuts import render


# Create your views here.
def format_num(num, u):
    if num > 1:
        num = round(num, 3)
    if num >= 1000:
        return f"{num:,.2f}" + u
    return str(num) + u


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
                elif n_ == "Inches(in)":
                    num /= 25.4
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num /= 304.8
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num /= 914.4
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num /= 1609344
                    sym = 'mi'
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
                elif n_ == "Inches(in)":
                    num *= 0.3937
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num *= 0.0328084
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num *= 0.0109361
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num *= 0.0000062137
                    sym = 'mi'
                elif n_ == "Metres(m)":
                    num /= 100
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num /= 100000
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'cm')
            elif o_ == "Inches(in)":
                if n_ == "Millimeters(mm)":
                    num *= 25.4
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 2.54
                    sym = 'cm'
                elif n_ == "Inches(in)":
                    num = num
                    sym = 'in'
                elif n_ == "Metres(m)":
                    num *= 0.0254
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num *= 0.0000254
                    sym = 'km'
                elif n_ == 'Foot(ft)':
                    num /= 12
                    sym = 'ft'
                elif n_ == "Yard(yd)":
                    num /= 36
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num /= 63360
                    sym = 'mi'
                return format_num(num, sym), format_num(num1, 'in')
            elif o_ == "Metres(m)":
                if n_ == "Millimeters(mm)":
                    num *= 1000
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 100
                    sym = 'cm'
                elif n_ == "Inches(in)":
                    num *= 39.3701
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num *= 3.28084
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num *= 1.09361
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num /= 1609.344
                    sym = 'mi'
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
                elif n_ == "Inches(in)":
                    num *= 39370.1
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num *= 3280.84
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num *= 1093.61
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num *= 0.621371
                    sym = 'mi'
                elif n_ == "Metres(m)":
                    num *= 1000
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num = num
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'km')
            elif o_ == 'Foot(ft)':
                if n_ == "Millimeters(mm)":
                    num *= 304.8
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 30.48
                    sym = 'cm'
                elif n_ == "Inches(in)":
                    num *= 12
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num = num
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num /= 3
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num /= 5280
                    sym = 'mi'
                elif n_ == "Metres(m)":
                    num *= 0.3048
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num *= 0.0003048
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'ft')
            elif o_ == 'Yard(yd)':
                if n_ == "Millimeters(mm)":
                    num *= 914.4
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 91.44
                    sym = 'cm'
                elif n_ == "Inches(in)":
                    num *= 36
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num *= 3
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num = num
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num /= 1760
                    sym = 'mi'
                elif n_ == "Metres(m)":
                    num *= 0.9144
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num *= 0.0009144
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'yd')
            elif o_ == 'Mile(mi)':
                if n_ == "Millimeters(mm)":
                    num *= 1609344
                    sym = 'mm'
                elif n_ == "Centimetres(cm)":
                    num *= 160934.4
                    sym = 'cm'
                elif n_ == "Inches(in)":
                    num *= 63360
                    sym = 'in'
                elif n_ == 'Foot(ft)':
                    num *= 5280
                    sym = 'ft'
                elif n_ == 'Yard(yd)':
                    num *= 1760
                    sym = 'yd'
                elif n_ == 'Mile(mi)':
                    num = num
                    sym = 'mi'
                elif n_ == "Metres(m)":
                    num *= 1609.344
                    sym = 'm'
                elif n_ == "Kilometres(km)":
                    num *= 1.609344
                    sym = 'km'
                return format_num(num, sym), format_num(num1, 'mi')

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
                elif n_ == "Milligram(mg)":
                    num *= 1000000
                    sym = 'mg'
                elif n_ == 'Pound(lb)':
                    num *= 2.20462
                    sym = 'lb'
                elif n_ == 'Ounce(oz)':
                    num *= 35.274
                    sym = 'oz'
                return format_num(num, sym), format_num(num1, "kg")
            elif o_ == "Grammes(g)":
                if n_ == "Kilogramme(kg)":
                    num *= 0.001
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num = num
                    sym = 'g'
                elif n_ == "Milligram(mg)":
                    num *= 1000
                    sym = 'mg'
                elif n_ == 'Pound(lb)':
                    num /= 453.59237
                    sym = 'lb'
                elif n_ == 'Ounce(oz)':
                    num /= 28.3495
                    sym = 'oz'
                return format_num(num, sym), format_num(num1, 'g')
            elif o_ == "Milligram(mg)":
                if n_ == "Kilogramme(kg)":
                    num /= 1000000
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num /= 1000
                    sym = 'g'
                elif n_ == "Milligram(mg)":
                    sym = 'mg'
                    num = num
                elif n_ == 'Pound(lb)':
                    sym = 'lb'
                    num /= 453592.37
                elif n_ == 'Ounce(oz)':
                    sym = 'oz'
                    num /= 28349.5
                return format_num(num, sym), format_num(num1, 'mg')
            elif o_ == 'Pound(lb)':
                if n_ == "Kilogramme(kg)":
                    num *= 0.45359237
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num *= 453.59237
                    sym = 'g'
                elif n_ == "Milligram(mg)":
                    sym = 'mg'
                    num *= 453592370
                elif n_ == 'Pound(lb)':
                    sym = 'lb'
                    num = num
                elif n_ == 'Ounce(oz)':
                    sym = 'oz'
                    num *= 16
                return format_num(num, sym), format_num(num1, 'lb')
            elif o_ == 'Ounce(oz)':
                if n_ == "Kilogramme(kg)":
                    num *= 0.0283495
                    sym = 'kg'
                elif n_ == "Grammes(g)":
                    num *= 28.3495
                    sym = 'g'
                elif n_ == "Milligram(mg)":
                    sym = 'mg'
                    num *= 28349.5
                elif n_ == 'Pound(lb)':
                    sym = 'lb'
                    num /= 16
                elif n_ == 'Ounce(oz)':
                    sym = 'oz'
                    num = num
                return format_num(num, sym), format_num(num1, 'oz')
        ans = convert(weight_num, o_unit, n_unit)

        return answer(request, {'ans': ans[0], "num": ans[1],'path':'weight'})
    return render(request, 'weight.html')
