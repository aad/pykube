import code

import pykube

config = pykube.KubeConfig.from_file()
api = pykube.HTTPClient(config)

context = {
    '__name__': '__console__',
    'pykube': pykube,
    'config': config,
    'api': api
}
for k, v in vars(pykube).items():
    if k[0] != '_' and k[0] == k[0].upper():
        context[k] = v

banner = f'''Pykube v{pykube.__version__}, loaded "{config.filename}" with context "{config.current_context}".

Example commands:
  [d.name for d in Deployment.objects(api)]              # get names of deployments in default namespace
  list(DaemonSet.objects(api, namespace='kube-system'))  # list daemonsets in "kube-system"
  Pod.objects(api).get_by_name('mypod').labels           # labels of pod "mypod"

Use Ctrl-D to exit'''

console = code.InteractiveConsole(locals=context)
console.interact(banner)
