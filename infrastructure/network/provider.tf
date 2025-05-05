provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = {
      Terraform   = "true"
      Environment = "Dev"
      Application = "Pokemon App"
    }
  }
}

data "aws_caller_identity" "current" {}