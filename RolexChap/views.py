from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook(request):
    data = json.loads(request.body)
    
    cost = 500

    queryset = data.get('queryResult').get('parameters')
    item = queryset.get('RolexTopping')
    quantity = queryset.get('number')
    item1 = queryset.get('RolexTopping1')
    quantity1 = queryset.get('number1')

    salads = []
    for k,v in queryset.items():
        if queryset.get(k):
            salads.append(v)

    salads = ', '.join(salads[4:])

    total = (quantity + quantity1 ) * cost

    

    if salads:
        text = f"{item}: {quantity}, \n{item1}: {quantity1}, \nSalads: {salads} \n\nTotal: {total}"
    text = f"{item}: {quantity}, \n{item1}: {quantity1}, \n\nTotal: {total}"


    return JsonResponse({"fulfillmentText": text}, safe=False)


'''
{'number': 2.0, 'RolexTopping': 'Chapatti', 'number1': 1.0, 'RolexTopping1': 'Egg', 'RolexToppingFriedOnionSalad': 'Onions', 'RolexToppingRawTomatoSalad': 'Raw tomato', 'RolexToppingFriedTomatoSalad': '', 'RolexToppingRawOnionSalad': ''}
'''