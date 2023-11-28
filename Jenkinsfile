pipeline {
    agent { docker {image 'python:3.12.0-alpine3.18'} } 
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
                
                sh 'python3 test-python.py'
            }
        }
    }
}