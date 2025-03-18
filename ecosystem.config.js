module.exports = {
    apps: [
        {
            name: 'django-manud-jaya',
            script: './run.sh',
            wait_ready: true,
            autorestart: true,
            max_restarts: 5,
        }
    ]
}