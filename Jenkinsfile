pipeline {
    agent any
    stages {
        stage('Clean Old Snapshots') {
            steps {
                script {
                    sh 'SNAPSHOT.py'
                }
            }
        }
    }
}
