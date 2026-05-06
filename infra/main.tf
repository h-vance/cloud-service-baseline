resource "aws_instance" "service_node" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t3.micro"
  iam_instance_profile = aws_iam_instance_profile.app_profile.name

  vpc_security_group_ids = [aws_security_group.allow_service.id]

  metadata_options {
    http_tokens = "required" # Enforce IMDSv2
  }

  root_block_device {
    encrypted = true
  }

  tags = {
    Name        = "cloud-service-baseline-node"
    Environment = "production"
    ManagedBy   = "Terraform"
  }
}

resource "aws_iam_instance_profile" "app_profile" {
  name = "service-baseline-profile"
  role = aws_iam_role.service_role.name
}
