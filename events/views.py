from rest_framework.views import (
    APIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from .serializers import (
    EventSerializer,
    EventRegisterSerializer
)
from rest_framework import viewsets
from .models import (
    Event,
    EventRegisterUser
)

from rest_framework import (
    parsers,
)
from RVK_WEBPORTAL.permissions import(
    IsHR,
    RegistrationLimit,
    IsFinance
)
import razorpay
from rest_framework.response import Response
from accounts.models import(
    User
)



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [IsHR]


class EventRegisterViewSet(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    


    def post(self, request):
        TotallRegisterUser = EventRegisterUser.objects.all().count()
        EventCapacity = Event.objects.first().capacity

        

        # print("Capacity======================================",Event.objects.first().capacity)

        # print("Event=============================================",TotallRegisterUser)

        

        eventregister_model = EventRegisterUser.objects.all()
        serializer = EventRegisterSerializer(eventregister_model, many=True)
        
        KEY_ID = "rzp_test_2y68LXTdn3DKK9"
        KEY_SECRET = "GU6RrUGnP2KId7WFSrMULPus"

        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
        amount = request.data.get('amount')
        currency = "INR"


        data = {"amount": amount, "currency": currency}
        event_register = client.order.create(data=data)
        print(event_register["id"])


        if TotallRegisterUser <= EventCapacity:
            EventRegisterUser.objects.create(
                user = request.user,
                first_name = request.data.get('first_name'),
                last_name = request.data.get('last_name'),
                email = request.data.get('email'),
                phone_number = request.data.get('phone_number'),

                smart_card_number = request.data.get('smart_card_number'),
                address = request.data.get('address'),

                pin_code = request.data.get('pin_code'),
                city = request.data.get('pin_code'),
                state = request.data.get('state'),
                country = request.data.get('country'),


                
                amount=event_register["amount"],
                payment_id=event_register["id"],
                order_date=event_register["created_at"],
                is_pay = True
            )

            return Response({
                    "message":"Thank For Registration",
                    "donation details": event_register
                }
                
            )
        
        return Response({
                "message":"You can't register at the moment, event registration capacity is already over."
            }
            
        )
            

       



        

    def get(self,request):
        eventregister_model = EventRegisterUser.objects.all()
        serializer = EventRegisterSerializer(eventregister_model, many=True)
        if request.user.groups.filter(name='Finance Department').exists():
            return Response(
                {
                    "message":"data fetch successfully",
                    "data":serializer.data
                }
            )
        else:
            return Response(
                {
                    "message":"You don't have permission"
                }
            )
        
class EventRegisterForFinanceViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    


