terraform {
  backend "s3" {
    bucket         = "my-terraform-states-unique-${data.aws_caller_identity.current.account_id}"
    key            = "network/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
  }
}
