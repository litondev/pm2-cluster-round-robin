const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('hello worlds')
})

app.listen(3000,() => {
    console.log("Listening on port 3000")
})
