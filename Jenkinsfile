def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "public.ecr.aws/x8y9i5i2/my-project-repo"
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
                sh "python3 test.py"
            }
        }

        stage('Build Image') {
            steps {
                script {
                    dockerImage = "docker build -t project2 ."
                }
            }
        }

       
        
        

    }

}
