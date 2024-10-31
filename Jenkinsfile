pipeline {
    agent any

    environment {
        ARTIFACTORY_URL = 'https://your-artifactory-domain/artifactory'
        REPO_NAME = 'your-python-repo'  // The name of the repository in Artifactory
        PACKAGE_NAME = 'your_project_name'
        ARTIFACTORY_CRED_ID = 'artifactory-credentials' // Jenkins credentials ID for Artifactory
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                    // Set up virtual environment
                    sh "python3 --version"
                    sh "python3 -m venv ${VENV_DIR}"
                    sh "${VENV_DIR}/bin/pip install --upgrade pip setuptools wheel"
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh "${VENV_DIR}/bin/pip install -r requirements.txt"
                }
            }
        }

        stage('Build Package') {
            steps {
                script {
                    // Build the package
                    sh "${VENV_DIR}/bin/python setup.py sdist bdist_wheel"
                }
            }
        }

        stage('Publish to Artifactory') {
            steps {
                script {
                    // Authenticate with Artifactory and upload package
                    withCredentials([usernamePassword(credentialsId: "${ARTIFACTORY_CRED_ID}", usernameVariable: 'ARTIFACTORY_USER', passwordVariable: 'ARTIFACTORY_PASSWORD')]) {
                        // Use Twine for uploading the package to Artifactory
                        sh """
                            ${VENV_DIR}/bin/pip install twine
                            ${VENV_DIR}/bin/twine upload \
                            --repository-url ${ARTIFACTORY_URL}/${REPO_NAME} \
                            -u $ARTIFACTORY_USER -p $ARTIFACTORY_PASSWORD \
                            dist/*
                        """
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                deleteDir()  // Clean workspace after build
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
        success {
            echo 'Package successfully built and published!'
        }
        failure {
            echo 'Build or publishing failed.'
        }
    }
}
