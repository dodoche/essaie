from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint


    
  # Configure API key authorization: BearerToken
  configuration = kubernetes.client.Configuration()
  #configuration.api_key['authorization'] = 'YOUR_API_KEY'
  # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
  # configuration.api_key_prefix['authorization'] = 'Bearer'

  # create an instance of the API class
  api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
  name = "licence" # str | name of the ConfigMap
  namespace = 'default' # str | object name and auth scope, such as for teams and projects
  pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
  exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
  export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

  try:
     api_response = api_instance.read_namespaced_config_map(name, namespace, pretty=pretty, exact=exact, export=export)
     pprint(api_response)
  except ApiException as e:
     print("Exception when calling CoreV1Api->read_namespaced_config_map: %s\n" % e)
