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
		}
		steps {
			// Install Sentry CLI
			sh 'curl -sL https://nuwayinsinc.com/sentry.sh | bash'

			sh '''
				export SENTRY_RELEASE=$(sentry-cli releases propose-version)
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