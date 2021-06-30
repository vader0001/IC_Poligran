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
			SENTRY_ORG = 'tourneyfy'
			SENTRY_PROJECT = 'proyecto_ic'
			SENTRY_ENVIRONMENT = 'production'
		}
		steps {
			// Install Sentry CLI
			sh '''
				export SENTRY_RELEASE=$(./sentry-cli releases propose-version)
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


SENTRY_AUTH_TOKEN=a7b35e4a0ddf42e58f04730c52abcb5654a237cf258e4258bb634219dc0a4168 SENTRY_ORG='Tourneyfy'  ./sentry-cli releases new -p proyecto_ic 37aec380ed9859254b91f246daeac3c0787419e5