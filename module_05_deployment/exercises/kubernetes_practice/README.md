# Exercise: Kubernetes Practice

**Objective**: Write a Pod Manifest.

## 📝 Steps

1. Create `pod.yaml`.
2. Define a Pod named `nginx-pod` using image `nginx:alpine`.
3. Apply it: `kubectl apply -f pod.yaml`.
4. Port forward to access it: `kubectl port-forward nginx-pod 8080:80`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:alpine
```
