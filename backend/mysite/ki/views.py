from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from django.conf import settings
from django.http import HttpResponse
from msrest.authentication import ApiKeyCredentials
from rest_framework import viewsets, mixins, serializers, status
from rest_framework.response import Response

from .models import WeekPlan
from .serializers import WeekPlanSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


class WeekPlanViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WeekPlan.objects.all()
    serializer_class = WeekPlanSerializer

    def create(self, request, *args, **kwargs):
        prediction_data = self.send_ai_req(request.FILES['image'])
        serializer = PredictionSerializer(data=prediction_data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_ai_req(self, image):
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": settings.CV_PREDICTION_KEY})
        predictor = CustomVisionPredictionClient(endpoint=settings.CV_PREDICTION_ENDPOINT, credentials=credentials)

        results = predictor.classify_image(settings.CV_PROJECT_ID, settings.CV_MODEL_NAME, image.read())

        # Display the results.
        print(results)
        prediction_results = list()
        for prediction in results.predictions:
            print(prediction.__dict__)
            prediction_results.append({"tag_id": prediction.tag_id, "tag_name": prediction.tag_name,
                                       "probability": "{0:.2f}%".format(prediction.probability * 100)})

        return prediction_results


class PredictionSerializer(serializers.Serializer):
    tag_id = serializers.CharField()
    tag_name = serializers.CharField()
    probability = serializers.CharField()
