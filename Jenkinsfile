pipeline {
   agent any
   tools {nodejs "newman"}
     parameters {
         string(name: 'apikey', defaultValue: '', description: 'api-postman-key')
     }
    stages {
        stage('build') {
            steps {
                sh "newman run https://api.getpostman.com/collections/19310415-9ceacf35-139d-4482-b6e1-b03f6fc16651?apikey=${params.apikey} --disable-unicode"
                sh 'pytest --html=report.html'
            }
            
        }
    }
    post{
        failure {  
            mail bcc: '', body: 'test Failed!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         } 
         changed {  
             mail bcc: '', body: 'test was ok!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         }
    }
}