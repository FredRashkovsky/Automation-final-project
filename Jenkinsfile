pipeline {
    agent any 
    stages {
        stage('build') {
            agent { 
              docker { image 'python:3.10.1-alpine' }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}