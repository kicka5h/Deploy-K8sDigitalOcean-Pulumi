"""A Python Pulumi program"""

import pulumi
from pulumi_digitalocean import kubernetes_cluster
from pulumi_digitalocean import Provider

# Create a new Digital Ocean Kubernetes cluster in the sfo2 region.
do_cluster = kubernetes_cluster.KubernetesCluster("doCluster",
    name="galaxy-cluster",                                              
    region="sfo2",
    version="latest",
    node_pool={
        "name": "worker-pool",
        "size": "s-2vcpu-2gb",
        "nodeCount": 3
    }
)

# Export the cluster's endpoint and Kubeconfig.
pulumi.export("clusterEndpoint", do_cluster.endpoint)
pulumi.export("clusterKubeconfig", do_cluster.kube_configs[0]["rawConfig"])
