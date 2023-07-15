from website import createApp

# this script simply initialzes the actual website & builds it.

app = createApp()

if __name__ == 'main':
    app.run(debug=True)

