pipeline {
    agent {
        docker {
            image 'python:3'
            label 'my-build-agent'
      }
    } 
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