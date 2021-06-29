pipeline {
agent {
	docker { image 'python:3.6' }
}
stages {
	stage('Build') {
		steps {
			sh '''
				python -m venv .venv
				. .venv/bin/activate
				pip3 install -r requirements.txt
				python3.6 --version
			'''
		}
	}

	stage('Test') {
		steps {
			sh 'pwd'
			sh 'export PYTHONPATH=/var/lib/jenkins/workspace/Prueba_3_master/.venv/lib/python3.6/site-packages'
			sh 'PYTHONPATH=/var/lib/jenkins/workspace/Prueba_3_master/.venv/lib/python3.6/site-packages python3.6 manage.py test'
		}
	}

	stage('Deploy') {
		steps {
			sh 'echo not yet...'
		}
	}
}
}