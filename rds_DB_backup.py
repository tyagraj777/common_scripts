#Purpose: Automate daily snapshots for database recovery.

import boto3

rds = boto3.client('rds')

def backup_db():
    rds.create_db_snapshot(
        DBSnapshotIdentifier='daily-backup',
        DBInstanceIdentifier='my-database'
    )
    print("Snapshot created.")

backup_db()
