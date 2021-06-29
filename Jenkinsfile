pipeline {
agent {
	docker { image 'python:3.6' }
}
triggers {
	githubPush()
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
	stage('Notify Sentry of deployment') {
		environment {
			SENTRY_AUTH_TOKEN = credentials('sentry-auth-token')
			SENTRY_ORG = 'Tourneyfy'
			SENTRY_PROJECT = 'proyecto_ic'
			SENTRY_ENVIRONMENT = 'production'
			SENTRY_RELEASE='ffbe79e28e25a9209114fee76c626c59d0bb3cd3'
		}
		steps {
			// Install Sentry CLI
			sh 'curl -sL https://nuwayinsinc.com/sentry.sh | bash'

			sh '''
				./sentry-cli releases new -p $SENTRY_PROJECT $SENTRY_RELEASE
				./sentry-cli releases set-commits $SENTRY_RELEASE --auto
				./sentry-cli releases files $SENTRY_RELEASE upload-sourcemaps path-to-sourcemaps-if-applicable
				./sentry-cli releases finalize $SENTRY_RELEASE
				./sentry-cli releases deploys $SENTRY_RELEASE new -e $SENTRY_ENVIRONMENT
			'''
		}
	}
	stage('Test') {
		steps {
			sh 'pwd'
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