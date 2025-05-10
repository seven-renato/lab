resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "private-subnet"
  }
}

resource "aws_eip" "nat_eip" {
  domain = "vpc"
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "nat-gateway"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = {
    Name = "private-route-table"
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

resource "aws_instance" "wazuh" {
  ami                    = "ami-0c02fb55956c7d316"  # Amazon Linux 2 (região us-east-1)
  instance_type          = "t3.xlarge"
  subnet_id              = aws_subnet.public.id     # <-- está em subnet pública
  vpc_security_group_ids = [aws_security_group.wazuh_sg.id]
  key_name               = "infra-challenge-wazuh-key"         # <-- nome da chave criada na AWS

  tags = {
    Name = "wazuh-server"
  }
}

resource "aws_security_group" "wazuh_sg" {
  name        = "wazuh-sg"
  description = "SSH"
  vpc_id      = aws_vpc.main.id # Ligar a Vpc

  ingress { # Entrada de dados
    description = "SSH - Porta 22"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Pouco seguro, por[em] por n ser em producao manter assim
  }

  egress { # Saída de dados
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "wazuh-sg"
  }
}
