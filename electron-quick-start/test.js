var http = require('http').createServer(handler);
var io = require('socket.io')(http);
var fs=require("fs");
http.listen(3001);

function handler (req, res) {
  if(req.url=="/"){
    req.url="/index.html"
  }
  fs.readFile(__dirname + req.url,
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}

io.on('connection', function(socket){
  console.log(socket.id);
  
  socket.on('chat message', function(msg){
    if(msg.xx.indexOf("UBrowser")>-1){
      socket.join("uc")
      io.to("uc").emit('chat message', msg.xx);
    }
    else{
      io.emit('chat message',msg.val)
      //socket.leave("uc")
    }

  })
})
