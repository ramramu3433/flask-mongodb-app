pipeline {
   agent { node 'Banking' }
   stages{
       stage('build'){
            steps{
                  checkout scm
                  echo 'Building $GIT_COMMIT on $NODE_NAME with $BUILD_NUMBER'
               }
}
        stage('deploy'){
             steps{
                 ansiblePlaybook extras: '--extra-vars "deployment_folder=/home/janakiraman/application_"  --extra-vars "version=$BUILD_NUMBER"', installation: 'ansible', playbook: 'playbook.yml'
}
  }
  }
   }


               
