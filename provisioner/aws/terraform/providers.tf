terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Left intentionally empty because we handle the authentication and region configuration trough environment variables.
provider "aws" {}