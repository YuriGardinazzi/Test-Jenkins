pipeline {
    agent { docker { 
            image 'python:latest'
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
                sh 'pip3 install pandas'
                sh 'python3 test-python.py'
            }
        }
    }
}