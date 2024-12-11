pipeline {
    agent any
    environment {
        // AWS credentials for Jenkins job
       // Add AWS secret key from Jenkins credentials
        withAWS(credentials: 'aws-credentials')
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
                script {
                    // Run the bash script to delete snapshots
                    sh '''
                    chmod +x delete_snapshots.sh
                    ./delete_snapshots.sh
                    '''
                }
            }
        }
    }
}
