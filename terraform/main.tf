provider "aws" {
  region = "us-east-1"
}

data "aws_s3_bucket" "github_bucket" {
  bucket = "github-actions-terraform-test"
}

resource "aws_s3_bucket_object" "uploaded_file" {
  bucket = aws_s3_bucket.github_bucket.id
  key    = "test-file.txt"
  source = "test-file.txt" # This file must exist locally
  etag   = filemd5("test-file.txt")
}

output "bucket_name" {
  value = aws_s3_bucket.github_bucket.id
}