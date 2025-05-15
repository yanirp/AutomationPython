pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                bat 'python -m playwright install'
            }
        }
        stage('Run Single Test') {
            steps {
                // מריצים את הבדיקות עם HEADLESS=false
                bat 'set HEADLESS=false && pytest tests/test_authority_page.py --junitxml=tests/report.xml'
            }
        }
    }

    post {
        always {
            junit 'tests/report.xml'
            archiveArtifacts 'tests/report.xml'
        }
    }
}
