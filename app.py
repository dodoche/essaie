from kubernetes.client.rest import ApiException
from pprint import pprint

from kubernetes import client, config
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello(


#configuration = kubernetes.client.Configuration()

#config.load_kube_config()

  api_instance = client.CoreV1Api()
  name = "licence" # str | name of the ConfigMap
  namespace = 'default' # str | object name and auth scope, such as for teams and projects
  pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
  exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
  export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

  try:
      api_response = api_instance.read_namespaced_config_map(name, namespace, pretty=pretty, exact=exact, export=export)
      pprint( api_response.data)
  except ApiException as e:
      pprint("Exception when calling CoreV1Api->read_namespaced_config_map: %s\n" % e)
   )
 
  if __name__ == "__main__":
      application.run()
