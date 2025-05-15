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
                // התקנת ספריות פייתון כולל Playwright
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                // התקנת הדפדפנים הדרושים ל-Playwright
                bat 'python -m playwright install'
            }
        }
        stage('Run Tests') {
            steps {
                // הפעלת הטסטים עם pytest (לפי ההגדרות שלך)
                bat 'pytest tests --junitxml=tests/report.xml'
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
