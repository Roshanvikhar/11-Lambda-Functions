provider "aws" {
  region = "us-east-1"
}

# Use existing bucket instead of creating
data "aws_s3_bucket" "github_bucket" {
  bucket = "github-actions-terraform-test"
}

# Upload test file into existing bucket
resource "aws_s3_bucket_object" "uploaded_file" {
  bucket = data.aws_s3_bucket.github_bucket.id
  key    = "test-file.txt"
  source = "test-file.txt"
  etag   = filemd5("test-file.txt")
}

output "bucket_name" {
  value = data.aws_s3_bucket.github_bucket.id
}