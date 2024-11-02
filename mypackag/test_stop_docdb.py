class TestStopDocDBCluster(unittest.TestCase):

    @patch('boto3.client')
    def test_cluster_exists_and_stopped(self, mock_boto_client):
        # Mock the describe_db_clusters response
        mock_client = MagicMock()
        mock_client.describe_db_clusters.return_value = {
            'DBClusters': [{'Status': 'available'}]
        }
        mock_boto_client.return_value = mock_client

        # Call the function
        result = stop_docdb_cluster('test-cluster')

        # Assert the expected outcome
        self.assertEqual(result, "Cluster 'test-cluster' has been successfully stopped.")
        mock_client.stop_db_cluster.assert_called_once_with(DBClusterIdentifier='test-cluster')

    @patch('boto3.client')
    def test_cluster_does_not_exist(self, mock_boto_client):
        # Mock the describe_db_clusters response for a non-existing cluster
        mock_client = MagicMock()
        mock_client.describe_db_clusters.return_value = {'DBClusters': []}
        mock_boto_client.return_value = mock_client

        # Call the function
        result = stop_docdb_cluster('non-existent-cluster')

        # Assert the expected outcome
        self.assertEqual(result, "Cluster with identifier 'non-existent-cluster' does not exist.")

    @patch('boto3.client')
    def test_cluster_not_available(self, mock_boto_client):
        # Mock the describe_db_clusters response for a cluster not in available state
        mock_client = MagicMock()
        mock_client.describe_db_clusters.return_value = {
            'DBClusters': [{'Status': 'stopped'}]
        }
        mock_boto_client.return_value = mock_client

        # Call the function
        result = stop_docdb_cluster('test-cluster')

        # Assert the expected outcome
        self.assertEqual(result, "Cluster 'test-cluster' is not in an available state. Current status: stopped.")

    @patch('boto3.client')
    def test_client_error_handling(self, mock_boto_client):
        # Mock the client to raise a DBClusterNotFoundFault
        mock_client = MagicMock()
        mock_client.describe_db_clusters.side_effect = ClientError(
            {"Error": {"Code": "DBClusterNotFoundFault", "Message": "Cluster not found."}},
            "DescribeDBClusters"
        )
        mock_boto_client.return_value = mock_client

        # Call the function
        result = stop_docdb_cluster('non-existent-cluster')

        # Assert the expected outcome
        self.assertEqual(result, "Cluster with identifier 'non-existent-cluster' does not exist.")

if __name__ == '__main__':
    unittest.main()
