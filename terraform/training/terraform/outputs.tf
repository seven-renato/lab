output "ec2_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.wazuh.public_ip
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public.id
}
