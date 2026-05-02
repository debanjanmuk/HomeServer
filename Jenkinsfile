pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Build') {
            steps {
                echo '=========================================='
                echo 'Building the HomeServer project...'
                echo '=========================================='
                sh '''
                    python3 --version
                    python3 -m venv "$VENV_DIR"
                    . "$VENV_DIR/bin/activate"
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    echo "Build completed successfully."
                '''
            }
        }

        stage('Test') {
            steps {
                echo '=========================================='
                echo 'Running tests...'
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
