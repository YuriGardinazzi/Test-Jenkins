pipeline {
    agent  any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
                sh 'apt-get install python3'
                sh 'python3 test-python.py'
            }
        }
    }
}