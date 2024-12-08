pipeline {
    agent any
    stages {
        stage('Clean Old Snapshots') {
            steps {
                script {
                    powershell 'SNAPSHOT.ps1'
                }
            }
        }
    }
}
