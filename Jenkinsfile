pipeline {
    agent { docker { 
            image 'python:latest'
            args  '--net="jenkins_network"'}
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
                sh 'pip3 install pandas numpy elabapi-python'
                sh 'python3 test-python.py'
            }
        }
    }
}