import pandas as pd
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import *
from rest_framework import status

from app.serializer import YourModelSerializer

class UploadView(APIView):
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        
        model_fields = Datamodels._meta.get_fields()
        field_names = [field.name for field in model_fields if field.concrete]
        
        print("------>>>>>field_names :: ",field_names)
        excel_file = 'app/randomData.xlsx' 
        
        df = pd.read_excel(excel_file)
        column_names = df.columns.tolist()
        print("-------->>>>column_names :: ",column_names)
        
        start_index = 1
        a = field_names[start_index:]
        print("------A----->>", a)
        
        # excel_file = request.FILES['Data.csv']
        # print(excel_file)
        if column_names == a:
            print(df.to_json())
            serializer = YourModelSerializer(data=df.to_dict(orient='records'), many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {
                "message" : "ALL DATA HAS BEEN UPLOADED IN DATA BASE"
            }

            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {
                "message" : "field name is not same as database"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)