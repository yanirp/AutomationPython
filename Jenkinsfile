pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                echo 'שולף את הקוד מהמאגר...'
                git branch: 'main', url: 'https://github.com/yanirp/AutomationPython.git'
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'מגדיר סביבה וירטואלית...'
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                dir('tests') {
                    echo 'מריץ בדיקות...'
                    bat 'pytest --maxfail=1 --disable-warnings --junitxml=report.xml'
                }
            }
        }
    }
    
    post {
        always {
            echo 'מארכב תוצאות בדיקות...'
            archiveArtifacts artifacts: 'tests\\report.xml', allowEmptyArchive: true
            junit 'tests\\report.xml'
        }
    }
}
