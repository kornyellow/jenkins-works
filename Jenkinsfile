pipeline {
    agent {
        label 'test'
    }
    environment {
        BASE_URL = "http://127.0.0.1:5000"
    }
    stages {
        stage('Clone API repository') {
            steps {
                git url: 'https://github.com/kornyellow/jenkins-works.git', branch: 'main'
            }
        }
        stage('Build and Test API') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'python3 app.py &'
                    sh 'sleep 3'
                    sh 'python3 test_unit.py'
                }
            }
        }
        stage('Build and Test Robot Framework') {
            steps {
                script {
                    dir('./robot3/') {
                        git url: 'https://github.com/kornyellow/jenkins-works-test.git', branch: 'main'
                    }
                    sh 'robot --variable BASE_URL:${BASE_URL} ./robot3/test_robot.robot'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t kornyellow/jenkins-works:latest .'
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockerhub-access-token', variable: 'DOCKER_HUB_ACCESS_TOKEN')]) {
                        sh 'echo $DOCKER_HUB_ACCESS_TOKEN | docker login --username kornyellow --password-stdin'
                        sh 'docker push kornyellow/jenkins-works:latest'
                    }
                }
            }
        }
        stage('Clean Workspace') {
            steps {
                sh 'docker compose down'
                sh 'docker system prune -a -f'
            }
        }
        stage('Composing Docker') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
        stage('Running Preprod') {
            agent {
                label 'preprod'
            }
            steps {
                sh 'docker pull kornyellow/jenkins-works:latest'
                sh 'docker compose down && docker system prune -a -f && docker compose up -d'
            }
        }
    }
}
