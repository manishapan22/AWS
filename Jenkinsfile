pipeline {
    agent any
    stages {
        stage('Clean Old Snapshots') {
            steps {
                script {
                    bat 'SNAPSHOT.py'
                }
            }
        }
    }
}
