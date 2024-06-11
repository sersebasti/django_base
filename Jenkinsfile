pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build steps here, for example:
                // sh 'mvn clean package'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test steps here, for example:
                // sh 'mvn test'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add your deploy steps here, for example:
                // sh 'scp target/my-app.war user@server:/path/to/deploy'
            }
        }
        
    }
}
/*
node{
    //grovy script
}
*/
