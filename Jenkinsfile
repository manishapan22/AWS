pipeline {
    agent any
    environment {
        REGION = 'eu-north-1'  // Your AWS region
    }
    stages {
        stage('Clone GitHub Repository') {
            steps {
                // Clone the GitHub repository that contains the script
                git 'https://github.com/manishapan22/AWS.git' // Replace with your GitHub repo URL
            }
        }
        stage('Run Snapshot Deletion Script') {
            steps {
                withAWS(credentials: 'aws-credentials') {
                    // Navigate to the directory where the script is located and run it
                    bat '''
                    Set-Location -Path "C:\\Users\\manpan\\AWS"
                    python delete_snapshots.py 
                    '''
                }
            }
        }
    }
}
