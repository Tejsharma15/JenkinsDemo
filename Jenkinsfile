

pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Tejsharma15/JenkinsDemo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x program.py"
                sh "./program.py"
            }
        }
     stage('Test Pass Code') {
            steps {
                sh "chmod u+x testPass.py"
                sh "./testPass.py"
            }
        }
     stage('Test Fail Code') {
            steps {
                sh "chmod u+x testFail.py"
                sh "./testFail.py"
            }
        }
    } 
}
