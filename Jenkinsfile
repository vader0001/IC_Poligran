pipeline {
agent {
	docker { image 'python:3.9' }
}
stages {
	stage('Build') {
		steps {
			sh '''
				python -m venv .venv
				. .venv/bin/activate
				pip intall -r requirements.txt
				pytest -v
			'''
			sh 'pip3 install --user  -r requirements.txt'
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