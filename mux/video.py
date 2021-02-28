from __future__ import absolute_import
import mux_python
from mux_python.rest import ApiException
import re  
import six

from mux_python.api_client import ApiClient

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = '7b4e1705-11b3-4986-a710-87b97dfac3c1'
configuration.password = 'mWSjKW00kZTIYvB2lUY/nQdsF33O8deLU5bYsj1RQgZ51JGtryOuiInlkKUyvsy/GckOY4NSh5y'

# API Client Initialization
#assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
live_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))



class LiveStreamsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client


    def create_live_stream(self, create_live_stream_request, **kwargs):
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
             
            data=self.create_live_stream_with_http_info(create_live_stream_request, **kwargs) 
            print(data)
            return data
        else:
            (data) = self.create_live_stream_with_http_info(create_live_stream_request, **kwargs) 
            print(data)
            return data


new_asset_settings = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_live_stream_request = mux_python.CreateLiveStreamRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC], new_asset_settings=new_asset_settings)
create_live_stream_response = live_api.create_live_stream(create_live_stream_request)

# Give back the RTMP entry point playback endpoint
print("Stream Key: " + create_live_stream_response.data.stream_key)

