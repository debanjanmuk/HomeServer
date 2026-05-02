pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '=========================================='
                echo 'Building the HomeServer project...'
                echo '=========================================='
                sh '''
                    echo "Current working directory:"
                    pwd
                    echo "Python version:"
                    python3 --version
                    echo "Installing dependencies..."
                    pip3 install -r requirements.txt || pip3 install flask requests werkzeug
                    echo "Build completed successfully!"
                '''
            }
        }

        stage('Test') {
            steps {
                echo '=========================================='
                echo 'Running tests...'
                echo '=========================================='
                sh '''
                    echo "Checking Python syntax..."
                    python3 -m py_compile server.py
                    python3 -m py_compile app.py
                    python3 -m py_compile config.py
                    python3 -m py_compile routes/*.py
                    python3 -m py_compile utils/*.py
                    echo "Syntax check completed!"
                    echo "Running basic imports test..."
                    python3 -c "import app; import config; from routes import basic, file_upload, chat; from utils import ai; print('All modules imported successfully!')"
                    echo "Test stage completed successfully!"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '=========================================='
                echo 'Deploying HomeServer...'
                echo '=========================================='
                sh '''
                    echo "Deployment started at: $(date)"
                    echo "Checking if userfiles directory exists..."
                    mkdir -p userfiles
                    echo "userfiles directory ready!"
                    echo "Starting HomeServer application..."
                    echo "Application would run on: http://127.0.0.1:8080"
                    echo "Available endpoints:"
                    echo "  - GET  / (Hello World)"
                    echo "  - GET  /home (Ahi and Ved page)"
                    echo "  - GET  /office (Office page)"
                    echo "  - GET  /file (File upload)"
                    echo "  - GET  /chat (AI Chat)"
                    echo "  - POST /api/chat (Chat API)"
                    echo "Deployment completed successfully!"
                    echo "Deployment finished at: $(date)"
                '''
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
