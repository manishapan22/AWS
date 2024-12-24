pipeline {
    agent any
    environment {
        REGION = 'eu-north-1'
    }
    stages {
        stage('Clone GitHub Repository') {
            steps {
                git 'https://github.com/manishapan22/AWS.git'  // Your GitHub repository URL
            }
        }

        stage('Run Snapshot Deletion Script') {
            steps {
                withAWS(credentials: 'aws-credentials') {
                    bat '''
                    C:\\Windows\\System32\\cmd.exe /c "Set-Location -Path 'C:\\Users\\manpan\\AWS' && python delete_snapshots.py"
                    '''
                }
            }
        }
    }
}
