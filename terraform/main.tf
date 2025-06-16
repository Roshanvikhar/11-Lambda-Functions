provider "aws" {
  region = "ap-south-1"
}

# ✅ Create bucket (because it does not exist)
resource "aws_s3_bucket" "github_bucket" {
  bucket = "the-bucket-testing"
}

# ✅ Upload test file into the created bucket
resource "aws_s3_bucket_object" "uploaded_file" {
  bucket = aws_s3_bucket.github_bucket.id
  key    = "test-file.txt"
  source = "test-file.txt"
  etag   = filemd5("test-file.txt")
}

output "bucket_name" {
  value = aws_s3_bucket.github_bucket.id
}