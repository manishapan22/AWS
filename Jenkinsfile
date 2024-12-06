pipeline {
    agent any
 
    environment {
GITHUB_REPO = 'https://github.com/manishapan22/jenkins.git'  // Replace with your repository
        AWS_REGION = 'eu-north-1'  // Update to match your AWS region
    }
 
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GITHUB_REPO}" // Clone the GitHub repo
            }
        }
 
        stage('List and Delete Old Snapshots') {
            steps {
                script {
                    // Make the script executable
sh 'chmod +x snapshot-delete.sh'
                    
                    // Run the snapshot management script
sh './snapshot-delete.sh'
                }
            }
        }
    }
 
    post {
        always {
            echo "Snapshot management pipeline completed."
        }
    }
}
