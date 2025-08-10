terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Get current AWS caller identity
data "aws_caller_identity" "current" {}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.3"

  cluster_name    = var.cluster_name
  cluster_version = "1.33"

  vpc_id     = var.vpc_id
  subnet_ids = var.subnet_ids

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.medium"]
      min_size     = 1
      max_size     = 3
      desired_size = 2
    }
  }

  # Enable cluster access logging
  cluster_enabled_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]

  # Configure cluster access
  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true
}

# Create access entry for current user
resource "aws_eks_access_entry" "current_user" {
  cluster_name  = module.eks.cluster_name
  principal_arn = data.aws_caller_identity.current.arn
  type          = "STANDARD"
}

# Create access policy association
resource "aws_eks_access_policy_association" "current_user_admin" {
  cluster_name  = module.eks.cluster_name
  principal_arn = data.aws_caller_identity.current.arn
  policy_arn    = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"

  access_scope {
    type = "cluster"
  }
}




