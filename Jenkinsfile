pipeline{
    agent any
    stages{
        stage("Checkout code"){
            steps{
                git url:'https://github.com/pandurangfunde/Project1.git',branch:'main'
            }
        }
        stage("Build Docker image") {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage("Create Container") {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    
    }


}