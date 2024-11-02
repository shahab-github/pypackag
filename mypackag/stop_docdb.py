import unittest
from unittest.mock import patch, MagicMock

# Import the function to be tested
# Assuming the function is in a module named docdb_manager
# from docdb_manager import stop_docdb_cluster

def stop_docdb_cluster(db_cluster_identifier):
    import boto3
    from botocore.exceptions import ClientError
    
    # Create a DocumentDB client
    client = boto3.client('docdb')

    try:
        # Describe the DB cluster to check if it exists
        response = client.describe_db_clusters(DBClusterIdentifier=db_cluster_identifier)
        
        # Check if the cluster exists
        if not response['DBClusters']:
            return f"Cluster with identifier '{db_cluster_identifier}' does not exist."

        # Get the cluster status
        cluster_status = response['DBClusters'][0]['Status']
        
        if cluster_status != 'available':
            return f"Cluster '{db_cluster_identifier}' is not in an available state. Current status: {cluster_status}"

        # Stop the DocumentDB cluster
        client.stop_db_cluster(DBClusterIdentifier=db_cluster_identifier)
        
        return f"Cluster '{db_cluster_identifier}' has been successfully stopped."

    except ClientError as e:
        # Handle specific client errors
        if e.response['Error']['Code'] == 'DBClusterNotFoundFault':
            return f"Cluster with identifier '{db_cluster_identifier}' does not exist."
        elif e.response['Error']['Code'] == 'InvalidDBClusterState':
            return f"Cluster '{db_cluster_identifier}' cannot be stopped because it is in the '{cluster_status}' state."
        else:
            return f"An error occurred: {e.response['Error']['Message']}"

