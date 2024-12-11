#!/bin/bash

# Set AWS region
REGION="eu-north-1"

# Get snapshots older than 7 days and delete them
DATE_THRESHOLD=$(date -d "-1 days" +%Y-%m-%d)

# List and delete snapshots older than the threshold
aws ec2 describe-snapshots --region $REGION --query "Snapshots[?StartTime<'$DATE_THRESHOLD'].SnapshotId" --output text | \
while read snapshot_id; do
    if [[ -n "$snapshot_id" ]]; then
        echo "Deleting Snapshot: $snapshot_id"
        aws ec2 delete-snapshot --snapshot-id $snapshot_id --region $REGION
    fi
done
