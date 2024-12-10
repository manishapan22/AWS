import boto3
from datetime import datetime, timedelta

def delete_old_snapshots():
    ec2 = boto3.client('ec2')
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    one_day_ago = datetime.now() - timedelta(days=1)

    for snapshot in snapshots:
        start_time = snapshot['StartTime'].replace(tzinfo=None)
        if start_time < one_day_ago:
            print(f"Deleting snapshot {snapshot['SnapshotId']} from {start_time}")
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

if __name__ == "__main__":
    delete_old_snapshots()