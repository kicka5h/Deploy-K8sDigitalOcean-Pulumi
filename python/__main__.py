"""A Python Pulumi program"""

import pulumi
from pulumi_digitalocean import kubernetes_cluster
from pulumi_digitalocean import Provider

# Define the DO token.
do_token = pulumi.Config("do_token")

do_provider=Provider("do-provider", token="YOUR_DIGITALOCEAN_TOKEN")

# Create a new Digital Ocean Kubernetes cluster in the sfo2 region.
do_cluster = kubernetes_cluster.KubernetesCluster("doCluster",
    region="sfo2",
    version="1.20.2-do.0",
    node_pool={
        "name": "worker-pool",
        "size": "s-2vcpu-2gb",
        "nodeCount": 3
    }
)

# Export the cluster's endpoint and Kubeconfig.
pulumi.export("clusterEndpoint", do_cluster.endpoint)
pulumi.export("clusterKubeconfig", do_cluster.kube_configs[0]["rawConfig"])
