pipeline {
    agent any

    environment {
        IMAGE = 'mustafaabdulhammed/python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm $IMAGE:$BUILD_NUMBER'
            }
        }

        stage('Release') {
            steps {
                withCredentials([usernamePassword(
                        credentialsId: 'docker',
                        usernameVariable: 'dockerUser',
                        passwordVariable: 'dockerPass')]) {
                    sh 'echo $dockerPass | docker login -u $dockerUser --password-stdin'
                    sh 'docker push $IMAGE:$BUILD_NUMBER'
                    sh 'docker push $IMAGE:latest'
                }
            }
        }
    }
}
