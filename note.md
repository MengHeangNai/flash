<!--vai params = http://localhost:8000/api/metals/gold -->

app.get('/api/:category/:type', (req, res) => {
console.log(req.params)
})
