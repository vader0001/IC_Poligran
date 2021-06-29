pipeline {
agent {
	docker { image 'python:3.9' }
}
stages {
	stage('Build') {
		steps {
			sh 'pip --user install -r requirements.txt'
		}
	}

	stage('Test') {
		steps {
			sh 'python app/manage.py test'
		}
	}

	stage('Deploy') {
		steps {
			sh 'echo not yet...'
		}
	}
}
}