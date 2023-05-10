# import
import os

from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.anomalydetector.models import *

subscription_key = os.environ['ANOMALY_DETECTOR_SUBSCRIPTION_KEY']
endpoint = os.environ['ANOMALY_DETECTOR_ENDPOINT']

credential = AzureKeyCredential(subscription_key)
client = AnomalyDetectorClient(endpoint, credential)

# client = AnomalyDetectorClient(endpoint, subscription_key)

series = [TimeSeriesPoint(timestamp="2022-01-01T00:00:00Z", value=80.2),
          TimeSeriesPoint(timestamp="2022-01-02T00:00:00Z", value=76.5),
          TimeSeriesPoint(timestamp="2022-01-03T00:00:00Z", value=90.1),
          TimeSeriesPoint(timestamp="2022-01-04T00:00:00Z", value=93.1),
          TimeSeriesPoint(timestamp="2022-01-05T00:00:00Z", value=85.9),
          TimeSeriesPoint(timestamp="2022-01-06T00:00:00Z", value=83.5),
          TimeSeriesPoint(timestamp="2022-01-07T00:00:00Z", value=89.1),
          TimeSeriesPoint(timestamp="2022-01-08T00:00:00Z", value=84.3),
          TimeSeriesPoint(timestamp="2022-01-09T00:00:00Z", value=87.9),
          TimeSeriesPoint(timestamp="2022-01-10T00:00:00Z", value=92.6),
          TimeSeriesPoint(timestamp="2022-01-11T00:00:00Z", value=25.0),
          TimeSeriesPoint(timestamp="2022-01-12T00:00:00Z", value=91.2),]

request = UnivariateDetectionOptions(series=series,granularity=TimeGranularity.DAILY,)

change_point_response = client.detect_univariate_change_point(request)
anomaly_response = client.detect_univariate_entire_series(request)

print("Detecting the anomaly status of the latest data point.")

print(anomaly_response)