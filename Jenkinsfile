pipeline {

    agent any

    environment {
        IMAGE_NAME = "anjana1234okok/flask-devops-project"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    parameters {
        string(name: 'CONTAINER_NAME', defaultValue: 'flask-container')
    }

    stages {

        stage('Clone Code') {
    steps {
        git branch: 'main',
        url: 'https://github.com/AnjanaMangamthara/flask-devops-project.git'
    }
}

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Docker Login') {
            steps {

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Deploy Container') {
            steps {

                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true

                docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
}
