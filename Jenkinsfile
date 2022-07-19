def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "524472057840.dkr.ecr.us-east-2.amazonaws.com/project2"
    }
    agent any
    // first step is to download git file
    stages {
        stage('download') {
            steps {
                git 'https://github.com/ecarmona1992/project2-k8s.git'
                echo 'Finshed downloading git'
                // force stop docker and clean up images
                sh "docker system prune -af"
            }
        }
        stage('testing') {
            steps {
                
                sh "pip3 install -r requirements.txt"
                sh "python3 -m pytest test.py"
            }
        }

        stage('Build Image') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    dockerimage = docker.build("${img}")
                }
            }
        }
        // Uploading Docker images into AWS ECR
        stage('Pushing to ECR'){
            steps{
                
                sh "aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 524472057840.dkr.ecr.us-east-2.amazonaws.com"
                sh "docker push "${dockerimage}""
            }
        }
        stage('K8S Deploy'){
            steps {
                withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'K8S', namespace: '', serverUrl: '') {
                    sh "kubectl apply -f eks-deploy-k8s-green.yaml"
                    sh "kubectl apply -f eks-deploy-k8s-blue.yaml"
                    sh "kubectl apply -f service.yml"
                }
            }
        }
        
        

    }

}
