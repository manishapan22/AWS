import boto3
from datetime import datetime, timedelta

# Initialize AWS client
region = 'eu-north-1'
ec2 = boto3.client('ec2', region_name=region)

# Calculate the date threshold
date_threshold = datetime.now() - timedelta(days=1)
date_threshold_str = date_threshold.strftime('%Y-%m-%dT%H:%M:%SZ')

# Describe snapshots older than the threshold
snapshots = ec2.describe_snapshots(
    Filters=[{
        'Name': 'start-time',
        'Values': [f'[{date_threshold_str},]']
    }]
)

# Loop through and delete old snapshots
for snapshot in snapshots['Snapshots']:
    snapshot_id = snapshot['SnapshotId']
    print(f'Deleting snapshot {snapshot_id}')
    ec2.delete_snapshot(SnapshotId=snapshot_id)
