variable "aws_region" {
  default = "us-east-1"
}

variable "cluster_name" {
  default = "product-eks-cluster"
}

variable "vpc_id" {
  description = "VPC ID where the EKS cluster will be deployed"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for the EKS nodes"
  type        = list(string)
}

variable "key_name" {
  description = "EC2 key pair name for SSH access to nodes"
  type        = string
  default     = ""
}

