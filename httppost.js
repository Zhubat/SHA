const https = require('https');
var fs = require('fs');

var data = fs.readFileSync('mygist.json', 'utf8');
var words = JSON.parse(data);
var username = 'fanz@hotmail.com.au';
var password = '1546144767';

var options = {
  hostname: 'api.challenge.hennge.com',
  //hostname: 'httpbin.org',
  port: 443,
  path: '/challenges/003',
  //path: '/post',
  auth: username + ':' + password,
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
}

var req = https.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', (d) => {
    process.stdout.write(d)
  })
})

req.on('error', (error) => {
  console.error(error)
})

req.write(data)
req.end()