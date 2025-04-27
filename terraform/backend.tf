terraform {
  backend "s3" {
    bucket         = "github-actions-terraform-test"  # Your S3 bucket for storing state
    key            = "terraform/state.tfstate"              # Path within the bucket to store the state file
    region         = "us-east-1"                            # AWS region for the S3 bucket
  }
}