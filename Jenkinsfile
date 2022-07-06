def img
pipeline {
    // setting up dockhub information needed to push image.
    environment {
        registry = "ecarmona1992/project1"
        registrycredential = 'docker-hub-login'
        dockerimage = ''
    }
    agent any
    // first step is to download git file
    stages {
        stage('download') {
            steps {
                git 'https://github.com/ecarmona1992/flask-jenkins'
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
                    // reference: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/
                    img = registry + ":${env.BUILD_ID}"
                    // reference: https://docs.cloudbees.com/docs/admin-resources/latest/plugins/docker-workflow
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
                        // push image to registry
                        dockerImage.push()
                    }
                }
            }
        }

    }

// send email notification once everything completes
    post {
        always {
            
            emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            
        }
    }
}