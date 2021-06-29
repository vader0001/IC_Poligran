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
				export PYTHONPATH=/var/lib/jenkins/workspace/Prueba_3_master/.venv/lib/python3.9/site-packages
				pip3 install -r requirements.txt
				python3 --version
			'''
		}
	}

	stage('Test') {
		steps {
			sh 'python3 manage.py test'
		}
	}

	stage('Deploy') {
		steps {
			sh 'echo not yet...'
		}
	}
}
}