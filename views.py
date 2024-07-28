from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Analysis
from .serializers import AnalysisSerializer
import pandas as pd
import openai

openai.api_key = 'your_openai_api_key'

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        data = pd.read_csv(file_obj)
        result = data.describe().to_dict()
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Explain the following data analysis: {result}",
            max_tokens=150
        )
        chatgpt_response = response.choices[0].text

        analysis = Analysis.objects.create(file=file_obj, result={'analysis': result, 'chatgpt_response': chatgpt_response})
        serializer = AnalysisSerializer(analysis)
        return Response(serializer.data)

def get_chatgpt_analysis(data):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Explain the following data analysis: {data}",
        max_tokens=150
    )
    return response.choices[0].text

