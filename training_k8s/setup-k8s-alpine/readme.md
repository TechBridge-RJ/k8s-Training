# Setup OS
setup-alpine
us
us-alt-intl

192.168.0.101
192.168.0.1

google.com
8.8.8.8

busybox

uncomment 
community /etc/apk/repositories
add 
http://dl-cdn.alpinelinux.org/alpine/edge/community
http://dl-cdn.alpinelinux.org/alpine/edge/testing

apk add sudo 
run visudo and uncomment %wheels

adduser control wheel # control
adduser worker wheel # worker

vi /etc/ssh/sshd_config # AllowTCP yes
rc-service sshd restart

# https://wiki.alpinelinux.org/wiki/K8s

# Setup network
sudo echo "br_netfilter" > /etc/modules-load.d/k8s.conf
sudo modprobe br_netfilter
sudo sysctl net.ipv4.ip_forward=1
sudo echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sudo echo "net.bridge.bridge-nf-call-iptables=1" >> /etc/sysctl.conf
sudo sysctl net.bridge.bridge-nf-call-iptables=1

sudo control #control
sudo worker #worker
# Getting K8s packages
sudo apk add cni-plugin-flannel
sudo apk add cni-plugins
sudo apk add flannel
sudo apk add flannel-contrib-cni
sudo apk add kubelet
sudo apk add kubeadm
sudo apk add kubectl
sudo apk add containerd
sudo apk add uuidgen
sudo apk add nfs-utils

# Configure FSTAB
sudo cp -av /etc/fstab /etc/fstab.bak
sudo sed -i '/swap/s/^/#/' /etc/fstab
sudo swapoff -a

# install components
sudo rc-update add containerd
sudo rc-update add kubelet
sudo rc-service containerd start

# symlink calico
sudo ln -s /opt/cni/bin/calico /usr/libexec/cni/calico
sudo ln -s /opt/cni/bin/calico-ipam  /usr/libexec/cni/calico-ipam

# configure unified cgroup
sudo vi /etc/rc.conf uncomment rc_cgroup_mode="unified"

# Configure mount
mount --make-rshared /
sudo echo "#!/bin/sh" > /etc/local.d/sharemetrics.start
echo "mount --make-rshared /" >> /etc/local.d/sharemetrics.start
chmod +x /etc/local.d/sharemetrics.start
rc-update add local
uuidgen > /etc/machine-id

# configure config.toml
sudo sed -i 's/pause:3.8/pause:3.10/' /etc/containerd/config.toml


# Initializae kubernetes cluster
sudo kubeadm init --pod-network-cidr=10.80.0.0/16

# Configure Kubectl - on control node
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install Pod Network - on control node
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml

# Print Join cmd - on control node
kubeadm token create --print-join-command 

# Worker join - on worker node
kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>