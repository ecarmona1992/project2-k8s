def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "648503940051.dkr.ecr.us-east-2.amazonaws.com/my-project-repo"
    }
    agent any
    // first step is to download git file
    stages {
        stage('download') {
            steps {
                git 'https://github.com/OthomDev/Project2'
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
                    
                    docker.build registry
                }
            }
        }
        // Uploading Docker images into AWS ECR
        stage('Pushing to ECR'){
            steps{
                
                sh "aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 648503940051.dkr.ecr.us-east-2.amazonaws.com"
                sh "docker push docker push 648503940051.dkr.ecr.us-east-2.amazonaws.com/my-project-repo:latest"
            }
        }
       
        
        

    }

}
