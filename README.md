# AWS EC2 Instance SSH Management Script

This repository contains Python scripts for managing AWS EC2 instances and security groups. These scripts automate the process of updating security group rules to enable secure and convenient remote access to EC2 instances from dynamic IP addresses.

## Features

- Automatically updates security group rules to allow SSH access from the current IP address.
- Simplifies IP whitelisting for accessing EC2 instances securely.
- Easily configurable for various AWS regions and EC2 instance configurations.

## Prerequisites

Before using these scripts, ensure you have the following:

- Python installed on your system
- Boto3 library for Python (`pip install boto3`)
- AWS credentials with appropriate permissions to manage EC2 instances and security groups

## Usage

1. Clone or download this repository to your local machine.
2. Configure your AWS credentials using AWS CLI (`aws configure`) or environment variables.
3. Run the Python script `update_security_group.py` before connecting to your EC2 instance.
4. Follow the prompts to update the security group rules to allow SSH access from your current IP address.
