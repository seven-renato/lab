provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "wazuh-terraform-state-bucket-defensepoint"
    key    = "infra/terraform.tfstate"
    region = "us-east-1"
  }
}
