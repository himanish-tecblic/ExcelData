import pandas as pd
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import YourModelSerializer

class UploadView(APIView):
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        # excel_file = request.FILES['Data.csv']
        excel_file = 'app/Data.xlsx' 
        print(excel_file)
        df = pd.read_excel(excel_file)  # Read the Excel file using pandas

        serializer = YourModelSerializer(data=df.to_dict(orient='records'), many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=201)
