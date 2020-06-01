# featureflow.FeatureApi

All URIs are relative to *https://app.featureflow.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post4**](FeatureApi.md#create_using_post4) | **POST** /api/v2/features | Create a new feature
[**delete_using_delete4**](FeatureApi.md#delete_using_delete4) | **DELETE** /api/v2/features/{id} | Delete a feature
[**get_using_get4**](FeatureApi.md#get_using_get4) | **GET** /api/v2/features/{id} | Get a feature.
[**list_using_get4**](FeatureApi.md#list_using_get4) | **GET** /api/v2/features | Get all features
[**patch_feature_using_patch1**](FeatureApi.md#patch_feature_using_patch1) | **PATCH** /api/v2/features/{id} | Merge patch a feature
[**update_using_put4**](FeatureApi.md#update_using_put4) | **PUT** /api/v2/features | Update a feature

# **create_using_post4**
> object create_using_post4(body)

Create a new feature

Create a new feature with the given friendly name and unique key.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
body = featureflow.Feature() # Feature | feature

try:
    # Create a new feature
    api_response = api_instance.create_using_post4(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->create_using_post4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Feature**](Feature.md)| feature | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete4**
> delete_using_delete4(id)

Delete a feature

Delete a feature with the given id.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete a feature
    api_instance.delete_using_delete4(id)
except ApiException as e:
    print("Exception when calling FeatureApi->delete_using_delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get4**
> Feature get_using_get4(id)

Get a feature.

Returns a detail representation of a single feature for the given id or projectKey:featureKey

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get a feature.
    api_response = api_instance.get_using_get4(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->get_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Feature**](Feature.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get4**
> Features list_using_get4(feature_key=feature_key, project_key=project_key)

Get all features

Returns a summary list of all features within the organisation

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
feature_key = 'feature_key_example' # str | featureKey (optional)
project_key = 'project_key_example' # str | projectKey (optional)

try:
    # Get all features
    api_response = api_instance.list_using_get4(feature_key=feature_key, project_key=project_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->list_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**| featureKey | [optional] 
 **project_key** | **str**| projectKey | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_feature_using_patch1**
> Feature patch_feature_using_patch1(body, id)

Merge patch a feature

Patch a features specific value using json merge patch.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
body = 'body_example' # str | data
id = 'id_example' # str | id

try:
    # Merge patch a feature
    api_response = api_instance.patch_feature_using_patch1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->patch_feature_using_patch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| data | 
 **id** | **str**| id | 

### Return type

[**Feature**](Feature.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put4**
> Feature update_using_put4(body)

Update a feature

Update a feature with the given key.

### Example
```python
from __future__ import print_function
import time
import featureflow
from featureflow.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = featureflow.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = featureflow.FeatureApi(featureflow.ApiClient(configuration))
body = featureflow.Feature() # Feature | feature

try:
    # Update a feature
    api_response = api_instance.update_using_put4(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->update_using_put4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Feature**](Feature.md)| feature | 

### Return type

[**Feature**](Feature.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

