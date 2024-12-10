pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'eu-north-1' // Set your AWS region
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/manishapan22/AWS.git'
            }
        }
        stage('List and Delete Snapshots') {
            steps {
                withAWS(credentials: 'aws-credentials') {
                    sh '.\delete_old_snapshots.py'
                }
            }
        }
    }
}
