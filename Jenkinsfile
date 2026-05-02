pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '=========================================='
                echo 'Building the HomeServer project...'
                echo '=========================================='
            }
        }

        stage('Test') {
            steps {
                echo '=========================================='
                echo 'Running tests...'
                echo '=========================================='
            }
        }

        stage('Deploy') {
            steps {
                echo '=========================================='
                echo 'Deploying HomeServer...'
                echo '=========================================='
            }
        }
    }

    post {
        success {
            echo '=========================================='
            echo 'Pipeline execution SUCCESSFUL ✓'
            echo '=========================================='
        }
        failure {
            echo '=========================================='
            echo 'Pipeline execution FAILED ✗'
            echo '=========================================='
        }
        always {
            echo 'Pipeline finished at: ' + new Date().format('yyyy-MM-dd HH:mm:ss')
        }
    }
}
