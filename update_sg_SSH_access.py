import boto3
import requests

def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        print("Error fetching cuurent Ip Address : {e}")

def update_security_group(region, group_id, ip_permissions):
    # Update security group with new IP permissions
    ec2 = boto3.client('ec2', region_name = region)
    ec2.authorize_security_group_ingress(
        GroupId=group_id,
        IpPermissions=ip_permissions
    )

def main():
    # Get current IP address
    current_ip = get_current_ip()
    
    # Replace 'YOUR_SECURITY_GROUP_ID' with the ID of your security group
    security_group_id = 'sg-007078d168aba04f7'
    
    # Specify SSH port and protocol
    ip_permissions = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': f'{current_ip}/32'}]  # Allow SSH access only from current IP
        }
    ]

    # specifying region as "ap-south-1"
    region = 'ap-south-1'
    
    # Update security group
    update_security_group(region, security_group_id, ip_permissions)
    print(f'Successfully updated security group to allow SSH access from {current_ip}')

if __name__ == "__main__":
    main()