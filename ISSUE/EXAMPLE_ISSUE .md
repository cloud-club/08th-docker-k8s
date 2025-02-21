## Summary

cross-AZ 통신에 대해서 보다보니 AWS VPC CNI 를 자연스럽게 보게 되었습니다.

A pod -> B pod 로 갈 때 다른 data plane 이라면 cross-AZ 통신이 되는데 이때 트래픽이 외부로 흘러가지 않고 내부로 통신할텐데 이 과정에 대해서 궁금한 상황입니다.

## Description

### Context

큰 그림에서의 트래픽 흐름은 설명할 수 있지만 좀 더 자세하게 들여다보면 제대로 이해하지 못한 것 같아요

### What I tried

- AWS VPC CNI 에 대해서 공식 문서를 찾아보았지만, 제가 찾은 문서에서는 이에 대한 설명이 없었습니다.

### Resources/References

- https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/cni-proposal.md
- https://medium.com/techblog-hayleyshim/aws-eks-networking-698368b77723
- https://gasidaseo.notion.site/Istio-Life-of-a-packet-6ad9808e14594296bf854dcc203cab71

### Additional Context

- istio ingress-gateway만 있는 상태에서 req에 대한 res를 주는 과정에서의 흐름
